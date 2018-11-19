class Customer():
  def __init__(self, cust_name, email, phone, address):
    self.cust_name = cust_name
    self.email = email
    self.phone = phone
    self.address = address
    membershipAcct = []
    
  def nameInput():
    NI = input("Please enter your name: ")
    print(NI)
  
  def emailInput():
    EI = input(int("Please enter your phone num: "))
    print(EI)
  
  def addressInput():
    AI = input("Please enter your address: "))
    print(AI)
  
  def validateMembership():
    VM = input("Do you have a membership with us: (y/n)?")
    if VM == 'n':
      membershipAcct.append(VM)
      print("Congratualations, your membership is now created, and you are an official member")
      
    
  def __str__(self):
    return(str(self.cust_name) + ',' + str(self.email) + ',' + str(self.phone) + ',' + str(self.address))
class Book():
class Shelf():
