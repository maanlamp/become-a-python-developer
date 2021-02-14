# Een generator is een functie die gebruik maakt van het `yield` keyword.
	# Dat houdt in dat je de functie daar "op pauze zet", een waarde teruggeeft, en wacht totdat je weer verder wil.
	# Dit is handig voor bijvoorbeeld custom iterators, of voor het consumeren van
	# (een gedeelte van) een oneindige reeks, zonder dat je computer crasht.

def tillInfinityAndBeyond():
	x = 0
	while True:
		yield x
		x = x + 1

import itertools # we hebben itertools nodig om een gedeelte van een generator te pakken
for num in itertools.islice(tillInfinityAndBeyond(), 100):
	print(num) #prints the numbers 0..99

	# Naast generator functions heb je ook generator expressions.
	# dat zijn expressions die gebruik maken van de functionaliteit
	# van generators, zonder een hele functie te hoeven schrijven.

def capitalise(name):
	return "{}{}".format(name[0].upper(), name[1:])
names = ["bert", "gert", "jan", "geertje"]
capitalisedNames = [capitalise(name) for name in names] # list comprehension
print(capitalisedNames) # ['Bert', 'Gert', 'Jan', 'Geertje']
print((capitalise(name) for name in names)) # generator expression, print dan ook <generator object <genexpr> at 0x0000021824A87580>

def fib():
	a, b = 0, 1 # fibonacci reeks start met 0 en 1
	while True: # herhaal oneindig
		yield a
		a, b = b, a + b # vervang a met b, en tel a op bij b voor de volgende iteratie

print(list(itertools.islice(fib(), 10))) # consumeer de eerste 10 items van de generator in een lijst en print die.
# print [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] Werkt!

# Coroutines
# Een coroutine is een "functie" die iets doet met een gegeven waarde
# We kunnen een "echte" coroutine nabbotsen met generators dankzij de ".send" methode.

def printCoroutine():
	while True:
		x = yield
		print x

co = printCoroutine()
co.next() # Eerst zorgen dat we bij de yield statement aankomen
co.send("Hello") # > "Hello"
co.send("World") # > "World"

# Het is "good practise" om je generators in een try/except block te typen zodat
# eventuele errors behandeld kunnen worden

def safeCoroutine():
	i = 0
	try:
		while True:
			txt = yield
			if txt == "add":
				i += 1
			if txt == "sub":
			 i -= 1
	except GeneratorExit:
		print(i)

safeCo = safeCoroutine()
safeCo.next() #start de teller
safeCo.send("add") # geen print maar er is 1 bij i opgeteld (1).
safeCo.send("add") # geen print maar er is 1 bij i opgeteld (2).
safeCo.send("sub") # geen print maar er is 1 bij i afgetrokken (1).
safeCo.close() # stop de teller, print 1

# Coroutines met decorators
# Je kunt een decorator maken die elke mogelijke generator functie alvast "aanzet"
# door .next() aan te roepen
def makeCoroutine(f):
	def wrap(*args, **kwargs):
		co = f(*args, **kwargs) # roep functie f aan met alle parameters
		co.next() # start de coroutine
		return co
	return wrap

@makeCoroutine
def generatorTest():
	while True:
		x = yield
		print(x)

autoCo = generatorTest()
# autoCo.next() is niet meer nodig!
autoCo.send("Test, 123!") # print "Test, 123"