#import dependencies
import os
import csv

#Variable that holds the path to the current script/Import a text file filled with a paragraph of your choosing.
#Chose paragraph_1.txt
Script_Location = os.path.dirname(os.path.realpath(__file__)) + "/"
Text_File = Script_Location + "/raw_data/paragraph_1.txt"

#Initializations
word_count = 0
sentence_count = 0
avg_letter_count = 0
avg_sentence_length = 0

#Open text file
with open(Text_File, "r") as txtfile:

#Assess the passage for each of the following:    
    for line in txtfile:

        #Approximate word count:
        words = line.split()
        word_count += + len(words)

        #Approximate sentence count:
        sentence_count += line.count('.') + line.count('!') + line.count('?')

        #Approximate/average letter count (per word):
        avg_letter_count +=  (+ len(line)- line.count(" "))/ word_count

        #Average sentence length (in words):
        avg_sentence_length = word_count/sentence_count

#Print Results
print("Paragraph Analysis")
print("-------------------------")
print("Approximate Word Count: {}".format(word_count))
print("Approximate Sentence Count: {}".format(sentence_count))
print("Average Letter Count: {:.1f}".format(avg_letter_count))
print("Average Sentence Length: {:.1f}".format(avg_sentence_length))

#Print results to .txtfile
outpath = os.path.join("paragraph_analysis.txt")

with open(outpath, "w", newline="") as datafile:
    writer = csv.writer(datafile)   
    datafile.write("Paragraph Analysis")
    datafile.write("\n")
    datafile.write("-------------------------")
    datafile.write("\n")
    datafile.write("Approximate Word Count: {}".format(word_count))
    datafile.write("\n")
    datafile.write("Approximate Sentence Count: {}".format(sentence_count))
    datafile.write("\n")
    datafile.write("Average Letter Count: {:.1f}".format(avg_letter_count))
    datafile.write("\n")
    datafile.write("Average Sentence Length: {:.1f}".format(avg_sentence_length))
    datafile.write("\n")

