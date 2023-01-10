class parking_garage():
    def __init__(self, tickets, parkingSpaces, currentTicket, payment):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.payment = payment
    
    def takeTicket(self):
        self.tickets = current_parking.tickets - 1
        self.parkingSpaces = current_parking.parkingSpaces - 1

    def payForParking(self):
        self.payment = 5 + current_parking.payment
        self.currentTicket["paid"] = True
        print(f'You have 15 mins to leave. There are currently {self.parkingSpaces} parking spaces left in the lot.')
            
    def leaveGarage(self):
        if self.tickets <= 9:
            self.tickets = current_parking.tickets + 1
            self.parkingSpaces = current_parking.parkingSpaces + 1
            self.currentTicket["paid"] = False
        print(f'Thank you, have a nice day! There are currently {current_parking.parkingSpaces} parking spaces left in the lot.')


current_parking = parking_garage(10, 10, {"paid": False}, 0)

def run():
    while True:
        question_ticket = input("Would you like to take a ticket? Type Yes or No. ")
        if question_ticket.lower() == "yes":
            print("Here is your ticket.")
            current_parking.takeTicket()
            current_parking.payForParking()
            continue
        if question_ticket.lower() == "no":
            goodbye = input("Do you want to leave? Enter yes or no. ")
            if goodbye.lower() == "yes":   
                current_parking.leaveGarage()
                break
            if goodbye.lower() == "no":
                continue

run()

