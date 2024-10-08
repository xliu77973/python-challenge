# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "Resources/election_data.csv"  # Input file path
file_to_output = "analysis/election_analysis.txt"  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes = total_votes + 1
    
        # Get the candidate's name from the row
        candidate_name = row["Candidate"]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
        
            # append this candidate in the list
            candidate_options.append(candidate_name)

            # search for this candidate
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------------------\n"
    )
    print(election_results)

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:

        # Get the vote count and calculate the percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Update the winning candidate if this one has more votes
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}%({votes})\n"
        print(voter_output)

        txt_file.write (voter_output)
    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"--------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        F"--------------------------------------\n"
    )
    print(winning_candidate_summary)
    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)