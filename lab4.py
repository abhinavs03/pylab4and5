from abc import ABC, abstractmethod

# (a)
class Ticket(ABC):
    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price

    @abstractmethod
    def ticket_info(self):
        pass

# (b)
class StandardTicket(Ticket):
    def ticket_info(self):
        return f"Standard Ticket - Movie: {self.movie_name}, Seat: {self.seat_number}, Price: Rs.{self.price}"

class VIPTicket(Ticket):
    def ticket_info(self):
        return f"VIP Ticket - Movie: {self.movie_name}, Seat: {self.seat_number}, Price: Rs.{self.price}, Includes free snacks and drinks!"

class PremiumTicket(Ticket):
    def ticket_info(self):
        return f"Premium Ticket - Movie: {self.movie_name}, Seat: {self.seat_number}, Price: Rs{self.price}, Includes a reclining seat and extra legroom!"

# (c)
tickets = [
    StandardTicket("Movie A", "A12", 120.0),
    VIPTicket("Movie B", "VIP1", 200.0),
    PremiumTicket("Movie C", "P5", 250.0)
]

# (d)
for ticket in tickets:
    print(ticket.ticket_info())



'''
Standard Ticket - Movie: Movie A, Seat: A12, Price: Rs.120.0
VIP Ticket - Movie: Movie B, Seat: VIP1, Price: Rs.200.0, Includes free snacks and drinks!
Premium Ticket - Movie: Movie C, Seat: P5, Price: Rs250.0, Includes a reclining seat and extra legroom!
'''
