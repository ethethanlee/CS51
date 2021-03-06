from functools import reduce

records = {"tim": {('CS','51P'): 90, ('CS','62'): 92, ('PE','90'): 87, ('Econ','51'): 97}, 
"bob": {('CS','51P'): 78, ('Bio','52'): 94, ('PE','18'): 60, ('Math','101'): 95, ('Math','60'): 82}}



def avg_grade(book,student):
    average = 0
    for y in book[student].values():
        average += y
    average = average / len(book[student])
    return(average)


print(avg_grade(records,"tim"))


def average_grade(boo,studen):
    average = 0
    average = reduce(lambda x,y: x + y, [average + y for y in boo[studen].values()])/len(boo[studen])
    return(average)

print(average_grade(records,"tim"))


def course_roster(boook, classs):
    peepole = []
    for z,x in boook.items():
        for y in x.keys():
            if classs in y[0] + y[1]:
                peepole.append(z)
    return peepole

print(course_roster(records, "CS51P"))

def good_performance(rec, threshold):
    end = {}
    for person,valss in rec.items():
        for koy, value in valss.items():
            if value > threshold:
                end.setdefault(person, [])
                end[person].append(koy[0] + koy[1])
                
    return end



print(good_performance(records, 90))