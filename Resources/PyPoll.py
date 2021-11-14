#Dependencies 
import os
import csv
# Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Declaring empty canditate names and votes 
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Reading file object with reader function
    file_reader = csv.reader(election_data)
   
    # Read header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count by increments of 1
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]


        # If candidate name is not match existing list
        if candidate_name not in candidate_options:
           
            # Add to the list of candidates
            candidate_options.append(candidate_name)

            # initializing that candidate's vote
            candidate_votes[candidate_name] = 0
        # Adding a vote to the candidate's count while looping through rows
        candidate_votes[candidate_name] += 1
# PRINT CANDIDATE OPTIONS
print(candidate_options)

# PRINT TOTAL VOTES
print(total_votes)

    
# PRINT CANDIDATE VOTE (DICTIONARY)
print(candidate_votes)


# PErcentage of votes for each candidate looping through counts
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Getting vote count of candidate
    votes = candidate_votes[candidate_name]
    
    # % of votes
    vote_percentage = float(votes)/float(total_votes)*100

    # PRINT CANDIDATE NAME AND % VOTE
    ##print(f"{candidate_name}: received {vote_percentage:.1f} % of the vote.")

    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes 
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
     
    # PRINT WINNING CANDIDATE'S NAME, VOTE COUNT AND PERCENTAGE OF VOTES
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Winnning Candidate Summary
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)


