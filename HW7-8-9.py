#HW7
def repN_ForSeq(phrase):
    myStr = ""
    repeat = 0
    for character in phrase: #for each *blank* in the thing, *blank*, run some command
        repeat = repeat + 1
        myStr = myStr + character*repeat
    print(myStr)

def repN_ForInd(word):
    end = ""
    for number in range(len(word)):
        variable = number + 1
        end = end + word[number]*variable
    print(end)

def repN_WhileInd(emily):
    count = 0
    strig = ""
    while count < len(emily):
        strig = strig + emily[(count)]*(count + 1)
        count = count + 1
    print(strig)
    


def repN_Recur(n):

    if n == "" :

        return n
    else:
        return repN_Recur(n[:-1])  + n[len(n)-1]*len(n)
        



hello = "emily"

print(repN_Recur(hello))


#HW8

def flip_char(input):
    output = ""
    #imma go through each letter of the input and if upper case then lower it else upper it
    for character in input:
        if character.isupper():
            output = output + character.lower()
        else:
            output = output + character.upper()
    return output


def format_name(input):
    if input.count(" ") == 2:
        return input[input.find(" ", input.find(" ") + 1) + 1:] + ", " + input[:input.find(" ")] + " " + input[input.find(" ") + 1:][0] + "."
    elif input.count(" ") == 1:
        return input[input.find(" ") + 1:] + ", " + input[:input.find(" ")]
        

hello = "Ethan Lee"

print(format_name(hello))



a_list = ['cs', 'math', ['bio', 'chem'], 'cogsci', 
         ['history', 'econ', 'music']]
         
val3 = a_list[::2]
val3.insert(1,val3[2][1])
print(val3)

#HW9

tim = [['CSCI51P', 90], ['CSCI62', 92],['Math101', 87],['Econ51', 97]]
bob = [['CSCI51P', 78], ['Econ52', 94],['Econ151', 60],['Math101', 95], ['Math60', 82]]


def getCourses(n_list, grade):
    my_list = []
    for a_list in n_list:
        if a_list[1] > grade:
            my_list.append(a_list[0])
    return my_list

def avgGrade(n_list):
    total = 0
    for a_list in n_list:
        total += a_list[1]
    return total/len(n_list)

print(avgGrade(tim))