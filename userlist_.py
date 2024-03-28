from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(payment for payment in self.data if payment > 0)
        
        
            
                
        