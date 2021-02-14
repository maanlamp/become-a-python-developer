# coding=utf-8
# dit bestand laadt niet lekker en dat schijnt te komen door een missende
# encoding definition, maar de andere bestanden werkten gewoon... raar.

# Serialistation is het transformeren van één format naar een ander format
# zoals json naar objects en terug

import pickle
# pickle schijnt een welbekende library te zijn om van en naar python specifieke data te serialisen

data = dict(
	test=123,
	name="Wouter",
	lang="python")

serialised = pickle.dumps(data) # dumps = dump string
print(serialised) # Print een reeks karakters die duidelijk niet meer het originele dict zijn

deserialised = pickle.loads(serialised) # loads = load string
print(deserialised) # {'lang': 'python', 'test': 123, 'name': 'Wouter'}

# repr() en type()
print(1, "1") # (1, '1')
# voor een print statement zijn 1 en "1" gelijk, maar dat is onhandig voor de menselijke lezer
# gebruik repr voor een correcte representatie van de data
print(repr(1), repr("1")) # ('1', "'1'")
# Nu staan er om beide waardes leestekens, maar de string heeft er twee paar..?

# type() geeft het datatype van de data die je als parameter meegeeft
print(1, repr(1), type(1)) # (1, '1', <type 'int'>)

# JSON
import json

test = {
	"name": "Wouter",
	"lang": "Python"
}

serialisedJson = json.dumps(data) # dumps = dump string (zelfde API als pickle)
print(serialisedJson) # {"lang": "python", "test": 123, "name": "Wouter"}
# json lijkt heel erg op python object literals, of andersom :)

deserialisedJson = json.loads(serialisedJson) # loads = load string (zelfde API als pickle)
print(deserialisedJson) # {u'lang': u'python', u'test': 123, u'name': u'Wouter'}
# de u'' syntaxis betekent dat het een unicode string is. Dat komt omdat json volgens
# specificatie unicode moet ondersteunen, omdat JSON van javascript komt, en dat
# ondersteunt natuurlijk UTF-16 unicode.

# niet elk python object kan naar json geserialised worden.
# Dat kun je oplossen met "default" in json.dumps.
from datetime import datetime
notJSONAble = {
	"Time": datetime(2020, 1, 1) # een datetime heeft geen json representatie
}
print(notJSONAble) # {'Time': datetime.datetime(2020, 1, 1, 0, 0)}
# print(json.dumps(notJSONAble)) # Als je de comment weghaalt krijg je TypeError: datetime.datetime(2020, 1, 1, 0, 0) is not JSON serializable

#maak een functie die wordt aangeroepen als de data niet serialisable is
def serialiseAnyway(x):
	return "{}-{}-{}".format(x.year, x.month, x.day)

print(json.dumps(notJSONAble,default=serialiseAnyway)) # {"Time": "2020-1-1"}