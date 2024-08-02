class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def authenticate(self, username, password):
        return self.username == username and self.password == password


class Ticket:
    ticket_counter = 0

    def __init__(self, user, category, description):
        Ticket.ticket_counter += 1
        self.id = Ticket.ticket_counter
        self.user = user
        self.category = category
        self.description = description
        self.status = 'Open'

    def __str__(self):
        return f"ID: {self.id}, Category: {self.category}, Description: {self.description}, Status: {self.status}"


class TicketSystem:
    def __init__(self):
        self.users = []
        self.tickets = []
        self.current_user = None
        self.create_default_users()

    def create_default_users(self):
        self.users.append(User("admin", "adminpass", True))
        self.users.append(User("user", "userpass"))

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        for user in self.users:
            if user.authenticate(username, password):
                self.current_user = user
                print(f"Welcome, {user.username}!")
                return True
        print("Login failed.")
        return False

    def create_ticket(self):
        category = input("Category (Technical/Administrative/Financial): ")
        description = input("Description: ")
        new_ticket = Ticket(self.current_user, category, description)
        self.tickets.append(new_ticket)
        print("Ticket created successfully.")

    def view_tickets(self):
        if self.current_user.is_admin:
            for ticket in self.tickets:
                print(ticket)
        else:
            for ticket in self.tickets:
                if ticket.user == self.current_user:
                    print(ticket)

    def update_ticket(self):
        if not self.current_user.is_admin:
            print("Access denied.")
            return
        ticket_id = int(input("Enter ticket ID: "))
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                new_status = input("Enter new status (Open/In Progress/Closed): ")
                ticket.status = new_status
                print("Ticket updated successfully.")
                return
        print("Ticket not found.")

    def run(self):
        if not self.login():
            return
        while True:
            if self.current_user.is_admin:
                print("\n1. View Tickets\n2. Update Ticket\n3. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.view_tickets()
                elif choice == '2':
                    self.update_ticket()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice.")
            else:
                print("\n1. Create Ticket\n2. View Tickets\n3. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.create_ticket()
                elif choice == '2':
                    self.view_tickets()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice.")


if __name__ == "__main__":
    system = TicketSystem()
    system.run()
