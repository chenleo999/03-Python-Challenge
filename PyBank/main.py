# import modules
import os, csv

# get file path
f1_path = os.path.join(".", "Resources", "budget_data.csv")
f2_path = os.path.join(".", "analysis", "result.csv")

# open/read source data
with open(f1_path, "r") as f1:
    f1_content = csv.reader(f1)

    #skip header
    next(f1_content, None)

    # set variables
    last_value = "n/a"
    total_value = 0
    min_change = 0
    max_change = 0
    row_count =  0
    sum_change = 0

    # calculate row count, total, change, max/min changes/date
    for row in f1_content:
        row_count += 1
        total_value += int(row[1])
        row_change = 0 if last_value == "n/a" else int(row[1]) - int(last_value)
        sum_change += row_change
        last_value = row[1]

        if row_change > max_change:
            max_change = row_change
            max_date = str(row[0])
        elif row_change < min_change:
            min_change = row_change
            min_date = str(row[0])
        else:
            pass
        
# open/write result csv
with open(f2_path, "w", newline = "") as f2:
    f2_content = csv.writer(f2)
    f2_content.writerow(["Financial Analysis"])
    f2_content.writerow([f"{'-'*50}"])
    f2_content.writerow([f"Total Months: {row_count}"])
    f2_content.writerow([f"Total: ${total_value}"])
    f2_content.writerow([f"Average Change: ${sum_change/(row_count-1):.2f}"])
    f2_content.writerow([f"Greatest Increase in Profits: {max_date} (${max_change})"])
    f2_content.writerow([f"Greatest Decrease in Profits: {min_date} (${min_change})"])

#print results to terminal
with open(f2_path, "r") as f2:
    f2_content = csv.reader(f2)
    for row in f2_content:
        print(row)
        


