#Dependencies
import os
import csv

#Set Variables
data=[]
candidate={}
can_win=[]

#read CSV file
csvpath=os.path.join('resources','election_data.csv')
file=open(csvpath)
csvreader=csv.reader(file)
next(csvreader, None)

#cycle through data and append candidate list with candidate
for line in file:
    temp= line.split(',')
    # print(temp)
    data.append(temp)
    a=temp[2]
    # print(a)

    #create dictionary candidate
    if a in candidate :
        candidate[a]+=1
    else:
        candidate[a]=1     

print("Election Results")
print("----------------------------")


# The total number of votes cast
total_votes=len(data)
print("Total Votes:",total_votes)
print("----------------------------")

#percentage  and Total no of votes each candidate won
for x, y in candidate.items():
    can_win.append([x,y,float((y/total_votes)*100)])
max=can_win[0][2]
name=can_win[0][0]
print("Total no of votes each candidate won and percenatge:", can_win)
print("----------------------------")

#output to textfile
f = open('poll_output.txt','w+')
f.write("Election Results")
f.write('\n'+"----------------------------")
f.write('\n'+"Total Votes:"+str(total_votes))
f.write('\n'+"----------------------------")
for i in can_win:
    f.write('\n'+i[0]+":"+str(round(i[2],3))+"%"+" ("+str(i[1])+")")
    if(i[2] > max):    
       max = i[2]
       name=i[0]   
f.write('\n'+"Winner:"+" "+str(name)) 
f.write('\n'+"----------------------------")   
f.close()

#winner of the election based on popular vote
print("Winner:",name)
print("----------------------------")