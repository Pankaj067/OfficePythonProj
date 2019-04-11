from nltk.tokenize import sent_tokenize, word_tokenize

example ="Weather is great , let's go for party!"

print(sent_tokenize(example))

print(word_tokenize(example))

for i in word_tokenize(example):
	print(i)