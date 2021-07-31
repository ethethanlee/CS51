import csv
def read_records(filename):
    with open(filename) as csvfile:
        ceereader = csv.reader(csvfile, delimiter=',')
        diction = {}
        ces = []
        for column in ceereader:
            for x in range(7):
                if 'CS' in column[x]:
                    ces.append(column[x])
                elif column[x] == column[0]:
                    pass
                elif len(column[0]) > 2:
                    hello = [ces[x-1] + ', ' + column[x]]
                    diction.setdefault(column[0], [])
                    diction[column[0]].append(hello)
        return diction
        

# need to turn '90' into ['CS51P', '90']
# need to bring back up the first instance of column from the for loop


print(read_records('CS51.csv'))