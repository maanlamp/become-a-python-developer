# Tools schrijven in python

# Een tool is conceptueel hetzelfde als een functie:
# Een algoritme dat een bepaalde taak behandelt zodat je dat niet steeds zelf moet doen.

# Python is een veelgebruikte taal voor tools, omdat het zo'n lage instapdrempel heeft.
# Wat belangrijk is om te weten, is hoe python via de CLI kan werken

# De "arguments" van een tool geef je mee via de CLI, en sla je op in python met sys
import sys
args = sys.argv

print(args) # python ./4-tools.py > ['.\\4-tools.py', 'test']

# Laat ik tooltje maken waarmee ik mezelf kan vermaken als ik me verveel tijdens de lockdown.

import json
import urllib2
import random
count = int(args[1])
words = json.loads(urllib2.urlopen("https://raw.githubusercontent.com/RazorSh4rk/random-word-api/master/words.json").read())
words = filter(lambda x: len(x) <= 5, words)
start = random.randint(0, len(words) - 1)
words = words[start:random.randint(start, len(words))]

def letterOrNot(letter):
	if random.randint(0, 2) == 0:
		return letter
	return "_"

print("Raad het woord!")
for word in words:
	tries = 0
	garbled = "".join(letterOrNot(letter) for letter in word)
	retry = True
	while retry:
		guess = raw_input("< {}{}\n> ".format(word[:tries], garbled[tries:]))
		if guess == word:
			print("< Correct! Nieuw woord komt eraan.")
			retry = False
		else:
			print("Nope >:)")
			tries += 1
		if tries == len(word):
			print("Je hebt het niet geraden, dom! Het was natuurlijk {}!\n".format(word))
			retry = False