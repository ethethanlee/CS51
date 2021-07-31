


import csv

def read_records(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        ceesv = ''
        for row in spamreader:
            ceesv = ceesv + ', '.join(row) + '\n'
    return ceesv



print(read_records('CS51.csv'))