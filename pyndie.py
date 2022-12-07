import lang.pyndieparser as parser
import lang.utils as utils
import sys
import argparse

def main(argv=None):
		
	cmdArguments = argparse.ArgumentParser(description='Process some integers.')
	cmdArguments.add_argument('file', metavar='file', type=str,
                    help='the script to execute')
	cmdArguments.add_argument('-d', dest='debug', action='store_true',
                    help='debug flag')
	#cmdArguments.add_argument('arguments',  nargs='*', help='program arguments')

	args = cmdArguments.parse_args()
	debug = args.debug

	try:
		in_file = open(args.file,"r", encoding="UTF-8")
		source = in_file.read()
		s = source
		in_file.close()
		lines = s.split('\n')
		s = " \n".join(lines)
		s = s.replace("...", " ... ").replace("!", " ! ") + " "
	except EOFError:
		print("Eccezione")
	
	utils.validate_program(s)
	s = utils.caseInsensitivize(s)
	
	modu = parser.parse(s)
	
	if debug:
		print ("--- Source ---")
		print(source)
		print("--- Compiled ---")
		print(modu)
		print("--- Execution ---")
	try:
		pass
		exec(compile(modu, filename="<string>", mode="exec"))
	except Exception as e:
		if debug:
			print(str(e))
		else:
			print("Tutto è andato bene, non preoccuparti")
	if debug:
		print("--- END ---")

def webparse(lines):
	s = " \n".join(lines)
	s = s.replace("...", " ... ").replace("!", " ! ") + " "
	utils.validate_program_web(s)
	s = utils.caseInsensitivize(s)
	
	modu = parser.parse(s)
	try:
		exec(compile(modu, filename="<string>", mode="exec"))
	except Exception as e:
		print(str(e))

    
if __name__ == "__main__":
    main()