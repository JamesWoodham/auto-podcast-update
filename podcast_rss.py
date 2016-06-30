#!/usr/bin/env python
import feedparser
import urllib3.request
import shutil
import re
import time
from datetime import datetime

linkList = []
linksList = []
nameList = []
dir = '/home/pi/python-stuff/auto-podcast-update/'
lastDateFilePath = dir+'last-date.txt'
feedsFilePath = dir+'feeds.txt'
audioDir = dir+'audio/'

lastDateFile = open(lastDateFilePath)
lastDateStr = lastDateFile.readline()
lastDateFile.close()
lastDate = datetime.strptime(lastDateStr[:19], '%Y-%m-%d %X')
print lastDate

nowDate = datetime.now()
print nowDate

feedsFile = open(feedsFilePath)
for url in feedsFile.xreadlines():
	feed = feedparser.parse(url)
	pubDateStr = feed['entries'][0]['published']
	newPubDateStr = pubDateStr[:25]
	pubDate = datetime.strptime(newPubDateStr, '%a, %d %b %Y %X')

	print pubDate > lastDate
	if pubDate > lastDate:
		print feed['entries'][0]['links'] #debug
		linksList.append(feed['entries'][0]['links'])
		name = re.sub("[-,: ]",'',feed['entries'][0]['title'])
		nameList.append(name)
feedsFile.close()

#update saved date of last operation
nowDateFile = open(lastDateFilePath, 'w')
nowDateFile.write(str(nowDate)[:19]) #only need the first 19 chars
nowDateFile.close()

for links in linksList:
	for link in links:
		print link['type'] #debug
		if link['type'] == "audio/mpeg" or link['type'] == "audio/mp3":
			linkList.append(link['href'])
print linkList

http = urllib3.PoolManager()
for i in range(len(linkList)):
	with http.urlopen('GET',linkList[i],preload_content=False) as response, open(audioDir+nameList[i]+'.mp3', 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
