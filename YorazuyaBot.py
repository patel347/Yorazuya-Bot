import requests
from RSSReader import RSSReader
channelID = 147031379438338048
NEWS_CHANNEL_ID = 156859545916801024

def sendMessage(channelID,message):
    token = "Bot MjQ5MjcwMzU3MTY3NDM5ODcz.CxEPDg.rca_6ll3s2RhqoeqJZQonIzhJdU"
    Authorization ={'Authorization': token}
    r = requests.post('https://discordapp.com/api/channels/%s/messages' %channelID, data = {'content': message}, headers = Authorization)

def getLatestLeagueNews():
    RSS_LINK = 'http://euw.leagueoflegends.com/en/rss.xml'
    LeagueNewsReader = RSSReader(RSS_LINK)
    latestDateRead = LeagueNewsReader.getDateOfLatestRead()
    newItems = LeagueNewsReader.getNewItems(latestDateRead)
    if newItems != None:
        for item in newItems:
            sendMessage(NEWS_CHANNEL_ID,item.title + ' ' + item.link )


def main():
    getLatestLeagueNews()


if __name__ == "__main__":
    main()