from pathlib import Path
import pickle

def caseInsensitivize(s):
	dquote_split = s.split("\"")
	for i in range(0,len(dquote_split)):
		if i % 2 == 0:
			dquote_split[i] = dquote_split[i].lower()
	case_insensitive = ""
	for i in range(0,len(dquote_split)):
		if i % 2 != 0:
			case_insensitive =  case_insensitive +"\""+dquote_split[i]+"\""
		else:
			case_insensitive =  case_insensitive +dquote_split[i]
	return case_insensitive
	
def validate_program(s):
	cities = set()
	matches = findCity(s)
	cities_pickle = Path(__file__).with_name('cities.pickle')
	if not(cities_pickle.is_file()):
		p = Path(__file__).with_name('city_list.txt')
		with p.open('r') as file:
			while (line := file.readline().rstrip('\n')):
				cities.add(line.lower())
		with open(cities_pickle, 'wb') as f:
			# Pickle the 'data' dictionary using the highest protocol available.
			pickle.dump(cities, f, pickle.HIGHEST_PROTOCOL)
	else:
		with open(cities_pickle, 'rb') as f:
			# The protocol version used is detected automatically, so we do not
			# have to specify it.
			cities = pickle.load(f)
	
	if not(any(city in matches for city in cities)):
		print("Syntaxt error: a valid program MUST contains at least a city name")
		exit()
        
def validate_program_web(s):
	cities = set()
	matches = findCity(s)
	file = open('lang/city_list.txt')
	while (line := file.readline().rstrip('\n')):
		cities.add(line.lower().strip())
	if not(any(city in matches for city in cities)):
		print("Syntaxt error: a valid program MUST contains at least a city name")
		exit()
		
def findCity(s):
	matches = []
	splitting = s.replace('\"', '').replace('\t', ' ').replace('\n', ' ').split(' ')
	for index, item in enumerate(splitting):
		if item and item[0].isupper():
			match = ""
			for i in range(5):
				if (len(splitting) > index + i):
					match = match + " " + splitting[index + i]
					matches.append(match.lower().strip())

	return matches
