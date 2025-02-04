#Objective:
#You've been hired by a company to shuffle their sales records for a certain privacy task.
#They want to randomize the order of rows in their CSV files every day at a specific time.
#Additionally, they want you to make backups of the original files in a separate directory before they are randomized.

#Tasks
# 1. Use the 'csv' library to read from and write to the sales data files.
# 2. Use the 'random' library to shuffle the rows in the CSV (excluding the header)
# 3. Use the 'time' library to wait and run the randomizing operation every day at a specific time.
# 4. Use the 'shutil' library to copy the original files to a backup directory before randomizing them.


#Step 1 - Read the sales data from a CSV file using the 'csv' library
import csv
# open the file in read mode
with open('sales_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    # iterate through rows in the CSV
    for row in csv_reader:
        print(row) #each row is a set of values



#Step 2 - Use 'shutil' to copy this original file to a backup directory
import os
import shutil
#Define file paths
original_file = 'sales_data.csv'
backup_dir = 'backup_directory/'
backup_file = os.path.join(backup_dir, 'sales_data_backup.csv')

# Ensure the backup directory exists
os.makedirs(backup_dir, exist_ok=True)

# Copy the original file to the backup directory
shutil.copy(original_file, backup_file)
print(f"File backed up to {backup_file}")



#Step 3 - Shuffle the rows of sales data using the 'random.shuffle()' function
import random
with open(original_file, mode='r') as infile:
    reader = list(csv.reader(infile))  # Read all rows into a list

# Shuffle the rows (excluding header if present)
header = reader[0]  # Assume first row is header
data = reader[1:]

random.shuffle(data)

# Combine header with randomized data
randomized_data = [header] + data



#Step 4 - Write the shuffled data back to the original CSV file
with open('sales_data.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(randomized_data)

print("CSV file has been randomized and saved as 'sales_data.csv'")



#Step 5 - Use 'time.sleep() to wait for a certain duration
#(e.g., 10 seconds for demonstration purpose) before repeating
import datetime
with open(original_file, mode='r', newline='', encoding='utf-8') as file:
    step5_reader = csv.reader(file)
    step5_header = next(step5_reader)
    rows = list(step5_reader)

random.shuffle(rows)

with open(original_file, mode='w', newline='', encoding='utf-8') as file:
    step5_writer = csv.writer(file)
    step5_writer.writerow(step5_header)
    step5_writer.writerows(rows)

print(f"CSV randomized at {datetime.datetime.now()}")