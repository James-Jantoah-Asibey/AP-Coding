# Activity: 
# create a function that will loop through
# and print each number in the list and stops st the 48
# in your function, the list and the value
# that needs to be found should br passed as arguments

numberList = [1, 20, 39, 48, 72, 83]
value  = 48
 
def numberThings(numberList, value):
    for x in numberList:
        print(x)
        if x == value:
            break
        print(x)

numberThing(number, value)        