#write a class train which has methods to book a ticket , get status (no of seats )
# and gate fare information of trainn running under  indian railway 

class train:
    def __init__(self, train_name, seats,fare):
        self.train_name = train_name
        self.seats = seats
        self.fare = fare


    def book_ticket(self):
        if self.seats>0 :
            print("\nYour ticket has been successfully booked.")
            self.seats -= 1
            print(f"\nSeats left in {self.train_name} = {self.seats} ")

        else:
            print("\nSorry! no seats available")

    def get_status(self):
        print(f"Train name : {self.train_name}")
        print(f"Available seats : {self.seats}")

    def get_fare(self):
        print(f"Fare of {self.train_name} is {self.fare} rupees.")


t=train("Vande Bharat", 3,1200 )
t.get_status()
t.get_fare()
t.book_ticket()

t.get_status()
