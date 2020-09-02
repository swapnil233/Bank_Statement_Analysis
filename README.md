# Python_Amount_Spent_Checker
A python script that takes in a store/vendor's name and reads your bank statement (csv) to tell you how much you've spent (and gotten refunded) there.

### To use it:
1. Download your bank account activity from one period to another and save it as a .csv file in the folder with the python script
2. Rename your account activity .csv file to "dc_accountactivity.csv" if you want the python script to read it (or just change the variable name from within python).
3. Make sure the .csv file is in this format: date|vendor_name|debit|credit|balance and delete the top titles row if your .csv file has one.
4. Change the value of 'target' to whatever you want track, according to the rules given in the .py file (ie if I wanted to track all Tim Horton's spendings I'd just need to put target='tim' as it checks for the first word.

### Bonus: 
I do UberEats, DoorDash and SkipTheDishes as a side income. I've included the code to check how much you've earned with these.
