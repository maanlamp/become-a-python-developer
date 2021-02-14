# Design patterns zijn vernoemd naar de principes waarop ze gebaseerd zijn.
# Als je deze patterns bij naam kent, kun je gebruik maken van dat gedeelde
# vocabulaire waar andere programmeurs ook mee communiceren.

# Creational design patterns
	# Dit soort design patterns beschrijven systematische creatie van objecten

	## 1. Factory pattern
		# met een factory kun je objecten aanmaken d.m.v. een functie
		# Ik begrijp niet waarom je dit zou gebruiken maar ik heb geleerd hoe je een klasse
		# schrijft in python.
class Dog:
	def __init__(self, name):
		self._name = name
	def speak(self):
		return "Woef!"

class Cat:
	def __init__(self, name):
		self._name = name
	def speak(self):
		return "Miauw!"

def getPet(pet):
	"""Haal dynamisch een dier op"""
	pets = dict(dog=Dog("Bertus"), cat=Cat("Otje"))
	return pets[pet]

otje = getPet("cat")
bertus = getPet("dog")

print(otje.speak()) # Miauw!
print(bertus.speak()) # Woef!
	
	## 2. Singleton pattern
		# Een singleton is een enkele instantie van een klasse,
		# waardoor er global state gedeeld kan worden als object i.p.v. gewone variables.
		# Ook hier ontgaat mij het nut. Er mist uitleg waarom dit nuttig is, en ik ben
		# van mening dat een global dict precies hetzelfde werkt zonder onnodige poespas
class Secrets:
	_sharedState = {}
	def __init__(self):
		self.__dict__ = self._sharedState

class Singleton(Secrets):
	"""Deze klasse omvat alle variables uit Secrets"""
	def __init__(self, **kwargs):
		self._sharedState.update(kwargs)
	def __str__(self):
		return str(self._sharedState)

x = Singleton(secret="Mijn sokken zijn blauw.")

print(x) # {'secret': 'Mijn sokken zijn blauw.'}

	## 3. Builder pattern
		# Een builder hakt het creëren van een object in kleinere stukjes via methods op een klasse.
		# Interessante manier van objects aanmaken. Mijn voorkeur gaat naar object literals met
		# nauwe verwerking in een type system, maar ik snap dat je dat in python niet zal krijgen.
class Car:
	def __init__(self):
		self.brand = None
		self.model = None
		self.russian = None
	def __str__(self):
		return "Car brand: {}, model: {}, Russian?: {}".format(self.brand, self.model, self.russian and "DA BLYAT" or "NJET PIZDEC")

class CarBuilder:
	def __init__(self):
		self.car = Car()
	def addBrand(self, brand):
		self.car.brand = brand
		return self
	def addModel(self, model):
		self.car.model = model
		return self
	def addRussian(self, russian):
		self.car.russian = russian
		return self
	def build(self):
		return self.car

car = CarBuilder().addBrand("Lada").addModel("Niva Urban").addRussian(True).build()
print(car) # Car brand: Lada, model: Niva Urban, Russian?: DA BLYAT

	## 4. Prototype pattern
		# Prototypes zijn een soort factory. Javascript gebruikt deze prototypes voor klassen.
		# python heeft geen ingebouwde hiërarchieën, dus moet je zelf d.m.v. klassen iets soortgelijks
		# implementeren (als je zoiets wil).
		# In python is dit compleet overbodig omdat classes bestaan.
import copy
def makePrototype(klass):
	return copy.deepcopy(klass)
pipiProto = makePrototype(Cat("Pipi"))
print(pipiProto.speak()) # Miauw!

# Structural design patterns
	# Dit soort design patterns beschrijven de structuur van objecten

	## 1. Decorators
		# Een decorator is een functie die een object uitbreidt.
		# Hele moeilijke manier, ik denk dat ik het wel begrijp.
		# Gek om een functional programming pattern te zien in een voornamelijk OOP tutorial
def makeAnchor(fun):
	def decorator():
		return "<a>{}</a>".format(fun())
	return decorator

@makeAnchor
def makeText():
	return "Hello, world!"

print(makeText()) # <a>Hello, world!</a>

	## 2. Proxy
		# Een proxy is een object dat doet alsof het een ander object is.
		# Volgens de uitleg van deze man is het niet hetzelfde als wat ik ken als PRoxy,
		# namelijk de ingebouwde proxy-constructor van javascript.
		# Of ik begrijp hem niet goed, kan ook.
test = dict(test="test")

class Proxy:
	def __init__(self, target):
		self._target = target
	def get(self, key, otherwise = "nothing"):
		if key in self._target:
			return self._target[key]
		else:
			return otherwise

test2 = Proxy(test)
print(test["test"], test2.get("test"), test2.get("tosti")) # test test nothing

# Behavioural design patterns
	# Dit soort design patterns beschrijven het gedrag van objecten

	## 1. Observer
		# Een observer observeert veranderingen binnen een object en geeft
		# mogelijkheden om daarop te reageren.
		# OOP mensen hebben functions as values ontdekt. Duidelijk.
class Subject:
	_listeners = []
	def listen(self, listener):
		self._listeners.append(listener)
		return self
	def emit(self, value):
		for listener in self._listeners:
			listener(value)

broadcaster = Subject()
broadcaster.listen(print)
broadcaster.emit("BOODSCHAP!") # prints "BOODSCHAP!"

	## 2. Visitor
		# Een visitor is een manier om een klasse uit te breiden zonder de code direct
		# aan te pakken. Dit is een welbekend pattern, maar niet om de jusite reden.
		# OOP heeft nogal wat problemen, waaronder moelijke refactoring. Alles hangt
		# nauw samen dus je wil niks veranderen. Om dat op te lossen gebruiken ze
		# dan visitors, maar de juiste oplossing is om niet zulke slecht refactorable code te schrijven.
		# Je kunt bijvoorbeeld functionele compositie gebruiken:
def compose(funs):
	def inner(x):
		for fun in funs:
			x = fun(x)
		return x
	return inner

def mult(a):
	def inner(b):
		return a * b
	return inner

double = mult(2)
quadrupleAndPrint = compose([double, double, print])
sayEight = quadrupleAndPrint(2) # 8

	## 2. Iterator
		# Een iterator is een functie/object dat een interface biedt om over waardes te itereren.
def countTo(n):
	x = 1
	while x <= n:
		yield x
		x = x + 1

for num in countTo(5): # telt op van 1 tot 5
	print(num)