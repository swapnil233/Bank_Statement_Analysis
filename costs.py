import csv

debit_card_account_activity = open("dc_accountactivity.csv", "r")
dc_reader = csv.reader(debit_card_account_activity)

total = 0
refunded = 0

# target is the first word before a space in row 2 
# (ie tim for TIM HORTONS). Also has to be lowercase.
target = 'steamgames'

for row in dc_reader:
    keyword = row[1].split()
    if keyword[0].lower()==target:
        if row[2]=='':
            print("Refunded ", float(row[3]), "on", row[0])
            refunded += float(row[3])
        else:
            print("Purchased ", float(row[2]), "on", row[0])
            total += float(row[2]) 

print("\n")        
print("Total Purchased: ", round(total, 2))
print("Total Refunded: ", round(refunded, 2))
print("Net: ", round(total-refunded, 2))

# Uber Eats Earnings
"""
for row in dc_reader:
    if row[1] == "Uber BV - Canad  MSP":
        print('Made:', row[3], "on: ", row[0])
        total += float(row[3])
        
print("Total Made: ", total)
"""

# DoorDash Earnings
'''
for row in dc_reader:
    if row[1] == "DoorDash, Inc.   MSP":
        print('Made:', row[3], "on: ", row[0])
        total += float(row[3])
        
print("Total Made: ", total)
'''

# Skip The Dishes Earnings
'''
for row in dc_reader:
    if row[1] == "SKIPTHEDISHES    MSP":
        print('Made:', row[3], "on: ", row[0])
        total += float(row[3])
        
print("Total Made: ", total)
'''