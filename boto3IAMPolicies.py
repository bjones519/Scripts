# Using IAM boto3, create a function that iterates through a dictionary of IAM policies to create a CSV file
# with a row for each policy with the columns 'Policy Name', 'PolicyId', and 'Arn'.

import boto3
import json
import csv

client = boto3.client('iam')

# Get IAM policies in my AWS Account
policies = client.list_policies()
#print(policies)

# Created json file to see all of the data in a readable format
# with open("policies.json", "w") as write_file:
#     json.dump(policies, write_file, indent=4, default=str)
    
totalIAMPolicies= len(policies["Policies"])
#Create a csv file with the policies
def makeCSV():
    fieldnames = ['PolicyName', 'PolicyId', 'Arn' ]
    rows =[]
    
    for i in range(0, totalIAMPolicies):
 
        rows.append({'PolicyName':policies["Policies"][i]['PolicyName'], 
                    'PolicyId':policies['Policies'][i]['PolicyId'], 
                    'Arn':policies['Policies'][i]['Arn'],
                    })
    #open the CSV file for writing and create a csv.DictWriter object to write the data as a dictionary
    with open("IAMPolicies.csv", "w", encoding = "UTF8", newline='') as file:
        writer= csv.DictWriter(file, fieldnames=fieldnames)
        #write the header row with the field names
        writer.writeheader()
        writer.writerows(rows)
    print('CSV Created')

makeCSV()
