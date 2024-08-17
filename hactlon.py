from datetime import datetime, timedelta

class E_WasteItem:
    def __init__(self, name, purchase_date, lifespan_years):
        self.name = name
        self.purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        self.lifespan_years = lifespan_years
        self.expiry_date = self.purchase_date + timedelta(days=lifespan_years * 365)

    def check_status(self):
        today = datetime.now()
        if today >= self.expiry_date:
            return f"{self.name} is due for recycling."
        else:
            remaining_days = (self.expiry_date - today).days
            return f"{self.name} is still in use. Remaining lifespan: {remaining_days} days."

def add_item():
    name = input("Enter item name: ")
    while True:
        purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
        try:
            datetime.strptime(purchase_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    while True:
        try:
            lifespan_years = int(input("Enter expected lifespan (years): "))
            if lifespan_years <= 0:
                print("Lifespan must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    item = E_WasteItem(name, purchase_date, lifespan_years)
    items.append(item)
    print(f"\n{name} added successfully!\n")

def check_item_status():
    if not items:
        print("\nNo items found. Please add items first.\n")
    else:
        print("\nItems in the system:")
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item.name}")
        
        print("\nEnter the item number to check status, or type 'all' to check all items.")
        choice = input("Enter your choice: ")
        
        if choice.lower() == 'all':
            for item in items:
                print(item.check_status())
        else:
            try:
                item_number = int(choice) - 1
                if 0 <= item_number < len(items):
                    print(items[item_number].check_status())
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Invalid input. Please enter a number or 'all'.")
        print()

def main_menu():
    while True:
        print("\n--- E-waste Monitoring System ---")
        print("1. Add Electronic Item")
        print("2. Check Item Status")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            check_item_status()
        elif choice == '3':
            print("Exiting...")
            print("Exited")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    items = []
    main_menu()
