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
    #Candidate Dictionary Keys
    for row in csvread:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1
    
        total = candidates.values()
        SumVotes = sum(total)

        candidate_list = candidates.keys()
        #Determining Votes per Candidate
        candidate_votes = [f'{(x/SumVotes)*100:.3f}%' for x in candidates.values()]
        #determining Winner
        Win = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        Win

#Print Stuff
print ("Election Results")

print ("-----------------------------")

print(f'Total Votes: {int(SumVotes)}')

print ("-----------------------------")
#loop to print index
i = 0 
for candidate, vote in candidates.items():
    print(f'{candidate}: {candidate_votes[i]} ({vote})')
    i+=1

print ("------------------------------")

print(f"Winner: {Win}")

#Output to analysis folder 
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