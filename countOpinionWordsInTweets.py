import json
import os
import langdetect
import nltk
import progressbar
import operator

def countOpinionWordsInTweets(tweetsPath, possWords):
	counted = {}
	count = 0

	files = os.listdir(tweetsPath)

	bar = progressbar.ProgressBar(maxval = 20000 * len(files), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	print("Counting words")
	bar.start()


	for filename in files:
		with open(tweetsPath + "/" + filename, "r") as f:
			for line in f:
				count += 1

				tweet = json.loads(line)
				tweetText = tweet["text"].lower()
				tokens = nltk.regexp_tokenize(tweetText, r"[A-Za-z]+")

				# Samo angleski tweeti
				try:
					lang = langdetect.detect(tweet["text"])
					if lang == "en":
						for token in tokens:
							if token in possWords:
								if token in counted:
									counted[token] += 1
								else:
									counted[token] = 1
								
				except langdetect.lang_detect_exception.LangDetectException:
					pass
				
				bar.update(count)


	bar.finish()

	counted = sorted(counted.items(), key=operator.itemgetter(1), reverse=True)
	return counted
