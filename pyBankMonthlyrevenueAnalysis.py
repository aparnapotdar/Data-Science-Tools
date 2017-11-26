# This program analyzes company's revenue data for months (Month, revenue)
# Provides total months , average revenue change, max revenue increase and decrease
# input - prompt for directory and data file name
# output - creates file with revenue analysis with file name prefix "analysis"
  
#prompt for directory name and data file name
directoryName=input(print("What's the directory name where data file resides? "))
dataFileName=input(print("What's the data file name? "))

# we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv

#csvpath = os.path.join('Resources', 'budget_data_1.csv')
csvpath = os.path.join(directoryName,dataFileName)

#Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:

	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	#initialze variables
	firstLine=True
	secondLine=True
	totalMonths=0
	totalrevenue=0
	currentRevenue=0
	prevRevenue=0
	increase=0
	decrease=0
	maxIncrease=0
	maxDecrease=0
	currentRevenueChange=0
	totalRevenueChange=0
	#Read records of data file
	for record in csvreader:
		#skip first header row
		if firstLine == True:
			firstLine = False
			continue
		#start analysis from second row
		#skip revenue change analysis for second row as it's the first month with revenue
		if secondLine == True:
			secondLine=False
			totalMonths=totalMonths+1
			currentRevenue = int(record[1])
			totalrevenue = totalrevenue + currentRevenue
			prevRevenue= int(record[1])
			continue
		totalMonths=totalMonths+1
		currentRevenue = int(record[1])
		totalrevenue = totalrevenue + currentRevenue
		
		#start revenue change analysis from 3rd recod
		currentRevenueChange = currentRevenue-prevRevenue
		totalRevenueChange = totalRevenueChange + currentRevenueChange

		if currentRevenue >= prevRevenue:
			increase = currentRevenue - prevRevenue
			if increase >= maxIncrease:
				maxIncrease=increase
				maxIncreaseMonth = record[0]
		else:
			decrease = prevRevenue - currentRevenue
			if decrease >= maxDecrease:
				maxDecrease=decrease
				maxDecreaseMonth = record[0]
		
		#initialize for comparison with next record
		prevRevenue= int(record[1])

#write output to file
#filename = 'Resources/' + 'analysis_budget_data_1.csv'
outputFilename = directoryName+'/analysis_'+dataFileName
file = open(outputFilename, 'w')


file.write('Financial Analysis'+'\n')
file.write('-------------------------------'+'\n')
file.write('Total months: ' + str(totalMonths)+'\n')
file.write('Total revenue : $' + str(totalrevenue)+'\n')
file.write('Average Revenue Change: $' + str(round(totalRevenueChange/totalMonths-1))+'\n')
file.write('Greatest Increase in Revenue: ' + maxIncreaseMonth + ' ($'+ str(maxIncrease) + ')'+'\n')
file.write('Greatest Decrease in revenue: ' + maxDecreaseMonth + ' ($-' + str(maxDecrease) + ')')

file.close()

#read the output file and print on screen

file = open(outputFilename,'r')
print(file.read())




