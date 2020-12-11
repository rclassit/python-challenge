# python-challenge

# Hello I've put together the steps that I've taken in order to complete both the PyBank and PyPoll homework for the 2nd Homework challenge for the UNC data bootcamp.  I'll go through the steps of how I did the Pybank Challenge:

    Pybank:
    1st step was to import the csv in order to red the csv files and to create the file paths across the operating systems:
    import os
    import csv
    
   # Utilized correct CSV path to pull csv from the Resources folder
    csvpath = os.path.join("Resources","budget_data.csv")
    
   # Next was open and reading the CSV as well as defining some variables to be used in my analysis: 
    with open(csvpath, newline = "") as csvfile:
      csvread = csv.reader(csvfile, delimiter = ",") 
      #Define the header row 
      header = next(csvread) 
      #Define variables 
      dates = []
      Profit = []
      Change_Profit[]
      
   #  Now we want to append our relevant data with a loop in the csvread:
      for row in csvread:
        #Value iteration
        dates.append(row[0])
        Profit.append(int(row[1]))
   #  loop for profit true differential 
      for i in range(len(Profit)-1):
        Change_Profit.append(Profit[i+1]-Profit[i])
        
   # Now that we've found the true profit change differential with our loops, we can define variables with max and mins functions:
    maxProfitMonth = max(Change_Profit)
    minProfitMonth = min(Change_Profit) 
    
   # Using index: 
    Max = Change_Profit.index(maxProfitMonth)+1
    Min = Change_Profit.index(minProfitMonth)+1
    
  #  This will search the list and retrieve our max/min P/L between months
    
   # Now we can begin printing our analysis summary: 
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {len(dates)}")
    print(f"Total Revenue : ${sum(Profit)}")
    print(f"Average Change: ${round(sum(Change_Profit)/len(Change_Profit),2)}") 
    print(f"Greatest Increase in Profits: {dates[Max]} (${(str(maxProfitMonth))})")
    print(f"Greatest Decrease in Profits: {dates[Min]} (${(str(minProfitMonth))})")
    
  #  Note the average change is simply a formula of the sum of P/L monthly differentials divided by # of changes (months) 
    
  #   and this is the Write up for our text output direct to the Analysis folder:
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

Analysis: 
Based on 86 months of P/L data, Total revenue was $38,382,578.00.  Average change was $-2,315.12 M-M.  The Greatest increase in profits M-M occurred in Feb 2012 at $1,926,159.  Greatest Decrease in profits M-M occurred Sep 2013 at $-2,196,167:

Financial Analysis
------------------
Total Months: 86
Total Revenue : $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
