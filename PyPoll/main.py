# import modules
import os, csv

# get file path
f1_path = os.path.join(".", "Resources", "election_data.csv")
f2_path = os.path.join(".", "analysis", "result.csv")

# open/read source data
with open(f1_path, "r") as f1:
    f1_content = csv.reader(f1)

    #skip header
    next(f1_content, None)

    # set variables
    tot_vote = 0
    candidates = []
    vote_count = []
    vote_percent = []

    # calculate variables
    for row in f1_content:
        # total number of votes cast 
        tot_vote += 1

        # new candidate, add into list, vote = 1
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count.append(1)

        # existing candidate, find index, vote + 1
        else:
            index = candidates.index(row[2])
            vote_count[index] += 1

# find winner
winner_index = vote_count.index(max(vote_count))
winner = candidates[winner_index]

# calculate vote % for each candidate
vote_percent = ["{:.3f}".format(v * 100 / tot_vote) + "%" for v in vote_count]

# combine candidates and vote count
candidate_vote = zip(candidates, vote_percent, vote_count)

# open/write result csv
with open(f2_path, "w", newline = '') as f2:
    f2_content = csv.writer(f2)
    # header
    f2_content.writerow(["Election Results"])
    f2_content.writerow([f"{'-'*50}"])

    #total votes
    f2_content.writerow([f"Total Votes: {tot_vote}"])
    f2_content.writerow([f"{'-'*50}"])

    # candidates: vote % (vote count)
    for item in candidate_vote:
        f2_content.writerow([f"{item[0]}: {item[1]} ({item[2]})"])

    # winner, footer
    f2_content.writerow([f"{'-'*50}"])
    f2_content.writerow([f"Winner: {winner}"])
    f2_content.writerow([f"{'-'*50}"])

# print results to terminal
with open(f2_path, "r") as f2:
    f2_content = csv.reader(f2)
    for row in f2_content:
        print(row)