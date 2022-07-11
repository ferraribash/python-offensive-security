import sqlite3
import csv

#after copy the chrome History file you can run this program.
#Modify the folders in the code.
#Author: Thiago Ferrari

a = sqlite3.connect("C:/Users/example/History")
cur = a.cursor()
cur.execute ("select url, title,last_visit_time from urls")
results = cur.fetchall()
#Save in CSV file
with open('C:/Users/example/desktop/historico.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(results)


