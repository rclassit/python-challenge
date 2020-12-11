#  create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources","budget_data.csv")



#Open and Read CSV
with open(csvpath, newline = "") as csvfile:
     csvread = csv.reader(csvfile, delimiter = ",")
     
     #header row
     header = next(csvread)

     #Variables 
     dates = []
     Profit = []
     Change_Profit = []

   
     #Append Data
     for row in csvread:
          #Value iteration 
          dates.append(row[0])
          Profit.append(int(row[1]))
     for i in range(len(Profit)-1):
          Change_Profit.append(Profit[i+1]-Profit[i])
          
#variables for max and min for list 
maxProfitMonth = max(Change_Profit)
minProfitMonth = min(Change_Profit)

Max = Change_Profit.index(maxProfitMonth)+1
Min = Change_Profit.index(minProfitMonth)+1


#Print Stuff
print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(dates)}")
print(f"Total Revenue : ${sum(Profit)}")
print(f"Average Change: ${round(sum(Change_Profit)/len(Change_Profit),2)}")
print(f"Greatest Increase in Profits: {dates[Max]} (${(str(maxProfitMonth))})")
print(f"Greatest Decrease in Profits: {dates[Min]} (${(str(minProfitMonth))})")

#Write up for output

output = os.path.join("Analysis",'outputAnalyis.txt')
with open(output,"w") as new:
          new.write("Financial Analysis")
          new.write("\n")
          new.write("------------------")
          new.write("\n")
          new.write(f"Total Months: {len(dates)}")
          new.write("\n")
          new.write(f"Total Revenue : ${sum(Profit)}")
          new.write("\n")
          new.write(f"Average Change: ${round(sum(Change_Profit)/len(Change_Profit),2)}")
          new.write("\n")
          new.write(f"Greatest Increase in Profits: {dates[Max]} (${(str(maxProfitMonth))})")
          new.write("\n")
          new.write(f"Greatest Decrease in Profits: {dates[Min]} (${(str(minProfitMonth))})")
