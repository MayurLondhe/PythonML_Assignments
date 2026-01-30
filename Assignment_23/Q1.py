class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")

obj1 = BookStore("Linux system programming", "Robert Love")

obj1.Display()

obj2 = BookStore("Python Programming", "Mayur Londhe")

obj2.Display()

