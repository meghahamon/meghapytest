
def counts(string):
    myDictionary = {}
    for i in string:
        if i not in myDictionary:
            myDictionary[i]= 1
        else :
            myDictionary[i] = myDictionary[i]+1 
    return myDictionary

def panagram(s):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True

def average(numbers):
    if len(numbers) ==0 :
     return None
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

# a=average([10,10,10,10])
# print(a)



