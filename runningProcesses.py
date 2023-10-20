import os
import psutil
import csv

# create a CSV file that lists all running processes and has columns for process ID #, name, executable path, CPU usage, and mem usage. 


#Get a list of running processes with process ID #, name, executable path, CPU usage, and mem usage
for proc in psutil.process_iter(['pid', 'name', 'memory_percent','cpu_percent','exe']):
    print(proc.info)


# Create CSV
def makeCSV():
    fieldnames = ['pid', 'name', 'memory_percent', 'cpu_percent', 'exe' ]
    rows =[]
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent','cpu_percent','exe']):
        rows.append(proc.info)
    with open("processes.csv", "w", encoding = "UTF8", newline='') as file:
        writer= csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print('CSV Created')

makeCSV()
