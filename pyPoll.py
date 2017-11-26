
#prompt for directory name and data file name
directoryName=input(print("What's the directory name where data file resides? "))
dataFileName=input(print("What's the data file name? "))

# we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join(directoryName,dataFileName)

#Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:

	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	#initialze variables
	firstLine=True
	totalVoters=0
	#initialize empty dictionary for candidates and votecounts
	candidateDict = {}
	#Read records of data file
	for record in csvreader:
		#skip first header row
		if firstLine == True:
			firstLine = False
			continue
		#start analysis from second row
		#Total voter count
		totalVoters=totalVoters+1
		
		# create dictionary entries for candidates and vote countes
		if record[2] in candidateDict:
			candidateDict[record[2]] = candidateDict[record[2]]+1
		else:
			candidateDict[record[2]] = 1
		
#write output to file
#filename = 'Resources/' + 'analysis_budget_data_1.csv'
outputFilename = directoryName+'/analysis_'+dataFileName
file = open(outputFilename, 'w')


file.write('Election Results'+'\n')
file.write('-------------------------------'+'\n')
file.write('Total voters: ' + str(totalVoters)+'\n')
file.write('-------------------------------'+'\n')

#initialize variables for previus candidate's vote count and winner
prevCount=0
winner=''
for candidate, count in candidateDict.items():
	file.write(candidate + ' ' + str(round(((count / totalVoters ) * 100),0))+ '% (' + str(count) + ')'+'\n')
	#find winner
	if count > prevCount:
		winner=candidate
	#for comparing count with previous candidate
	prevCount=count
file.write('-------------------------------'+'\n')
file.write('Winner: ' + winner + '\n')
file.write('-------------------------------')

file.close()

#read the output file and print on screen

file = open(outputFilename,'r')
print(file.read())
