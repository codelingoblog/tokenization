#Top 10 most commonly occuring words in Alice's Adventures in Wonderland, Lewis Carrol.
import re
from collections import Counter					#Import Counter into our program.
regex = "([a-zA-Z]+)"
file = open("alice.txt","r")				#Open the book, stored as a text file.	
sentence = file.read().lower()					#Read the contents of book, convert all letters to their lower case and store them in a string.				
tokenized_words = re.findall(regex,sentence)	
wordcount = Counter(tokenized_words)			#Store words and their word counts in a Counter.
print(wordcount.most_common(10))				#Display the top 10 most commonly occuring words.

