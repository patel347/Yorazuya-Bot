import feedparser
import time

RSS_LINK = 'http://euw.leagueoflegends.com/en/rss.xml'
DATA_FILE = 'RSSData.txt'


def main():

    feed = feedparser.parse(RSS_LINK)

    # latestItemDate = feed.entries[0].published_parsed

   

    
    latestDateRead = getDateOfLatestRead()

    newItems = getNewItems(latestDateRead)
    if newItems != None:
        for item in newItems:
            print(item.title.encode('utf8'))
            print('\n')

    input()

def getDateOfLatestRead():
    dateOfLatestRead = None

    try:
        dataFile  = open(DATA_FILE,'r')
        dateOfLatestRead = dataFile.readline()
        dataFile.close()
    except FileNotFoundError:
        print("file not found, making file")
        dateOfLatestRead = 'Sat, 05 Aug 2017 19:34:59 +0000' #date this file was created
        dataFile  = open(DATA_FILE,'w+')
        dataFile.write(dateOfLatestRead)
        dataFile.close()

    dateOfLatestRead  = time.strptime(dateOfLatestRead, "%a, %d %b %Y %H:%M:%S %z") 

    return dateOfLatestRead


def setDateOfLatestRead(dateToSet):
    dataFile  = open(DATA_FILE,'w+')
    dataFile.write(dateToSet)
    dataFile.close()


def getNewItems(latestDateRead):
  

    feed = feedparser.parse(RSS_LINK)
    newLatestDateReadParsed = feed.entries[0].published_parsed
    newLatestDateRead =  feed.entries[0].published

    newItems= []

    for item in feed.entries:
        #manual parsing because saved date has been manually parsed and has a -1
        #the is_dst value casuing the comparisons to be incorrect.
        item.parsedDate  = time.strptime(item.published, "%a, %d %b %Y %H:%M:%S %z") 
        if latestDateRead < item.parsedDate:
            newItems.insert(0,item)
        if  item.parsedDate> newLatestDateReadParsed:
            newLatestDateRead = item.published
            newLatestDateReadParsed = item.parsedDate


    setDateOfLatestRead(newLatestDateRead)
    return newItems

# def setRSSFeedLink():

# def printToConsole():

if __name__ == "__main__":
    main()


