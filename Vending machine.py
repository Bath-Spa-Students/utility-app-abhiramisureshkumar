# BATHSPA VENDING MACHINE


class VendingMachine:
    def __init__(vend):
        # Define the items available in the vending machine
        vend.items = {
            "1" : {"name": "Coke", "price": 1.25 },
            "2" : {"name": "Pepsi", "price": 1.50},
            "3" : {"name": "Water", "price": 0.75},
            "4" : {"name" :"Sprite","price":1.25 },
            "5" : {"name" :"Fanta","price":2},
            "6" : {"name" :"Fruit Juice","price":5},
            "7" : {"name" :"Redbull","price":2.50},
            "8" : {"name" :"Mountain Dew","price":3},
            "9" : {"name" :"Dairymilk","price":4},
            "10": {"name" :"TWIX","price":2},
            "11": {"name" :"Snickers","price":2.50},
            "12": {"name" :"m$ms","price":1.25},
            "13": {"name" :"Protein Bar","price":2},
            "14": {"name" :"Cadbury","price":1.25},
            "15": {"name" :"Skittles","price":1.52},
            "16": {"name" :"Chicken Sandwich","price":5},
            "17": {"name" :"Veg Sandwich","price":4},
            "18": {"name" :"Lays","price":2},
            "19": {"name" :"Doritos","price":1.50},
            "20": {"name" :"Hot Chips","price":3.25},
            "21" : {"name" :"EXIT", "price":0 },
        }

        #initialize the balance and selected items
        vend.balance = 0
        vend.selected_item = None

    def display_menu(self):
        print("\nWelcome to the Vending Machine!")
        for key, item in self.items.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")

    def user_choice(vend):
        while True:
            code = input("Enter the number of your code: ")
            if code in vend.items:
                return code
            else:
                print("Invalid choice. select a valid option.")

    def payment_process(vend):
        while True:
            try:
                amount_inserted = float(input("Insert money (in dollars): $"))
                if amount_inserted >= 0:
                    return amount_inserted
                else:
                    print("Invalid amount. ")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")    

    def dispense_item(vend):
        item = vend.items[vend.selected_item]
        print(f"Dispensing {item['name']}. Enjoy your purchase!.")

    def run_vending_machine(vend):
        while True:
            vend.display_menu()
            vend.selected_item = vend.user_choice()

            if vend.selected_item == "21":
                print("")
                break

            selected_item_info= vend.items[vend.selected_item]
            print(f"Selected item: {selected_item_info['name']} - ${selected_item_info['price']:.2f}")

            vend.balance = vend.payment_process()

            if vend.balance >= selected_item_info['price']:
                change = vend.balance - selected_item_info['price']
                print(f"Your balance is: ${change:.2f}")
                vend.dispense_item()
                vend.balance = 0  # Reset balance after successful purchase
            else:
                print("Incorrect Amount. Transaction cancelled.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_vending_machine()
   