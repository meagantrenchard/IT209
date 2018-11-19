class Customer():
  def __init__(self, cust_name, email, phone, address):
    self.cust_name = cust_name
    self.email = email
    self.phone = phone
    self.address = address
    membershipAcct = []
    
  def nameInput(self):
    NI = input("Please enter your name: ")
    return NI
  
  def emailInput(self):
    EI = input(int("Please enter your phone num: "))
    return EI
  
  def addressInput(self):
    AI = input("Please enter your address: "))
    rerun AI
  
  def validateMembership(self):
    VM = input("Do you have a membership with us: (y/n)?")
    if VM == 'n':
      membershipAcct.append(VM)
      return "Congratualations, your membership is now created, and you are an official member"
    
    else:
      return "You already have a membership with us!"
   
  def __str__(self):class
    return(str(self.cust_name) + ',' + str(self.email) + ',' + str(self.phone) + ',' + str(self.address))
  
 
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
