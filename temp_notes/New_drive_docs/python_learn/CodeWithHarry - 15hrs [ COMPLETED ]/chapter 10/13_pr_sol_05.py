class Train:

    def __init__(self, trainName, fare, seats):
        self.name = trainName
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is : {self.name}")
        print(f"The seats available in the train are : {self.seats}")
        
    def fareInfo(self):
        print(f"The fare of the ticket is : Rs {self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket is booked ! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry the train is full ! Kindly try in tatkal ")

    def cancelTicket(self, seatNumber):
        pass


intercity = Train("Intercity Express : 14506", 90, 2)
intercity.getStatus()
intercity.bookTicket()

intercity.getStatus()
intercity.bookTicket()

intercity.getStatus()
intercity.bookTicket()

intercity.fareInfo()


