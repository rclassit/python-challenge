# python-challenge

Hello I've put together the steps that I've taken in order to complete both the PyBank and PyPoll homework for the 2nd Homework challenge for the UNC data bootcamp.  I'll go through the steps of how I did the Pybank Challenge:

    Pybank:
    1st step was to import the csv in order to red the csv files and to create the file paths across the operating systems:
    import os
    import csv
    
   Utilized correct CSV path to pull csv from the Resources folder
   
    csvpath = os.path.join("Resources","budget_data.csv")
    
   Next was open and reading the CSV as well as defining some variables to be used in my analysis: 
    
    with open(csvpath, newline = "") as csvfile:
      csvread = csv.reader(csvfile, delimiter = ",") 
      #Define the header row 
      header = next(csvread) 
      #Define variables 
      dates = []
      Profit = []
      Change_Profit[]
      
   Now we want to append our relevant data with a loop in the csvread:
      
      for row in csvread:
        #Value iteration
        dates.append(row[0])
        Profit.append(int(row[1]))
   loop for profit true differential 
      
      for i in range(len(Profit)-1):
        Change_Profit.append(Profit[i+1]-Profit[i])
        
   Now that we've found the true profit change differential with our loops, we can define variables with max and mins functions:
    
    maxProfitMonth = max(Change_Profit)
    minProfitMonth = min(Change_Profit) 
    
   Using index: 
    
    Max = Change_Profit.index(maxProfitMonth)+1
    Min = Change_Profit.index(minProfitMonth)+1
    
  This will search the list and retrieve our max/min P/L between months
    
   Now we can begin printing our analysis summary: 
    
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {len(dates)}")
    print(f"Total Revenue : ${sum(Profit)}")
    print(f"Average Change: ${round(sum(Change_Profit)/len(Change_Profit),2)}") 
    print(f"Greatest Increase in Profits: {dates[Max]} (${(str(maxProfitMonth))})")
    print(f"Greatest Decrease in Profits: {dates[Min]} (${(str(minProfitMonth))})")
    
  Note the average change is simply a formula of the sum of P/L monthly differentials divided by # of changes (months) 
    
  and this is the Write up for our text output direct to the Analysis folder:
    
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
       
PyPoll 
For the Pypoll Challenge I imported dependencies and created a single candidates dictionary: 
        
        #import dependencies
        import os
        import csv

        #Variables
        candidates = {}

        #CSV Read
        election_data_csv = os.path.join("Resources", "election_data.csv")
        with open(election_data_csv, 'r') as csvfile:

            #Header Info
            csvread = csv.reader(csvfile, delimiter = ',')
            header = next(csvread)
Looped through the CSVread in order to list candidate vote values:
            
            for row in csvread:
                if row[2] in candidates.keys():
                    candidates[row[2]]+=1
                else:
                    candidates[row[2]] = 1
Can list values with candidates variable
               
                total = candidates.values()
Sum total votes
                
                SumVotes = sum(total)
  
                candidate_list = candidates.keys(
Determining Votes per Candidate
                    
                candidate_votes = [f'{(x/SumVotes)*100:.3f}%' for x in candidates.values()]
Determining Winner
                    
                Win = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
                Win
 
This is our Print Info: 
 
     print ("Election Results")

    print ("-----------------------------")

    print(f'Total Votes: {int(SumVotes)}')

    print ("-----------------------------")
loop to print index 

    i = 0 
    for candidate, vote in candidates.items():
        print(f'{candidate}: {candidate_votes[i]} ({vote})')
        i+=1

    print ("------------------------------")

    print(f"Winner: {Win}")
    
Lastly, our Output to Analysis Folder: 

Output to analysis folder 

    output = os.path.join("Analysis",'outputAnalyis.txt')
    with open(output,"w") as new:
              new.write("Election Results")
              new.write("\n")
              new.write("------------------")
              new.write("\n")
              new.write(f"Total Votes:" + str(SumVotes))
              new.write("\n----------------")
              i=0
              for candidate, vote in candidates.items():
                new.write(f"\n" +str(candidate) +" : " + str(candidate_votes[i]) + "% ("+ str(vote) + ")")
                i+=1
              new.write("\n----------------")
              new.write("\n Winner: "+ str(Win))    
              
 Analysis: Out of 3,521,001 total votes, Khan was the winner by (63%) - 2,218,231 votes.  

        Election Results
        ------------------
        Total Votes:3521001
        ----------------
        Khan : 63.000%% (2218231)
        Correy : 20.000%% (704200)
        Li : 14.000%% (492940)
        O'Tooley : 3.000%% (105630)
        ----------------
         Winner: Khan
