from loadOpinionWords import loadOpinionWords
from countOpinionWordsInTweets import countOpinionWordsInTweets
import json

negWords = loadOpinionWords("opinionWords/negative-words.txt")
posWords = loadOpinionWords("opinionWords/positive-words.txt")

counted = countOpinionWordsInTweets("tweets/:D :) =) =D :-) :-D", posWords)
counterJson = json.dumps(counted)

f = open("posWordsCounted.json", "w+")
f.write(counterJson)

# print(posWordsDictionary)