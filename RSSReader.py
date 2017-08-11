import feedparser
import time

RSS_LINK = 'http://euw.leagueoflegends.com/en/rss.xml'
DATA_FILE = 'RSSData'


def main():

    feed = feedparser.parse(RSS_LINK)

    # latestItemDate = feed.entries[0].published_parsed

    # for story in feed.entries:
    #     print(story.published_parsed)
    #     print('\n')
    print(feed.entries[0].published)
    latestItemDate = getDateOfLatestRead()

    getNewItems(latestItemDate)

    input()

def getDateOfLatestRead():
    dateOfLatestRead = None

    try:
        dataFile  = open(DATA_FILE,'r')
        dateOfLatestRead = dataFile.readline()
        dataFile.close()
    except FileNotFoundError:
        print("file not found, making file")
        dateOfLatestRead = '2000 01 01 00 00 00'
        dataFile  = open(DATA_FILE,'w+')
        dataFile.write(dateOfLatestRead)
        dataFile.close()


    # dateOfLatestRead =  dateOfLatestRead.split(',')

    dateOfLatestRead  = time.strptime(dateOfLatestRead, "%Y %m %d %H %M %S %Z") 

    return dateOfLatestRead

def setDateOfLatestRead(dateToSet):
    dataFile  = open(DATA_FILE,'w+')
    dataFile.write('')
    dataFile.close()


def getNewItems(latestDateRead):
  

    feed = feedparser.parse(RSS_LINK)

    print(latestDateRead)


# def setRSSFeedLink():

# def printToConsole():

if __name__ == "__main__":
    main()


