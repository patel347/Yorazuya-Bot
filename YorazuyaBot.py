import asyncio
import aiohttp
import json

from RSSReader import RSSReader
from Config import Config

class YorazuyaBot:

    """Main Bot Program"""
    # self.loop = None

    CHANNEL_ID = 147031379438338048
    NEWS_CHANNEL_ID = 156859545916801024
    URL = 'https://discordapp.com/api'


    def __init__(self):
        self.loop = asyncio.get_event_loop()

        #get bot token from config file
        config = Config('config.ini')
        self.token = config.token
        self.last_sequence = None

        #get gateway from cache here
        #TODO
        self.ws = None


    async def api_call(self,path, method="GET", **kwargs):
        """Return the JSON body of a call to Discord REST API."""
        defaults = {
            "headers": {
                "Authorization": f"Bot {self.token}",
                "User-Agent": "dBot Patel347"
            }
        }
        kwargs = dict(defaults, **kwargs)
        with aiohttp.ClientSession() as session:
            async with session.request(method, f"{self.URL}{path}",**kwargs) as response:
                assert 200 == response.status, response.reason
                return await response.json()

    async def heartbeat(self, interval):
        """Send every interval ms the heatbeat message."""
        while True:
            await asyncio.sleep(interval / 1000)  # seconds
            await self.ws.send_json({
                "op": 1,  # Heartbeat
                "d": self.last_sequence
            })

    async def send_message(self,content,channelID):
        """Send a message with content to the recipient_id."""
        # channel = await api_call("/users/@me/channels", "POST",json={"recipient_id": recipient_id})
        return await self.api_call(f"/channels/{channelID}/messages", "POST",json={"content": content})

    async def handshake(self):
        await self.ws.send_json(
            {
               "op": 2,  # Identify
               "d": {
                   "token": self.token,
                   "properties": {},
                   "compress": False,
                   "large_threshold": 250
               }
            }
        )
        print('sent handshake')

    async def messageCreatedEvent(self,messageData):
        '''when a message is sent'''
        print()
        print(messageData)
        print()
        user = messageData['author']['username']
        message = messageData['content']
        channelID = messageData['channel_id']
        if message.startswith('!'):
            #message parser function here
            splitMessage = message.split(' ', 1)
            command = splitMessage[0]
            if command == '!echo':
                text = splitMessage[1]
                task = asyncio.ensure_future(self.send_message(text,channelID))
            elif command == '!angry':
                text = splitMessage[1]
                task = asyncio.ensure_future(self.send_message(text.upper(),channelID))
            elif  command == '!quit':
                task = asyncio.ensure_future(self.send_message('Bye :wave:',channelID))
                print('Bye bye!')
                await asyncio.wait([task])
                return -1


    async def parseEvent(self,data):
        event = data['t']
        test = None
        if event == "MESSAGE_CREATE":
            # print(data['d'])
            test = await self.messageCreatedEvent(data['d'])
        return test
                        

    async def run(self):
        #temp get gateway address
        response = await self.api_call("/gateway") 
        self.gateway = response['url']

        with aiohttp.ClientSession() as session:
            async with session.ws_connect(f"{self.gateway}?v=6&encoding=json") as ws:
                self.ws = ws
                async for msg in ws:
                    data = json.loads(msg.data)

                    if data["op"] == 10:  # Hello
                       asyncio.ensure_future(self.heartbeat(data['d']['heartbeat_interval']))
                       await self.handshake()
                       
                    elif data["op"] == 11:  # Heartbeat ACK
                        print('Heartbeat Acked')
                        pass
                    elif data["op"] == 0:  # Dispatch
                        # print(data['t'], data['d'])
                        self.last_sequence = data['s']
                        test = await self.parseEvent(data)
                        if test == -1:
                            break
                    else:
                       print(data)

    def start(self):
        # loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.run())
        self.loop.close()

def main():
    print('Starting Bot')
    bot = YorazuyaBot()
    bot.start()

    
    # getLatestLeagueNews()


if __name__ == "__main__":
    main()