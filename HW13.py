


import csv

def read_records(filename):
    with open(filename) as csvfile:
        ceereader = csv.reader(csvfile, delimiter=',')
        diction = {}
        for column in ceereader:
            for x in range(7):
                if column[x] == column[0]:
                    pass
                elif len(column[0]) > 2:
                    # diction[column[0]] = column[x]
                    diction.setdefault(column[0], [])
                    diction[column[0]].append(column[x])
        return diction

    #     ceesv = ''
    #     for row in spamreader:
    #         ceesv = ceesv + ', '.join(row) + '\n'
    # return ceesv



print(read_records('CS51.csv'))