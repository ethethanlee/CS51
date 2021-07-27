records = {"tim": {('CS','51P'): 90, ('CS','62'): 92, ('PE','90'): 87, ('Econ','51'): 97}, 
"bob": {('CS','51P'): 78, ('Bio','52'): 94, ('PE','18'): 60, ('Math','101'): 95, ('Math','60'): 82}}

def avg_grade(book,student):
    average = 0
    for y in records[student].values():
        average += y
    average = average / len(records[student])
    return(average)


print(avg_grade(records,"tim"))








#average + x for x in book.values():