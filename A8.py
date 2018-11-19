class Customer(object):

  def __init__(self, cust_name, email, phone, address):

    self.cust_name = cust_name

    self.email = email

    self.phone = phone

    self.address = address

    membershipAcct = []

    

  def nameInput():

    NI = input("Please enter your name: ")

    return (NI)

  
  def phoneInput():
    PI = input(str("Please enter your phone num: "))

    return(PI)

  

  def addressInput():

    AI = input("Please enter your address: ")

    return(AI)

  

  def validateMembership(self, NI):
    membershipAcct = []
    VM = input("Do you have a membership with us: (y/n)?")

    if VM == 'n':

      membershipAcct.append(NI)
      print(membershipAcct)

      return "Congratualations, your membership is now created, and you are an official member"

    

    else:

      return "You already have a membership with us!"

   

  #def __str__():

#    return(str(NI + ',' + PI + ',' + AI + ',' + VM))


#global code---------------------------------------------------------------------
print(Customer.nameInput())
print(Customer.phoneInput())
print(Customer.addressInput())
print(Customer.validateMembership())
#print(__str__())
#print(membershipAcct)



 
 Shelf():
  def __init__(self, title, genre, author, ISBN, cust_name):
    self.title = title
    self.genre = genre
    self.author = author
    self.ISBN = ISBN
    self.cust_name = cust_name
  def __str__(self):
    return(str(self.title) +','+ str(self.genre) +','+ str(self.author) +','+ str(self.ISBN) +','+ str(self.cust_name))

  class Book():
    def __init__(self, title, genre, author, ISBN, count):
      self.title = title
      self.genre = genre
      self.author = author
      self.ISBN = ISBN
      self.count = count
    def __str__(self):
      return(str(self.title) +','+ str(self.genre) +','+ str(self.author) +','+ str(self.ISBN) +','+ str(self.count))

  
  
  
#global code---------------------------------------------------------------------
print(Customer.nameInput())
print(Customer.phoneInput())
print(Customer.addressInput())
print(Customer.validateMembership())
#print(__str__())
#print(membershipAcct)
