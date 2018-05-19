import json
import thread
import analyze_sentiment_nltk as asn
from pprint import pprint
import progressbar
import multiprocessing
import Lock

# def countFileLines(fileName):
# 	count=0
# 	with open(fileName, "r") as f:
# 		for line in f:
# 			count=count+1
# 	return count

# def threadCount(lines):
# 	analyze=asn.SentimentAnalyse()
# 	pos=0
# 	nev=0
# 	neg=0
# 	for line in lines:
# 		data=json.loads(line)
# 		res=analyze.analyse(data['text'])
# 		if(res[3]>0):
# 			pos=pos+1
# 		elif(res[3]<0):
# 			neg=neg+1
# 		else:
# 			nev=nev+1
# 	return [pos, nev, neg]


# analyze=asn.SentimentAnalyse()
# analyze.downloadLexicon()
# coreCount=1
# coreCount=multiprocessing.cpu_count()
# lineCount=len(open("Tweets/tweets.json").readlines(  ))
# linesPerThread=lineCount/coreCount
# pos=0
# nev=0
# neg=0
# with open("Tweets/tweets.json", "r") as f:
# 	#bar = progressbar.ProgressBar(maxval = 20000, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
# 	#bar.start()
# 	lineNumber=0
# 	lines=[]
# 	threads=[]
# 	cntr=0
# 	for line in f:
# 		lines.append(line)
# 		cntr=cntr+1
# 		if(len(lines)>=linesPerThread or cntr>=lineCount):
# 			try:
# 				thr=Thread(target=threadCount, args=(lines,))
# 				thr.start()
# 				threads.append(thr)
# 				lines=[]			
# 			except er:
# 				print("U done fucked up 1!" + str(er))
# 				break		

# 	for thread in threads:
# 		result=thread.join()
# 		pos=pos+result[0]
# 		nev=nev+result[1]
# 		neg=neg+result[2]
# 		#lineNumber = lineNumber + 1
# 		#bar.update(lineNumber)
# 		"""data=json.loads(line)	
# 		res=analyze.analyse(data['text'])
# 		if(res[3]>0):
# 			pos=pos+1
# 		elif(res[3]<0):
# 			neg=neg+1
# 		else:
# 			nev=nev+1
# 		"""
# 	#bar.finish()

# print("Positive: "+str(pos)+"\r\nNeutral: "+str(nev)+"\r\nNegative: "+str(neg)+"\r\n")

positiveTweets = 0
negativeTweets = 0
neutralTweets = 0

lock = Lock()

def analyzeFunction(lines):
	# positiveTweets
	pass

numberOfThreads = 4

lines = tuple(open("tweets/trump/990934408197804033_990931100171145216_20000", 'r'))


print(len(lines))