def pdCheck():
    print("please enter a number.")
    number = input()
    values = []
    calculate = 'q'
    while calculate != 'stop': #whatever is not zero do this
        values.append(number)
        print(values)
        print("please enter a number")
        number = input()
    else:
        print('doing calculations') 

pdCheck()           

