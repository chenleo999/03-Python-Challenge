# import modules
import os, csv

# get source csv path
f1_path = os.path.join(".", "Resources", "budget_data.csv")
f2_path = os.path.join(".", "analysis", "analysis.csv")
f3_path = os.path.join(".", "analysis", "result.csv")

# open/read source csv
with open(f1_path, "r") as f1:
    f1_content = csv.reader(f1)

    #skip header
    next(f1_content, None)

    #set variables
    total_pl = 0
    row_count = 0
    last_value = "n/a"
    max_change = 0
    min_change = 0
  

    # calculate monthly change, sum changes
    for row in f1_content:
        total_pl += int(row[1])
        row_count += 1
        row_change = int(row[1]) - int(last_value) if last_value != "n/a" else int(row[1])
        if row_change > max_change:
            max_change = row_change
            max_date = str(row[0])
        last_value = row[1]




        print(f"row_change {row_change}")
        print(f"max_change {max_change} max_date {max_date}")
        print(row_change > max_change)
        print(row[0])
        print(max_date)