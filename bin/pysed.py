#!/usr/bin/python
# -*- coding: utf-8 -*-


'''usage: pysed [-h] [-v] [-p] [-s] [-b] [-n]

Utility that parses and transforms text

optional arguments:
  -h, --help		show this help message and exit
  -v, --version		print version and exit
  -p, --print		print text
  -s,			find and replace text
  -b,			add text before target
  -n,			add text after the target'''



import re
import sys
import subprocess



__author__ = "dslackw"
__version__ = "0.0.2"
__license__ = "GNU General Public License v3 (GPLv3)"
__email__ = "d.zlatanidis@gmail.com"




path = subprocess.check_output(['pwd'], shell=True).replace('\n', '/')


def PrintText(file, arg0, arg2, arg3):
	result = []

	try :
		file = open(path + file, 'r')

	       	read = file.read()
        	file.close()


		try:
		        find_text = re.findall(arg2, read)
		except re.error:
			sys.exit()
			
		if arg0 == '-p' or arg0 == '--print':
			print read,
			sys.exit()

		elif arg0 == '-s':
		        for char in find_text:
        		        result = read.replace(char, arg3)

		elif arg0 == '-b':
			for char in find_text:
                	        result = read.replace(char, arg3 + char)

		elif arg0 == '-n':
			for char in find_text:
                	        result = read.replace(char, char + arg3)

		else:
			print ('pysed: error argument')
			sys.exit()
		
	        if result == []:
			pass
		else:
        	        print result,	

	except IOError:
                print ("pysed: can't read %s: No such file or directory" % file)




def ReplaceText(file, arg1, arg2):
	result = []

	try:

	        file =  open(path + file, 'r+')
		read = file.read()
	
		try:
			find_text = re.findall(arg1, read)
		except re.error:
			sys.exit()

		for char in find_text:
			result = read.replace(char, arg2)

	        if result == []:
			pass
		else:
			file.seek(0)
			file.truncate()
			file.write(result)

		file.close()

	except IOError:
		print ("pysed: can't read %s: No such file or directory" % file)




def AppendText(file, arg0, arg1, arg2):
	result = []

	try:

		file = open(path + file, 'r+')
        	read = file.read()
	
		try:
		        find_text = re.findall(arg1, read)
		except re.error:
        	        sys.exit()
	

		if arg0 == '-b':
		        for char in find_text:
        		        result = read.replace(char, arg2 + char)

		else:
			for char in find_text:
        		        result = read.replace(char, char + arg2)

	        if result == []:
			pass
		else:
			file.seek(0)
			file.truncate()
	                file.write(result)

	        file.close()

	except IOError:
		print ("pysed: can't read %s: No such file or directory" % file)




def Version():
	print ('Version : '),  __version__	
	print ('License : '),  __license__
	print ('Email   : '),  __email__




def ArgumentsView():
	print ('usage: pysed [-h] [-v] [-p] [-s] [-b] [-n]\n')
        print ('Utility that parses and transforms text\n')
        print ('optional arguments:')
        print ('  -h, --help            show this help message and exit')
        print ('  -v, --version         print version and exit')
        print ('  -p, --print           print text')
        print ('  -s,                   find and replace text')
        print ('  -b,                   add text before target')
        print ('  -n,                   add text after the target')



def ArgumentsError(arg0, argx):
	print ('usage: pysed [-h] [-v] [-p] [-s] [-b] [-n]\n')

	if arg0 == '':
		print ('pysed: error: argument: expected one argument')


	elif arg0 in ['-h', '-v', '-p', '-s', '-b', '-n']:
		print ('pysed: argument %s: expected at least one argument' % arg0)

	else:
		print ('pysed: error: unrecognized arguments: %s %s' % (arg0, ' '.join(argx)))




def main():

	arg = sys.argv
	arg.pop(0)


	if len(arg) == 2:
		file = arg[1]

	elif len(arg) == 4:
		file = arg[3]

	elif len(arg) == 5:
		file = arg[4]



	if len(arg) == 0:
		ArgumentsError('', '')

	elif len(arg) == 1 and arg[0] == '-h' or len(arg) == 1 and arg[0] == '--help':
		ArgumentsView()

	elif len(arg) == 1 and arg[0] == '-v' or len(arg) == 1 and arg[0] == '--version':
		Version()

	elif len(arg) == 2 and arg[0] == '-p' or len(arg) == 2 and arg[0] == '--print':
		PrintText(file, arg[0], '', '')

	elif len(arg) == 5 and arg[1] == '-p' or len(arg) == 5 and arg[1] == '--print':
		PrintText(file, arg[0], arg[2], arg[3])
	
	elif len(arg) == 4 and arg[0] == '-s':
		ReplaceText(file, arg[1], arg[2])

	elif len(arg) == 4 and arg[0] == '-b':
		AppendText(file, arg[0], arg[1], arg[2])

	elif len(arg) == 4 and arg[0] == '-n':
		AppendText(file, arg[0], arg[1], arg[2])

	elif not any([len(arg) == 1 and arg[0] == '-h', len(arg) == 1 and arg[0] == '-v',
		len(arg) == 1 and arg[0] == '-p', len(arg) == 1 and arg[0] == '-s',
		len(arg) == 1 and arg[0] == '-b', len(arg) == 1 and arg[0] == '-n']):
		ArgumentsError(arg[0], arg[1:])

	elif arg[0] in ['-h', '-v', '-p', '-s', '-b', '-n']:
		ArgumentsError(arg[0], arg[1:])



if __name__ == "__main__":
    main()