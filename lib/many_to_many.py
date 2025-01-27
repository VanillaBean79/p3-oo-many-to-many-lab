class Author:

    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())



class Book:

    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all_contracts = []
    

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")

        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        
        if not isinstance(date, str):
            raise Exception("Date must be a string representing when the contract was signed.")
        
        if not isinstance(royalties, (int, float)):
            raise Exception("Royalties must be a number between 0 and 100.")
        
   
    @classmethod
    def contracts_by_date(cls, date):
       return sorted(
            [contract for contract in cls.all_contracts if contract.date == date],
            key = lambda contract: contract.date)
    
    
