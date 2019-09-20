#Import Dependencies
import csv
import os

#Variable that holds the path to the current script
Script_Location = os.path.dirname(os.path.realpath(__file__)) + "/"
Out_File = Script_Location + "PyBoss_Employee_Data.csv"
Output_Object = open(Out_File, mode='w', newline='')
Output_Object = csv.writer(Output_Object, delimiter=',')

#Create Dictionary
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

#Functions Declarations
def CsvOpen(filename, *SkipHeader):
    obj = open(filename, newline='', encoding='UTF-8')
    CSVobj = csv.reader(obj, delimiter=',')
    
    if SkipHeader == "SkipHeader":
        next(CSVobj)
    return list(CSVobj)

#Open CSV
File_Name = Script_Location + "employee_data.csv"
EmployeeData = CsvOpen(File_Name)

#The Name column should be split into separate First Name and Last Name columns.
EmployeeData[0] = ["Emp ID","First Name","Last Name","DOB","SSN","State"]

for row in EmployeeData:
	if row == EmployeeData[0]:
		pass
	else:
		fullname = row[1].split(" ")
		firstname = fullname[0]
		lastname = fullname[1]

		#The DOB data should be re-written into MM/DD/YYYY format.
		Date = row[2].split("-")
		Year = Date[0]
		Month = Date[1]
		Day = Date[2]
		NewDate = Month + "/" + Day + "/" + Year

		#The SSN data should be re-written such that the first five numbers are hidden from view.
		SSN = row[3].split("-")
		LastFour = SSN[2]
		New_SSN = "***-**-" + LastFour

		#The State data should be re-written as simple two-letter abbreviations.
		state = row[4]
		New_State = us_state_abbrev[state]

		row = [row[0], firstname, lastname, NewDate, New_SSN, New_State]

	#Output to CSV
	print(row)
	Output_Object.writerow(row)


		
