class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages =pages

    def __str__(self): #String Representation Function
        return "Title = {}, Author = {}, Pages ={}".format(self.title,self.author,self.pages)

    def __len__(self): #Length Representation function, to print the length of the book
        return self.pages

    def __del__(self): # Delete Representation
        print("The book has been deleted")

#All special method are indicated as __name__ 
mybook = Book("python","nimritee",200)
print(mybook) # When we print like this without using a string represntation function 
# it returns a object 
print(len(mybook))
del mybook