import random

alphabet = "abcdefghijklmnopqrstuvwxyz "
desire = "methinks it is like a weasel"


def str_generator(string, length) :
    result = ""
    for i in range(0, length):
        result += string[random.randint(0, len(string)-1)]

    return result

def checker(str1, str2):# totally wrong 
    result = 0
    for n in range(0, len(str1)):
        if str1[n] == str2[n]:
            result += 1
        
    return result 

def working ():
    score  = 0
    count  = 0
    while True:
        string = str_generator(alphabet, len(desire))
        temp = checker(desire, string)
        if temp == len(desire):
            print("Final result: " + string + "After: " + count + " tries.")
            break
        elif  temp > score:
            score = temp
            percent = (temp/len(desire)) * 100
            print("Count %d, String: %s, percent: %d" % (count, string, percent))
        elif count %10000 == 0:
            print("Count %d, still working" %(count))
            
        count+=1

working()