# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add our dependencies
import csv
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Assign a variable for the file to load and the path to the file.
file_to_load = os.path.join("Resources","election_results.csv") #for different paths -- os.path.join("foldername1","Foldername2","election_results.csv") 

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#The total number of votes cast
total_voters = 0

#candidate options - list
candidate_options = []

#candidate votes - dictionary
candidate_votes ={}

# Winning Candidate and Winning Count Tracker
winning_count =0
winning_percentage =0 
winning_candidate = ""

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)

    #Print each row in csv file
    for row in file_reader:
        #Add to the total vote count:
        total_voters += 1

        #Print the candidate name from each row
        candidate_name =row[2]
        
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
              candidate_options.append(candidate_name)
            # Begin tracing the candidates vote count 
              candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1


#Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_voters:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percnetage of votes
        vote_percentage = float(votes)/float(total_voters) *100
        #Print name and percentage
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)

        #save the candidate results to our text file
        txt_file.write(candidate_results)
    
        # Determine winning vote count and candidate
        # to check if the first vote count is great than zero
        if (votes > winning_count) and (vote_percentage>winning_percentage):
            #If true set winning_count and winning_percentage as votes and vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #select winning candiate
            winning_candidate = candidate_name

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate summary to text file
    txt_file.write(winning_candidate_summary)

    # Close the file.
    election_data.close()

#close the file
txt_file.close()
