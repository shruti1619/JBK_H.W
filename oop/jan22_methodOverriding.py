class parent:
    def property(self):
        print("car, money , home, land, jewellery, etc")
        
    def marry(self):
        print("arranged marriage girl A")
        
class child(parent):
    def property1(self):
        print("bike, laptop, phone")
        
    def marry(self):
        super().marry() # This will call parent class marry method
        print("love marriage girl B ")
        
jay=child()
jay.property()
jay.property1() 
jay.marry()  # This will call child class marry method due to method overriding
