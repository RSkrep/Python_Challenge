import csv
import os

#Create pathway to data 
csv_election_path = r"PyPoll\Resources\election_data.csv"
output_file_path = "election_results.txt"

# Create Variables
total_votes = 0
candidates_set = set()
candidates_counts = {}

with open(csv_election_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    # Skip the header row
    header_row = next(csvreader, None)
    # Find Total votes and votes for each Candidate name 
    for row in csvreader:
        total_votes += 1 
        candidate_name = str(row[2])

        candidates_set.add(candidate_name)

        candidates_counts[candidate_name] = candidates_counts.get(candidate_name, 0) + 1

candidates_percentages = {candidate: (count / total_votes) * 100 for candidate, count in candidates_counts.items()}

# Announce the winner of election
winner = max(candidates_counts, key=candidates_counts.get)

# Print to the terminal
print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
for candidate, percentage in candidates_percentages.items():
    print(f"{candidate}: {percentage:.2f}% ({candidates_counts[candidate]} votes)")
print("-------------------------")
print("Winner:", winner)
print("-------------------------")

# Export to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, percentage in candidates_percentages.items():
        output_file.write(f"{candidate}: {percentage:.2f}% ({candidates_counts[candidate]} votes)\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print(f"Results have been exported to {output_file_path}")

