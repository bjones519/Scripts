
# Retrieve a JSON of all NBA players using the Python requests module with this API 
# Manipulate the data to create a CSV file with the player ID, first and last name, position, and full team name.

import json
import csv
import requests

url = "https://free-nba.p.rapidapi.com/players"


querystring = {"page":"1","per_page":"100"}

headers = {
	"X-RapidAPI-Key": "api-key",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
#print(type(response.json()))
responses=response.json()
print(responses)


totalPlayers= len(responses["data"])


#Create CSV
def makeCSV():
    fieldnames = ['id', 'first_name', 'last_name', 'position','name' ]
    rows =[]
    
    for i in range(0, totalPlayers):
 
        rows.append({'id':responses['data'][i]['id'], 
                    'first_name':responses['data'][i]['first_name'], 
                    'last_name':responses['data'][i]['last_name'],
                    'position':responses['data'][i]['position'],
                    'name':responses['data'][i]["team"]["name"]
                    })
    #open the CSV file for writing and create a csv.DictWriter object to write the data as a dictionary
    with open("nbaPlayers.csv", "w", encoding = "UTF8", newline='') as file:
        writer= csv.DictWriter(file, fieldnames=fieldnames)
        #write the header row with the field names
        writer.writeheader()
        #write the process information for each process into the csv
        writer.writerows(rows)
    print('CSV Created')

makeCSV()
