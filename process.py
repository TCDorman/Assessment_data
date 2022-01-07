log_file = open("um-server-01.txt")


def sales_reports(log_file): #this is creating a function called sales reports
    for line in log_file:   #this is a for loop going through the log_file
        line = line.rstrip() #this removes any trailing characters in each line
        day = line[0:3] #this targets the third indexed item on the line picking out where it specifies what day it was on
        if day == "Mon": #this is filtering for only things that happened on monday
            print(line) #this is printing the data


sales_reports(log_file) #this is running the function of sales_report on log_file
