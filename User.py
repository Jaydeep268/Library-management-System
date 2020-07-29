# -*- coding: utf-8 -*-

from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id

    def viewBooks(self):
        Catalog.displayAllBooks()


class Member(User):
    members_list = []

    @classmethod
    def addMemberList(cls, member):
        cls.members_list.append(member)

    def __init__(self,name,location,age,aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_book_list = []

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def searchByname(self, name):
        Catalog.searchByName(name)

    def searchByAuthor(self, author):
        Catalog.searchByAuthor(author)

    #assume name is unique
    def issueBook(self,name,maxdays=10):
        days = 0

        c1 = [False, "Sorry.. your membership has been revoked.\nContact librarian for further details."]
        for member in Member.members_list:
            if member == self:
                c1[0] = True
                days = int(input("For how many days would you like to issue this book? "))

        c2 = [False, "Sorry! You can issue a book for a maximum of {} days".format(maxdays)]
        if days <= maxdays:
            c2[0] = True

        c3 = [False, "You can issue a maximum of 3 books at a time"]
        if len(self.issued_book_list) < 3:
            c3[0] = True

        conditions = [c1,c2,c3]

        for condition in conditions:
            if condition[0] == False:
                print(condition[1])
                break
        else:
            book_item =Member.issueBook(self.name, self.student_id, name, days)
            self.issued_book_list.append(book_item)
            print("Book reserved successfully!")
            print("Grab your copy {} from rack {}".format(book_item.isbn, book_item.rack))


    #assume name is unique
    def returnBook(self,name):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        for book_item in self.issued_book_list:
            print(book_item.book.name, book_item.isbn)
        isbn = input("Which book would you like to return? Enter isbn: ")
        days = int(input("How many days has it been since you issued this book? "))
        for book_item in self.issued_book_list:
            if book_item.isbn == isbn:
                ret_book_item = book_item
            else:
                print("Sorry.. the book you're trying to return is not issued by you!")
        self.issued_book_list.remove(ret_book_item)

        
        
class Librarian(User):

    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        Catalog.addBook(name,author,publish_date,pages)

    def addBookItem(self,isbn, rack):
        Catalog.addBookItem(isbn, rack)

    def removeBook(self,name):
        Catalog.removeBook(name)

    def removeBookItem(self, name,isbn):
        Catalog.removeBookItem(name,isbn)

    def addMember(self,name,location,age,aadhar_id,student_id):
         Member(name,location,age,aadhar_id,student_id)

    def removeMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                Member.members_list.remove(member)
                print("{} was successfully removed from the library!".format(name))
                break
        else:
            print("No such name exists")

    def viewMembers(self):
        for member in Member.members_list:
            print(member)

    def searchMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                print(member)
                for book_item in member.issued_books_list:
                    print(book_item.name, book_item.isbn)
                break
        else:
            print("There are no registered members in this library by this name.")
