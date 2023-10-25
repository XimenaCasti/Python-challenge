import os
import csv

# Establece la ruta para el archivo CSV
csvpath = os.path.join("C:/Users/ximen/OneDrive/Escritorio/election_datax.csv")

# Abre el CSV usando la codificación UTF-8
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print("Election Results")
    print("______________________")

    # Salta la fila de encabezado
    next(csvreader, None)

    # Inicializa variables
    Total_Votes = 0
    Candidates_votes_dictionary = {}  # Dictionary to storage the name with # of votes

    # Looping thru to get Total number of votes 
    for row in csvreader:
        Total_Votes += 1

        # To get the name of the candidate ** starting in 0 index
        candidate_name = row[2]  

        # How many times each candidate is in the list  
        # If the canidate is in the list
        if candidate_name in Candidates_votes_dictionary:
        # If the candidate exist, add one to the count
            Candidates_votes_dictionary[candidate_name] += 1
        else:
        # if it does not, add it to the dictionary and start the count in 1

            Candidates_votes_dictionary[candidate_name] = 1

    print("Total Votes:", Total_Votes)
    
    print("________________")
    # To get the amount of votes, loop thru the dictionary and count the votes for each candidate 

    for candidate, votes in Candidates_votes_dictionary.items():
        percentage = (votes/Total_Votes)*100
        print(f'{candidate}: {percentage:.3f}%({votes})')

    print("______________________")    
    #using a function to get the Winner - Which candidate has the max amount of votes - key= what is the criteria 
    # get = to obtain the value associated to the key 

    Winner = max(Candidates_votes_dictionary, key=Candidates_votes_dictionary.get)  

    print('Winner:', Winner )
    print("______________________")    


     # Open the output file in write mode and write the results
    with open("C:/Users/ximen/OneDrive/Escritorio/Penn_Data/3rd Module/election_results.txt", 'w') as txt_file:
        txt_file.write("election_results")


