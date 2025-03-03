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
#print(merge(dict1,dict2))

data = {
  "fruit": ["apple", "banana", "orange"],
  "colour": ["red", "yellow", "orange"]
 }

def transform_data(data):
     list1 = []
     for item in data:
         for value in data.get(item):
             list1.append({item:value})
     return list1

#print(transform_data(data))

data = {"a": 1, "b": 2, "c": 3}

def remove_and_return(data,value):
     out = data.get(value)
     data.pop(value)
     return out

#print(remove_and_return(data, "b")) # Output: 2
#print(data) # Output: {'a': 1, 'c': 3}

data = {"x": 10, "y": 20, "z": 30}

def pop_all_values(data):
     out = []
     for item in data:
         out.append(data.get(item))

     while len(data)>0:
         data.popitem()
    
     return(out)

#print(pop_all_values(data)) # Output: [10, 20, 30]
#print(data) # Output: {}

data = {"p": 5, "q": 15, "r": 25}

def pop_and_sum(data,values):
     sum = 0
     for item in data:
         if item in values:
             sum += data.get(item)
    
     for item in values:
         if item in data:
             data.pop(item)

     return sum

#print(pop_and_sum(data, ["p", "r"])) # Output: 30
#print(data) # Output: {'q': 15}

data = {"m": 7, "n": 14}

def pop_with_default(data,value,default):
     if value in data:
         out = data.get(value)
         data.pop(value)
         return out

     else:
         return default

#print(pop_with_default(data, "n", 0)) # Output: 14
#print(pop_with_default(data, "o", 0)) # Output: 0
#print(data) # Output: {'m': 7}

data = {"a": 1, "b": 2, "c": 3, "d": 4}

def pop_and_create_new(data, values):
     newdict = {}
     for item in data:
         if item in values:
             newdict[item] = data.get(item)

     for item in values:
          if item in data:
              data.pop(item)

     return newdict
    

print(pop_and_create_new(data, ["b", "d"])) # Output: {'b': 2, 'd': 4}
print(data) # Output: {'a': 1, 'c': 3}
