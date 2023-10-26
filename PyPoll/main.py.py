import os
import csv

# Set path for file
#csvpath = os.path.join("\\Resources\budget_data.csv") 
csvpath = os.path.join("Resources", "election_data.csv")
csvpath_output = "election_results.txt"

# Open the CSV using the UTF-8 encoding
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

      # Skip the header row
    next(csvreader, None)
    
    # Initializing the variables
    Total_Votes = 0
    Candidates_votes_dictionary = {}
    Winner = ""
    Votes_Winner = 0

    # Looping through to get the total number of votes
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        # To get the name of the candidate
        candidate_name = row[2]

        # How many times each candidate is in the list
        # If the candidate is not in the list
        if candidate_name not in Candidates_votes_dictionary:
            # If the candidate does not exist, add one to the count
            Candidates_votes_dictionary[candidate_name] = 0

        # Adding the vote
        Candidates_votes_dictionary[candidate_name] += 1

    # To get the amount of votes, loop through the dictionary and count the votes for each candidate
    for candidate, votes in Candidates_votes_dictionary.items():
        percentage = (votes / Total_Votes) * 100
        print(f'{candidate}: {percentage:.3f}% ({votes})')

    # Output summary for CSV

    # Open the output file in write mode and write the results
    with open(csvpath_output, 'w') as txt_file:
        Output = (
            f"Election Results\n"
            f"------------------\n"
            f"Total Votes: {Total_Votes}\n"
            f"------------------\n"
        )

        # Save the final vote count to the text file
        txt_file.write(Output)

        # Getting the winner by looping through the counts
        for candidate, votes in Candidates_votes_dictionary.items():
            vote_percentage = (votes / Total_Votes) * 100

            # Winner and amount of votes
            if votes > Votes_Winner:
                Votes_Winner = votes
                Winner = candidate

            # Printing the amount of votes and percentage
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output)

            # Save each candidate's vote count and percentage to the text file
            txt_file.write(voter_output)

        # Print the winner in the terminal
        winner_candidate_summary = (
            f"------------------\n"
            f"Winner: {Winner}\n"
            f"------------------\n"
        )

        print(winner_candidate_summary)

        # Save the winner's name to the text file
        txt_file.write(winner_candidate_summary)
