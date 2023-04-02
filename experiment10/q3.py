#Creat a Book class having the member bname,bauthor,bprice and initialize value with constructor print it with detail() method
class Book:
    def __init__(self):
        self.bname = "jai sri Ram "
        self.bauthor = "Tulsi das"
        self.bprice = 200
    def detail(self):
        print("Book name is : ",self.bname)
        print("Book price is : ",self.bprice)
        print("Book author is : ",self.bauthor)
b=Book()
b.detail()



