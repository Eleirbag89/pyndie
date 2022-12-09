import ply.lex as lex
import re

tokens = [
	'NUMBER',
	'EQUALS',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'MODULE',
	'PRINT',
	'AND',
	'RETURN',
	'HEY',
	'OH',
	'AS',
	'SAI',
	'WHILE',
	'DO',
	'STRING_CAST',
	'CHE',
	'CALL',
	'SPACE',
	'EXCLAMATION_MARK',
	'QUESTION_MARK',
	'MINOR',
	'MAJOR',
	'END_LINE',
	'TRUE',
	'FALSE',
	'NOT',
	'OR',
	'ELSE',
	'NAME',
	'COMPARISON',
	'DQUOTE',
	'EMPTY_PARAM',
	'DRUG',
	'POINT'
	]


#TOKENS
def t_SPACE(t):
	r'\ '
	if lex.dquotes:
		t.type = 'NAME'
		t.value = ' '
		return t
	else: pass
	
def t_EQUALS(t):
	r'(è|sono|sei|siete|siamo|ero|eri|era|eravamo|eravate|sarà|sarò)\ '
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
	
def t_ARTICLE(t):
	r'(il|lo|la|gli|le|un|uno|una|mi|ti|ci|si|vi|i)\ + |un\'|l\''
	if lex.dquotes:
		t.type = 'NAME'
		return t
	else:
		pass

def t_TRUE(t):
	r'(vero|giusto|vera|giusta)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_COMPARISON(t):
	r'(sembra|sembri|sembriamo|sembrate|sembro)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_FALSE(t):
	r'(falso|falsa|bugia|menzogna)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
def t_NOT(t):
	r'(non)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_ELSE(t):
	r'(invece|altrimenti)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_STRING_CAST(t):
	r'(letteralmente|letterale)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_EMPTY_PARAM(t):
	r'(\.\.\.)\ '
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value =""
	return t
def t_POINT(t):
	r'(\.|\,)'
	if lex.dquotes:
		t.type = 'NAME'
	return t


	
def t_OR(t):
	r'(o|oppure)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_END_LINE(t):
	r';'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
	
def t_RETURN(t):
	r'dammi'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_EXCLAMATION_MARK(t):
	r'!'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_QUESTION_MARK(t):
	r'(\?)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_TIMES(t):
	r'per\ +'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '*'
	return t
	
def t_DIVIDE(t):
	r'diviso\ +'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '/'
	return t

def t_MINOR(t):
	r'minore'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '<'
	return t

def t_MAJOR(t):
	r'(maggiore|maggiori)'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '>'
	return t
	
def t_CALL(t):
	r'(ricordare|ricorda|ricordo)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_HEY(t):
	r'hey|ei|ehi'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_OH(t):
	r'(oh)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_AS(t):
	r'come'
	if lex.dquotes:
		t.type = 'NAME'
	return t

def t_SAI(t):
	r'sai'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_CHE(t):
	r'che'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_AND(t):
	r'(e)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_PRINT(t):
	r'(sussurra|gridavate|gridava|gridavi|gridavano|grido|grida|sussurravate|sussurravi|sussurrava|sussurra|sussurro)\ +'
	return t
	
def t_WHILE(t):
	r'(finchè|finché)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
def t_DO(t):
	r'(faccio|fai|fa|facciamo|fate|fanno)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t

def t_MODULE(t):
	r'(divisibile|resto|resta)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '%'
	return t
	
def t_PLUS(t):
	r'più'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '+'
	return t
	
def t_MINUS(t):
	r'(meno)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	else:
		t.value = '-'
	return t
	
def t_DQUOTE(t):
	r'\"'
	lex.dquotes = not(lex.dquotes)
	return t

def t_DRUG(t):
	r'(paracetamolo|tachipirina|aulin|oki|brioschi)\ +'
	if lex.dquotes:
		t.type = 'NAME'
	return t
	
# Ignored characters
t_ignore = "\t"


def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z_0-9ò]*'
	return t

def t_NUMBER(t):
	r'\d+'
	if not(lex.dquotes):
		t.value = int(t.value)    
		return t
	t.type = 'NAME'
	return t



def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

	
# Build the lexer
lex.dquotes= False
lex.lex(reflags=re.UNICODE | re.VERBOSE)