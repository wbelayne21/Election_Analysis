#Dependencies 
import os
import csv
# Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Reading file object with reader function
    file_reader = csv.reader(election_data)
    # Read and print header 
    headers = next(file_reader)
    print(headers)



