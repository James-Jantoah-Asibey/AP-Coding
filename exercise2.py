

def pdCheck():
    print("Please enter a number")
    number = input()
    values = []

    while number!= 'q':
        values.append(int(number))
        print(values)
        print("Please enter a number")
        number = input()
    else:
        print('doing calculation...')
        total = sum(values)
        print(total)


pdCheck()        

#which team has the best home point differential this season
'the best home PD is indianan with a 64 PD'

#whihc team has the bes away point differential this season?
'the best away PD is'