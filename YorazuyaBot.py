import requests
channelID = 147031379438338048

def main():
    # my code here
    #helloString = "Hello World!"
    userinput = raw_input("Enter a message.")
    token = "Bot MjQ5MjcwMzU3MTY3NDM5ODcz.CxEPDg.rca_6ll3s2RhqoeqJZQonIzhJdU"
    Authorization ={'Authorization': token}
    r = requests.post('https://discordapp.com/api/channels/%s/messages' %channelID, data = {'content': userinput}, headers = Authorization)
    print userinput
    print r.text



if __name__ == "__main__":
    main()


