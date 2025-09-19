# objects are construct for storing data and functions together
# when creating an object we start with the class keyward.
# This acts like our object maker/ our blueprint

#class carMaker:
    #def __init__(color, name, seating, year, model, miles):
       # self.name = name
       # self.color = color
        #self.seating = seating,
        #self.year = year
        #self.model = model
        
        #def printInfo(self):
            print('heres your car FAQS') #FACTS
            print('name: '+ self.name)
            print('year: '+ str(self.year))
            print('miles: ' + str(self.miles))


        def carFacts():
            print('name: ')
        def windshieldwipper():
            print('when raining turn on')

        def airbag():
            print('when driving a certain speed anc a collision happens; open')

        def turnsignals(up, down):
            if up:
                print("turn left")
            elif down:
                print("turn right")
            else:
                print("don't turn signals on")

        def bluetooth(year):
            if year > 2020:
                print("you have blietooth")
            else:
                print(" no bluetooth on this model")

carOption1 = carMaker('carolla', 'black', '2', '2024', 'carolla', 20000)

print(carOption1)

carOption1.printInfo()

class phone:
        def __init__(self , color, name, model, storage)
                self.color = color
                self.name = name
                self.model = model
                self.storage = storage


phoneA = phone(267-444-5656)
phoneB = phone(267-434-9847)

        def phoneFacts():
                print('name: ')

        def ringing():
                print('when phoneB is calling ring 4 times')        
                        





















