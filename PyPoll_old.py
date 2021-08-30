# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# import the datetime class from the datetime module.
import datetime
#Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
#Print the present time
print("the time right now is ", now)

#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path to the file.
file_to_load = os.path.join("Resources","election_results.csv") #for different paths -- os.path.join("foldername1","Foldername2","election_results.csv") 

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # To do: Read and analysis.
    #print(election_data)
    #Read the file object with the reader function
    #file_reader = csv.reader(election_data)

# 1. The total number of votes cast
total_voters = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in csv file
    for row in file_reader:
        #print(row)
        #2. Add to the total vote count:
        total_voters += 1
#3. Print the total votes
print(total_voters)
        

# Close the file.
election_data.close()

# #Using the open() function with the "w" mode we will write data to the file
# open(file_to_save, "w")

#Using with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #Write some data
    #outfile.write("Hello World")
    #txt_file.write("Hello world")
    txt_file.write("Counties in the Election\n_______________________________\nArapahoe\nDenver\nJefferson ")

#close the file
txt_file.close()