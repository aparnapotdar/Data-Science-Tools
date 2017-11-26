
# This program analyzes paragraphs in input files
# input on prompt - directory and data file name 
# output - file with formatted data. Filename prefix "analysis_"

# import reg exp
import re


#prompt for directory name and data file name
directoryName=input(print("What's the directory name where data file resides? "))
dataFileName=input(print("What's the data file name? "))
outputFileName = 'analysis_'+dataFileName



inputFileName = directoryName+'/'+dataFileName
inFile= open(inputFileName, 'r')
paragraph = inFile.read()
#print(paragraph)

words = paragraph.split()
#sentences = paragraph.split(('.','!','?'))

sentences = re.split('([.!?])', paragraph)

#print ("Approximate Word count: " + str(len(words)))

#print ("Approximate Sentence count: " + str(len(sentences)))

wordLength=0
for word in words:
	#print(word + " "+ str(len(word)))
	wordLength = wordLength + len(word)

avgWordLength=wordLength/len(words)

#print ("avg letter count in words: " + str(round(avgWordLength,2)))

wordsInSentence=0
for sentence in sentences:
	wordsInSentence = wordsInSentence + len(sentence.split())
	wordLength = wordLength + len(word)

avgSentenceLength=wordsInSentence/len(sentences)


#print ("avg word count in sentences: " + str(round(avgSentenceLength,2)))


outputFilename = directoryName+'/analysis_'+dataFileName
outfile = open(outputFilename, 'w')


outfile.write('Paragraph Analysis'+'\n')
outfile.write('--------------------------------'+'\n')
outfile.write('Approximate Word count: ' + str(len(words))+ '\n')
outfile.write('Approximate Sentence count: ' + str(len(sentences))+ '\n')
outfile.write('Approximate letter count (per word): ' + str(round(avgWordLength,2))+ '\n')
outfile.write('Average sentence length (in words): ' + str(round(avgSentenceLength,2)) + '\n')

outfile.close()

#read the output file and print on screen

file = open(outputFilename,'r')
print(file.read())