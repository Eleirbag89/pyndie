from ply import *
import lang.pyndielexer as lexer

# Precedence rules for the arithmetic operators

tokens = lexer.tokens
precedence = (
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE', 'MODULE'),
	('right','UMINUS'),
	)

# dictionary of names (for storing variables)
names = { }
# hack for sharing variable number
variable_counter=[0]
variable_counter[0]=0

def p_program_statements(p):
	'program : statements'
	p[0] = p[1]

def p_statements_statement(p):
	'statements : statement statements'
	tmp = p[1]
	if p[2] != "":
		tmp = str(tmp)+"\n"+str(p[2])
	p[0] = tmp
	
def p_statements_statement_eol(p):
	'statements : statement POINT statements'
	tmp = p[1]
	if p[2] != "":
		tmp = str(tmp)+"\n"+str(p[3])
	p[0] = tmp
	
def p_statements_empty_statement(p):
	'statements : empty_statement'
	p[0] = ""
	
def p_statement_empty(p):
    'empty_statement :'
    p[0] = ""
	
def p_declare_function(p):
	'statement : SAI CHE EQUALS variable AS params HEY statements OH'
	tmp = "global "+str(p[4]).rstrip().replace(" ", "_")+"\n"
	tmp = tmp + "def "+str(p[4]).rstrip().replace(" ", "_")+"("+p[6]+"):"
	substm = str(p[8]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp

def p_statement_function_invoke(p):
	'statement : function_invoke'
	p[0] = p[1]
	
def p_expression_function_invoke(p):
	'expression : function_invoke'
	p[0] = p[1]
	
def p_function_invoke(p):
	'function_invoke : CALL variable CHE EQUALS params_actual EXCLAMATION_MARK'
	tmp = str(p[2]).rstrip().replace(" ", "_")+"("+p[5]+")"
	p[0] = tmp


def p_function_params(p):
	'''params : variable AND params
			  | variable
			  | EMPTY_PARAM'''
	varName = ""
	if p[1] != "":
		try:
			varName = names[p[1]] 
		except KeyError:
			names[p[1]] = "fun"+str(variable_counter[0])
			variable_counter[0] = variable_counter[0]+1
			varName = names[p[1]]
	if len(p) < 3:
		p[0] = varName.rstrip()
	else:
		p[0] = varName.rstrip()+","+str(p[3]).rstrip()

def p_function_params_actual(p):
	'''params_actual : expression AND params_actual
			  | expression
			  | EMPTY_PARAM'''
	if len(p) == 1:
		p[0] = ""
	else:
		if len(p) < 3:
			p[0] = str(p[1]).rstrip()
		else:
			p[0] = str(p[1]).rstrip()+","+str(p[3]).rstrip()

	
def p_statement_return(p):
	'''statement : RETURN expression'''
	p[0] = "return " + str(p[2]) 


def p_statement_assign(p):
	'''statement : variable EQUALS expression'''
	varName = ""
	try:
		varName = names[p[1]] 
	except KeyError:
		names[p[1]] = "var"+str(variable_counter[0])
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[1]]
	p[0] = str(varName) + "=" + str(p[3]) 
	
	
