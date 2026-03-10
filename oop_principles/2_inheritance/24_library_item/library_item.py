from datetime import datetime


class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checkout_status = False
        self.checkout_date = None

    def checkout(self):
        self.checkout_status = True
        self.checkout_date = datetime.now()

    def return_item(self):
        self.checkout_status = False
        self.checkout_date = None

    def get_info(self):
        return f"{self.title} by {self.author} (ID: {self.item_id})"

    def calculate_late_fee(self, return_date):
        return 0

    def is_overdue(self, current_date):
        if not self.checkout_date:
            return False
        return (current_date - self.checkout_date).days > 14


class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages, genre):
        super().__init__(title, author, item_id)
        self.pages = pages
        self.genre = genre

    def get_info(self):
        status = f"Checked out on {self.checkout_date.strftime('%Y-%m-%d')}" if self.checkout_status else "Available"
        return f"Book: {self.title} by {self.author} (ID: {self.item_id})\nPages: {self.pages}, Genre: {self.genre}\nStatus: {status}"

    def calculate_late_fee(self, return_date):
        if not self.checkout_date:
            return 0
        days_overdue = (return_date - self.checkout_date).days - 14
        return max(0, days_overdue * 0.50)


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def get_info(self):
        status = f"Checked out on {self.checkout_date.strftime('%Y-%m-%d')}" if self.checkout_status else "Available"
        return f"Magazine: {self.title} by {self.author} (ID: {self.item_id})\nIssue: {self.issue_number}, Published: {self.publication_date}\nStatus: {status}"

    def calculate_late_fee(self, return_date):
        if not self.checkout_date:
            return 0
        days_overdue = (return_date - self.checkout_date).days - 14
        return max(0, days_overdue * 0.25)


class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration, rating):
        super().__init__(title, author, item_id)
        self.duration = duration
        self.rating = rating

    def get_info(self):
        status = f"Checked out on {self.checkout_date.strftime('%Y-%m-%d')}" if self.checkout_status else "Available"
        return f"DVD: {self.title} by {self.author} (ID: {self.item_id})\nDuration: {self.duration} minutes, Rating: {self.rating}\nStatus: {status}"

    def calculate_late_fee(self, return_date):
        if not self.checkout_date:
            return 0
        days_overdue = (return_date - self.checkout_date).days - 14
        return max(0, days_overdue * 1.00)
