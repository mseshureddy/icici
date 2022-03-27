def SingleTon(arg):
    d={}
    def inner():
        if len(d)==0:
            d[arg]=arg()
        return d[arg]
    return inner
@SingleTon
class Moive():
    def __init__(self):
        self.tickets=100
    def booking(self,n):
        if self.tickets>=n:
            print('Tickets booked suscessfully!!!')
            self.tickets-=n
        else:
            print('Invalid Tickets')
def BookMyshow():
    obj=Moive()
    n=int(input('Enter  Tickets: '))
    obj.booking(n)

BookMyshow()
BookMyshow()
BookMyshow()
