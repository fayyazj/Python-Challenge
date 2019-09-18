#import needs
import csv

#Initializing Variables
Number_Of_Months = 0
Net_Total = 0
Total_Monthly_Change = 0
Greatest_Increase = 0
Greatest_Decrease = 0

#read in csv file
File_Name = "/Users/celiakresser/Documents/GitHub/Python-Challenge/PyBank/Budget_Data.csv"

#create object that will maintain the data in Budget_Data
with open(File_Name, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #Skip first line or header in row
    next(csvreader)

    #parse csv for:
    for row in csvreader:
        #The total number of months included in the dataset
        Number_Of_Months = Number_Of_Months + 1  #Alternative short hand is Number_of_Months+=1
        
        #The net total amount of "Profit/Losses" over the entire period
        Monthly_Profit = int(row[1])
        Net_Total = Net_Total + Monthly_Profit

        #The average of the changes in "Profit/Losses" over the entire period
        if Number_Of_Months == 1:
            Prev_Profit = Monthly_Profit
        else:
            Monthly_Change = Monthly_Profit - Prev_Profit
            Prev_Profit = Monthly_Profit
            Total_Monthly_Change = Total_Monthly_Change + Monthly_Change
            
            #The greatest increase in profits (date and amount) over the entire period
            if Monthly_Change > Greatest_Increase:
                Greatest_Increase = Monthly_Change
                Greatest_Increase_Date = row[0]
            #The greatest decrease in losses (date and amount) over the entire period
            elif Monthly_Change < Greatest_Decrease:
                Greatest_Decrease = Monthly_Change
                Greatest_Decrease_Date = row[0]

#Defining Average Change at the end of the for loop
Average_Change = round(Total_Monthly_Change/(Number_Of_Months - 1), 2)

#Output to terminal and text file
Financial_Analysis = "Financial Analysis\n--------------------------------------------------\nTotal Months: {}\nTotal: ${}\nAverage Change: ${}\nGreatest Increase In Profits: {} (${})\nGreatest Decrease In Profits: {} (${})".format(Number_Of_Months, Net_Total, Average_Change,Greatest_Increase_Date, Greatest_Increase, Greatest_Decrease_Date, Greatest_Decrease)
print(Financial_Analysis)

File = "/Users/celiakresser/Documents/GitHub/Python-Challenge/PyBank/Financial Analysis.txt"
Output_Object = open(File, 'w')
Output_Object.write(Financial_Analysis)
Output_Object.close