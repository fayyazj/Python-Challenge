#import dependencies
import csv

#Initializing Variables
Number_Of_Votes = 0
Winner_Votes = 0
Candidate_List = []
Candidate_Data = []

File_Name = "/Users/celiakresser/Documents/GitHub/Python-Challenge/PyPoll/Election_Data.csv"
#File_Name = "Election_Data.csv"

#Read in the csv file
csvfile = open(File_Name, newline='', encoding='UTF-8')
csvreader = csv.reader(csvfile, delimiter=',')

#Skip Header Row
next(csvreader)

#Parse the data for:
for row in csvreader:
    #The total number of votes cast
    Number_Of_Votes = Number_Of_Votes + 1

    #A complete list of candidates who received votes
    Candidate_Name = row[2]
    Candidate_Dictionary = {"Name":row[2],"Vote":0}

    if Candidate_Name not in Candidate_List:
        Candidate_List.append(Candidate_Name)
        Candidate_Data.append(Candidate_Dictionary)

    #The total number of votes each candidate won
    for Candidate_Dictionary in Candidate_Data:
        if Candidate_Dictionary["Name"] == row[2]:
            Candidate_Dictionary["Vote"] = Candidate_Dictionary["Vote"] + 1

Results = "Election Results\n-------------------------\nTotal Votes: {}\n-------------------------\n".format(Number_Of_Votes)

#The percentage of votes each candidate won
for Candidate_Dictionary in Candidate_Data:
    #The winner of the election based on popular vote.
    if Candidate_Dictionary["Vote"] > Winner_Votes:
        Winner_Votes = Candidate_Dictionary["Vote"]
        Winner = Candidate_Dictionary["Name"]
    
    Percent = Candidate_Dictionary["Vote"]/Number_Of_Votes * 100

    #Build Output
    Results = Results + "{}: {:.3f}% ({})\n".format(Candidate_Dictionary["Name"],float(round(Percent, 3)),Candidate_Dictionary['Vote'])

Results = Results + "---------------------------\nWinner = {}\n---------------------------".format(Winner)

#Ouput to Terminal
print(Results)

#Output to Text File
File = "/Users/celiakresser/Documents/GitHub/Python-Challenge/PyPoll/Election Results.txt"
Output_Object = open(File, "w")
Output_Object.write(Results)
Output_Object.close