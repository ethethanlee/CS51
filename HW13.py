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


# print(read_records('CS51.csv'))


#  so need to find the grade, then do a for x in range(80 ,100) then insert them into a new list; 'none' will cause list to be at the end

records = [
['Lucy', ['CS51P', 90], ['CS54', 85], ['CS62', None], ['CS101', None], ['CS105', None], ['CS140', None]], 
['Bob',  ['CS51P', 82], ['CS54', 93], ['CS62', 91], ['CS101', None], ['CS105', 88], ['CS140', None]],
['Alice',['CS51P', None], ['CS54', 93], ['CS62', 97], ['CS101', 91], ['CS105', None], ['CS140', 85]]]


def sortbycoursegrade(book, cclass):
    listu = []
    activator = True
    base = 80
    while activator:
        if base == 100:
            for z in range(3):
                for n in range(1,6):
                    if book[z][n][0] == cclass and book[z][n][1] == None:
                        listu.append(book[x])
            activator = False
        for x in range(3):
            for y in range(1,6):
                if book[x][y][0] == cclass and book[x][y][1] == base:
                        listu.append(book[x])
        base += 1
    return listu



# print(sortbycoursegrade(records, 'CS51P'))

#use sort function

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [{'car': 'Ford', 'year': 2005},{'car': 'Mitsubishi', 'year': 2000},{'car': 'BMW', 'year': 2019},{'car': 'VW', 'year': 2011}]

cars.sort(key=lambda x: myFunc(x))
# print(cars)
# it does my func onto cars on its own



def grade(leest,clash):
    # records[0][1][0] is CS51P
    # student is the thing that will be lambda'd, but 
    for x in range(1,3):
            if clash == leest[x][0] and leest[x][1] != None:
                return leest[x][1]
            else:
                return 10928309128


def sort_these(leeest, classs):
    leeest.sort(key = (lambda x: grade(x,classs)))

sort_these(records, 'CS51P')
print(records)
