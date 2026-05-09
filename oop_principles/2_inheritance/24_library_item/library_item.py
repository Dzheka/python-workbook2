from datetime import datetime, timedelta

class LibraryItem:
    def __init__ (self, title, author, item_id):
        self._title = title
        self._author = author
        self._item_id = item_id
        self._checkout_status = False
        self._checkout_date = None

    def checkout(self):
        self._checkout_status = True
        self._checkout_date = datetime.now()

    def return_item(self):
        self._checkout_status = False
        self._checkout_date = None

    def get_info(self):
        return f"Item: {self._title} by {self._author} (ID: {self._item_id})"

    def calculate_late_fee(self, return_date):
        raise NotImplementedError("Subclases must implement this method")

    def is_overdue(self, current_date):
        if not self._checkout_date:
            return False
        return (current_date - self._checkout_date).days > 14

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages, genre):
        super().__init__(title, author, item_id)
        self._pages = pages
        self._genre = genre

    def get_info(self):
        status = f"Status: {'Checked out on' + str(self._checkout_date) if self._checkout_status else 'Available'}"
        return (f"Book: {self._title} by {self._author} (ID: {self._item_id})\n"
                f"Pages: {self._pages}, Genre: {self._genre}\n{status}")

    def calculate_late_fee(self, return_date):
        if not self._checkout_date:
            return 0.0
        days_overdue = (return_date - self._checkout_date).days - 14
        return max(0, days_overdue * 0.5)
    
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date):
        super().__init__(title, author, item_id)
        self._issue_number = issue_number
        self._publication_date = publication_date

    def get_info(self):
        status = f"Status: {'Checked out on ' + str(self._checkout_date) if self._checkout_status else 'Available'}"
        return (f"Magazine: {self._title} by {self._author} (ID: {self._item_id})\n"
                f"Issue: {self._issue_number}, Published: {self._publication_date}\n{status}")

    
    def calculate_late_fee(self, return_date):
        if not self._checkout_date:
            return 0.0
        days_overdue = (return_date - self._checkout_date).days - 14
        return max(0, days_overdue * 0.25)

    
class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration, rating):
        super().__init__(title, author, item_id)
        self._duration = duration
        self._rating = rating

    def get_info(self):
        status = f"Status: {'Checked out on ' + str(self._checkout_date) if self._checkout_status else 'Available'}"
        return (f"DVD: {self._title} by {self._author} (ID: {self._item_id})\n"
                f"Duration: {self._duration} minutes, Rating: {self._rating}\n{status}")

    
    def calculate_late_fee(self, return_date):
        if not self._checkout_date:
            return 0.0
        days_overdue = (return_date - self._checkout_date).days - 14
        return max(0, days_overdue * 1.00)

    
# Create library items
book = Book("The Python Guide", "John Doe", "B001", 350, "Programming")
magazine = Magazine("Tech Today", "Jane Smith", "M001", 42, "2024-01-15")
dvd = DVD("Python Tutorial", "Tech Corp", "D001", 120, "G")

# Checkout items
book.checkout()
magazine.checkout()
dvd.checkout()

# Display information
print(book.get_info())
print(magazine.get_info())
print(dvd.get_info())

# Calculate late fees (assuming 20 days overdue)
return_date = datetime.now() + timedelta(days=20)
print(f"Book late fee: ${book.calculate_late_fee(return_date):.2f}")
print(f"Magazine late fee: ${magazine.calculate_late_fee(return_date):.2f}")
print(f"DVD late fee: ${dvd.calculate_late_fee(return_date):.2f}")
