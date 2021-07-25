a_list = ['CS51P', 'Computer Science', 'I love CS', 'CS1', 'ID1', 'CS62', 'CS']

new_list = [str(i)[::-1] for i in a_list if not "CS" in i and len(i) > 2]

tim = [['CSCI51P', 90], ['CSCI62', 92],['Math101', 87],['Econ51', 97]]
bob = [['CSCI51P', 78], ['Econ52', 94],['Econ151', 60],['Math101', 95], ['Math60', 82]]

grade_list = [i[0] for i in tim if i[1] > 90]

student = tim
majors = ['CSCI', 'Econ']
mejores = [i for i in student if i[0][:4] in majors]


print(mejores)

#bob = {"class": 90, "math": 10}

#for class, grade in bob.items():