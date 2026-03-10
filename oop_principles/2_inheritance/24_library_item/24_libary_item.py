from datetime import datetime, timedelta


class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title           = title
        self.author          = author
        self.item_id         = item_id
        self.checkout_status = False
        self.checkout_date   = None

    def checkout(self):
        self.checkout_status = True
        self.checkout_date   = datetime.now()

    def return_item(self):
        self.checkout_status = False
        self.checkout_date   = None

    def is_overdue(self, current_date):
        if self.checkout_date is None:
            return False
        days_out = (current_date - self.checkout_date).days
        return days_out > 14

    def get_info(self):
        return f"{self.title} by {self.author} (ID: {self.item_id})"

    def calculate_late_fee(self, return_date):
        return 0



class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages, genre):
        super().__init__(title, author, item_id)
        self.pages = pages
        self.genre = genre

    def get_info(self):
        status = f"Checked out on {self.checkout_date.strftime('%Y-%m-%d')}" if self.checkout_status else "Available"
        return (
            f"Book: {self.title} by {self.author} (ID: {self.item_id})\n"
            f"Pages: {self.pages}, Genre: {self.genre}\n"
            f"Status: {status}"
        )

    def calculate_late_fee(self, return_date):
        if self.checkout_date is None:
            return 0
        days_overdue = (return_date - self.checkout_date).days - 14
        if days_overdue <= 0:
            return 0
        return days_overdue * 0.50



class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date):
        super().__init__(title, author, item_id)
        self.issue_number     = issue_number
        self.publication_date = publication_date

    def get_info(self):
        status = f"Checked out on {self.checkout_date.strftime('%Y-%m-%d')}" if self.checkout_status else "Available"
        return (
            f"Magazine: {self.title} by {self.author} (ID: {self.item_id})\n"
            f"Issue: {self.issue_number}, Published: {self.publication_date}\n"
            f"Status: {status}"
        )

    def calculate_late_fee(self, return_date):
        if self.checkout_date is None:
            return 0
        days_overdue = (return_date - self.checkout_date).days - 14
        if days_overdue <= 0:
            return 0
        return days_overdue * 0.25     # $0.25 per day



class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration, rating):
        super().__init__(title, author, item_id)
        self.duration = duration
        self.rating   = rating

    def get_info(self):
        status = f"Checked out on {self.checkout_date.strftime('%Y-%m-%d')}" if self.checkout_status else "Available"
        return (
            f"DVD: {self.title} by {self.author} (ID: {self.item_id})\n"
            f"Duration: {self.duration} minutes, Rating: {self.rating}\n"
            f"Status: {status}"
        )

    def calculate_late_fee(self, return_date):
        if self.checkout_date is None:
            return 0
        days_overdue = (return_date - self.checkout_date).days - 14
        if days_overdue <= 0:
            return 0
        return days_overdue * 1.00



book     = Book("The Python Guide", "John Doe",   "B001", 350, "Programming")
magazine = Magazine("Tech Today",   "Jane Smith", "M001", 42,  "2024-01-15")
dvd      = DVD("Python Tutorial",   "Tech Corp",  "D001", 120, "G")

book.checkout()
magazine.checkout()
dvd.checkout()

print(book.get_info())
print()
print(magazine.get_info())
print()
print(dvd.get_info())


return_date = datetime.now() + timedelta(days=20)
print(f"\nBook late fee:     ${book.calculate_late_fee(return_date):.2f}")
print(f"Magazine late fee: ${magazine.calculate_late_fee(return_date):.2f}")
print(f"DVD late fee:      ${dvd.calculate_late_fee(return_date):.2f}")

