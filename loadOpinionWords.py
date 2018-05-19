def loadOpinionWords(path):
	words = []

	with open(path, "r") as f:
		for line in f:
			line = line.replace("\n", "")
			word = line.replace("\r", "")
			words.append(word)

	return words