#Dependencies
import os
import csv

#set variables
date=[]
loss_profit=[]
total_amount=0

#read CSV file
csvpath=os.path.join('resources','budget_data.csv')
file=open(csvpath)
csvreader=csv.reader(file)
next(csvreader, None)

#for loop through dataset
for row in file:
    #print(row)
    temp= row.split(',')
    date.append(temp[0])
    loss_profit.append(temp[1])
    total_amount+=int(temp[1])

      
print("Financial Analysis")
print("----------------------------")

# The total number of months included in the dataset
total_months=len(date)
print("Total Months:",total_months)

# The net total amount of "Profit/Losses" over the entire period
print("Total:$",total_amount)


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
avg_money=round(total_amount/total_months, 2)
print("Average  Change:$",avg_money)


# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

max_pos = loss_profit.index(max(loss_profit))
min_pos = loss_profit.index(min(loss_profit))
print("Greatest Increase in Profits:",date[max_pos],loss_profit[max_pos])
print("Greatest Decrease in Losses:",date[min_pos],loss_profit[min_pos])
print("----------------------------")


# create file Output file and print statments

f = open('bank_output.txt','w+')
f.write("Financial Analysis")
f.write('\n'+"----------------------------")
f.write('\n'+"Total Months:"+str(total_months))
f.write('\n'+"Total:$"+str(total_amount))
f.write('\n'+"Average  Change:$"+str(avg_money))
f.write('\n'+"Greatest Increase in Profits:"+str(date[max_pos])+" "+"("+str(loss_profit[max_pos])+")")
f.write('\n'+"Greatest Decrease in Losses:"+str(date[min_pos])+" "+"("+str(loss_profit[min_pos])+")")
f.write('\n'+"----------------------------")
f.close()
