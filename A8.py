class Customer(object):
  def __init__(self, cust_name, email, phone, address, member):
    self.cust_name = cust_name
    self.email = email
    self.phone = phone
    self.address = address
    self.member = member
  def __str__(self):
    return(str(self.cust_name) + ',' + str(self.email) + ',' + str(self.phone) + ',' + str(self.address) + ',' + boolen(self.member))

class Book(object):
  def __init__(self, title, ISBN, count, genre, author):
    self.title = title
    self.ISBN = ISBN
    self.count = count
    self.genre = genre
    self.author = author
  def __str__(self):
    return(str(self.title) + ',' + str(self.ISBN) + ',' + int(self.count) + ',' + str(self.genre) + ',' + str(self.author))

  
class Shelf(object):
  def __init__(self, title, ISBN, count, genre, author, cust_name):
    self.title = title
    self.ISBN = ISBN
    self.count = count
    self.genre = genre
    self.author = author 
    self.cust_name = cust_name
  def __str__(self):
    return(str(self.title) + ',' + str(self.ISBN) + ',' + int(self.count) + ',' + str(self.genre) + ',' + str(self.author) + ',' + str(self.cust_name))