def p_statement_if(p):
	'''statement : boolean_expression QUESTION_MARK statements HEY'''
	
	tmp = "if " + p[1] +":"
	substm = str(p[3]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
	
def p_statement_while(p):
	'''statement : WHILE boolean_expression DO statements HEY'''
	
	tmp = "while "+p[2]+":"
	substm = str(p[4]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
def p_statement_if_else(p):
	'''statement : boolean_expression QUESTION_MARK statements ELSE statements HEY'''
	substm = str(p[3]).split('\n')
	tmp = "if " + str(p[1]) + ":"
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	tmp = tmp + "\nelse:"
	substm = str(p[5]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
def p_boolean_expression(p):
	'''boolean_expression : expression COMPARISON expression
						| expression MINOR expression
						| expression MAJOR expression'''

	if p[2] == "<":
		tmp = str(p[1])+" < "+str(p[3])
	elif p[2] == ">":
		tmp = str(p[1])+" > "+str(p[3])
	else:
		tmp = str(p[1])+" == "+str(p[3])
	p[0] = tmp
	
def p_boolean_expression_not(p):
	'''boolean_expression : expression NOT COMPARISON expression
						| expression NOT MINOR expression
						| expression NOT MAJOR expression'''
	if p[3] == "<":
		tmp = "not("+str(p[1])+" < "+str(p[4])+")"
	elif p[3] == ">":
		tmp = "not("+str(p[1])+" > "+str(p[4])+")"
	else:
		tmp = "not("+str(p[1])+" == "+str(p[4])+")"

	p[0] = tmp

def p_boolean_expression_and(p):
	'''boolean_expression : boolean_expression AND boolean_expression'''
	p[0] = str(p[1]) + " and " + str(p[3])

def p_boolean_expression_or(p):
	'''boolean_expression : boolean_expression OR boolean_expression'''
	p[0] = str(p[1]) + " or " + str(p[3])
	
def p_expression_string(p):
	'expression : DQUOTE variable DQUOTE'
	tmp = p[2].replace("_", "")
	p[0] = "\""+str(tmp)+"\""


def p_statement_print(p):
	'''statement : PRINT expression'''
	tmp = p[2].replace("_", "")
	p[0] = "print("+str(tmp+")")
	
def p_expression_string_cast(p):
	'''expression : STRING_CAST variable'''
	tmp = p[2]
	try:
		tmp = str(names[tmp])
	except:
		tmp = var_to_value(tmp, p.lineno(1))
	p[0] = "str("+str(tmp+")")
	
def p_expression_uminus(p):
	'expression : MINUS statement %prec UMINUS'
	p[0] = "-"+p[2]


	
def p__booleans_true(p):
	'boolean_expression : TRUE'
	p[0] = str(True)

def p__booleans_false(p):
	'boolean_expression : FALSE'
	p[0] = str(False)
	
def p_expression_boolean_expression(p):
	'expression : boolean_expression'
	p[0] = str(p[1])
	
def p_expression_number(p):
	'expression : numbers'
	p[0] = str(p[1])
	
def p_drug_number(p):
	'''numbers : DRUG NUMBER'''
	p[0] = str(p[2])

def p_expression_binop(p):
	'''expression : expression PLUS expression
					| expression MINUS expression
					| expression TIMES expression
					| expression DIVIDE expression
					| expression MODULE expression'''
	if p[2] == '+'  : p[0] = str(p[1]) +"+"+ str(p[3])
	elif p[2] == '-': p[0] = str(p[1]) +"-"+ str(p[3])
	elif p[2] == '*': p[0] = str(p[1]) +"*"+ str(p[3])
	elif p[2] == '/': p[0] = str(p[1]) +"/"+ str(p[3])
	elif p[2] == '%': p[0] = str(p[1]) +"%"+ str(p[3])
def p_expression_variable(p):
	'''expression : variable'''
	try:
		p[0] = str(names[p[1]])
	except:
		p[0] = var_to_value(p[1], p.lineno(1)) #var_or_input(p[1], p.lineno(1))
		
def p_variable_name(p):
	'''variable : names
			| names END_LINE'''
	try:
		p[0] = str(p[1])
	except:
		p[0] = "ERROR"
	
def p_variable_names(p):
	'names : NAME names'
	p[0] = str(p[1])
	if str(p[2]) != "":
		p[0] = p[0] +'_'+str(p[2])
	
		
def p_variable_names_empty(p):
	'names :'
	p[0] = ""

def p_error(p):
	# get formatted representation of stack
	stack_state_str = ' '.join([symbol.type for symbol in rparser.symstack][1:])

	if p != None:
		print("Syntax error at line '%s'" % 	p.lexer.lineno)
		print('Parser State:{} {} . {}'.format(rparser.state, stack_state_str,p))
		exit()

#rparser = yacc.yacc(errorlog=yacc.NullLogger())
rparser = yacc.yacc()

def parse(data,debug=0):
    rparser.error = 0
    p = rparser.parse(data,debug=debug,tracking=True)
    if rparser.error: 
        print(rparser.error)
        return None
    return p

def var_to_value(varname, line):
	value = ""
	for x in varname.split('_'):
		if x != "":
			value = value + str(len(x) % 10)
	if len(value) > 1 and value.startswith("0"):
		print("Syntax error at line '%s': invalid number starting with zero" % 	line)
		exit()
	return value