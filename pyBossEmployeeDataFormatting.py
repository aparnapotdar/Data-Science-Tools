
# This program formats employee information (name, SSN , DOB, State)
# input on prompt - directory and data file name 
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# output - file with formatted data. Filename prefix "formatted_"
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL

# we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv

#prompt for directory name and data file name
directoryName=input(print("What's the directory name where data file resides? "))
dataFileName=input(print("What's the data file name? "))
outputFileName = 'formatted_'+dataFileName

#specify the file to read from
csvpath = os.path.join(directoryName,dataFileName)
# Specify the file to write to
output_path = os.path.join(directoryName,outputFileName)

#dictionary for state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open(csvpath, newline='') as csvfileIn:

	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfileIn, delimiter=',')


	# Open the file using "write" mode. Specify the variable to hold the contents
	with open(output_path, 'w', newline='') as csvfileOut:

		# Initialize csv.writer
		csvwriter = csv.writer(csvfileOut, delimiter=',')
    
		firstLine=True
		for empRecord in csvreader:
			#skip first header row from formatting excercise  
			if firstLine == True:
				firstLine = False
    			# Write the first row (column headers)
				csvwriter.writerow(['Emp Id', 'First Name','Last Name', 'DOB','SSN','State'])
				continue

			empId = empRecord[0]

			#split full name
			firstName, lastName = empRecord[1].split()

			#split DOB
			yyyy, mm, dd = empRecord[2].split('-')
			formattedDOB=str(mm) + '/' + str(dd)+ '/'+str(yyyy)

			#split SSN
			beg,middle,last4 = empRecord[3].split('-')
			formattedSSN = '***-***-'+last4

			#use state dictionry to get state abbreviation
			abbrevState = us_state_abbrev[empRecord[4]]

			csvwriter.writerow([empId, firstName,lastName, formattedDOB,formattedSSN,abbrevState])