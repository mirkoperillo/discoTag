import sys
import argparse
import os

optParser = argparse.ArgumentParser()
optParser.add_argument('--startdoc',help='initial doc (default 0)')
optParser.add_argument('--lastdoc',help='latest doc (default 50)')
''' add tag parameter '''
optParser.add_argument('--tag',help='tag to search')
''' add input file parameter '''
optParser.add_argument('--file',help='input file')
''' add output file parameter '''
optParser.add_argument('--output',help='output file (default input file .extract)')
optParser.add_argument('--pretty',help='format the output',action="store_true")

args = optParser.parse_args()

''' validate input parameters'''
if(args.startdoc) :
	start =  int(args.startdoc)
else : 
	start = 0

if(args.lastdoc) :
	end =  int(args.lastdoc)
else : 
	end = 50
if(not args.file) :
	print '--file is mandatory'
	sys.exit(-1)
else : 
	filename = args.file	

if(not args.tag) :
	print '--tag is mandatory'
	sys.exit(-1)
else : 
	tag = args.tag	

if(args.output) :
	outputFile = args.output
else : 
	outputFile = filename+'.extract'	


buffer_size = 1000000

out = open(outputFile,'w')
reader = open(filename,'r')
founded = 0

out.write('<root>')
while True and end > 0 :
	buffer = reader.read(buffer_size)
	if(len(buffer) == 0) :
		break
	current = 0
	while True and end > 0:
		startIndex = buffer.find('<'+tag,current)
		if startIndex != -1 :
			start = start -1
			endIndex = buffer.find('</'+tag+'>',startIndex)
			if(endIndex == -1) :
				endIndex = buffer.find('/>',startIndex)
			if endIndex != -1 :
				if(start < 0 ) : 
					out.write('<'+tag+buffer[startIndex+1+len(tag):endIndex]+'</'+tag+'>')
					founded = founded +1
				current = endIndex
				end = end - 1
			else : 
				reader.seek(startIndex)
				break
		else:
			break
out.write('</root>')
out.close()
print 'elements founded: '+str(founded)
if(args.pretty) :
	os.system('xmllint --format '+ outputFile+'  -o '+outputFile)