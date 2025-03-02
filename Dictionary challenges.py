words = ["apple","banana","apple","orange","banana","apple"]

def frequency(words):
    wf = {}
    counter = 0
    for word in words:
        
        if word in wf:
            wf[word]+=1
        else:
            wf[word] = 1
    return wf
            

#print(frequency(words))

student_grades = {
    "Alice":[85,90,78],
    "Bob":[92,88,84],
    "Charlie":[70,75,80]

}

def avg(student_grades):

    grades = {}

    for k,v in student_grades.items():
        grades[k] = (sum(v)/ float(len(v)))
        
        
    return grades
#print(avg(student_grades))


values = {"a": 2,"b": 3,"c": 4}

def square_values(values):

    n_vals = {}
    for val in values:
        n_vals[val] = values[val]*values[val]
    return n_vals
#print(square_values(values))

dict1 = {"a":1,"b":2,"c":3}
dict2 = {"b":3,"c":4,"d":5}
def merge(dict1,dict2):
    full_d = dict1.copy()
    for key,value in dict2.items():
        if key in full_d:
            print(key,value)
            full_d[key] +=value
        else:
            print(key,value)
            full_d[key]=value
        
    return full_d
print(merge(dict1,dict2))
#stuck here, can merge the dictionaries however cannot add the values



