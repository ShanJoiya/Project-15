class Library:
    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booksList:
            print(book)


    def lendBook(self, user, book):
        if book not in self.booksList:
            print("Sorry, We do not have that book.")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")  
        else:
            self.lendDict[book] = user
            print(
                "Lender-Book database has been updated. You can take the book now."
            ) 


    def addbook(self, book):
        self.booksList.append(book)
        print("f{book}has been added to the list".)                    


    def returnbook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been removed.")
        else:
            print("That book wasn't borrowed from us.")


if __name__ =='__main__':
    books = Library(['Python', 'rich Dad Poor Dad', 'Harry Potter', 'C++ BAsics', 'Algorithms by CLRS'],
                    "Let's upskill" )
    user_name = input("Welcome to ourlibrary! Please enter your name: ")  

    while True:
        print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an optoion:") 
        print("1. Display books\n2. Lend a book\n3. Add a book\4. Return a book\n5.Quit" ) 
        user_choice = input("Enter your choice to continue: ")


        if user_choice not in ['1', '2', '3', '4', '5']:
            print("please enter a valid option.")  
            continue
        if user_choice == '1':
            books.displayBooks() 
        elif user_choice == '2':
            book = input("Enter the name of the book you ant to lend :")
            books.lendBook(user_name, book)

        elif user_choice == '3':
            book = input("Enter the name of the book you want to add :")
            books.addBook(book) 
        elif user_choice == '4':                              
             book = input("Enter the name of the book you ant to return :")
             books.retuenBook(book)
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break
