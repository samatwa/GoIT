from collections import UserString



class NumberString(UserString):
    def number_count(self):
        return sum(i.isdigit() for i in self.data)
        
            
        
            
                
                
            
                
        