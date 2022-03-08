# Kenneth Linehan, 
# My program reads in a text file and counts how many E's are in the text file


#Source I used to read in data - https://pythonexamples.org/python-count-number-of-characters-in-text-file/

#Moby Dick Txt File found here - https://gist.github.com/StevenClontz/4445774

#open file in read mode
file = open("mobydick.txt", "r")

#read the content of file
data = file.read()

#Source I used to help count data - https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

occurrences = data.count("e")

#Checks how many occurrences of e appear in document

print('Number of occurrences of the letter e is :', occurrences)

#Prints amount of e's that appear in document