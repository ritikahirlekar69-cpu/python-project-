# Stationery Shop Management System

MAX_ITEMS = 50

# Initial stationery items
items = [
    {"id": 101, "name": "Notebook", "price": 40.00, "quantity": 50},
    {"id": 102, "name": "Pen", "price": 10.00, "quantity": 100},
    {"id": 103, "name": "Pencil", "price": 5.00, "quantity": 100},
    {"id": 104, "name": "Eraser", "price": 5.00, "quantity": 50},
    {"id": 105, "name": "Sharpener", "price": 8.00, "quantity": 50},
    {"id": 106, "name": "Scale", "price": 10.00, "quantity": 40},
    {"id": 107, "name": "Marker", "price": 25.00, "quantity": 30},
    {"id": 108, "name": "File", "price": 20.00, "quantity": 40},
    {"id": 109, "name": "Drawing Book", "price": 60.00, "quantity": 25},
    {"id": 110, "name": "Colour Pencils", "price": 80.00, "quantity": 20}
]

total_sales = 0
total_revenue = 0.0


# Display all stationery items
def display_items():
    print("\n========== STATIONERY ITEMS ==========")
    print(f"{'ID':<8}{'Name':<20}{'Price':<12}{'Stock':<10}")
    print("-" * 50)

    for item in items:
        print(
            f"{item['id']:<8}"
            f"{item['name']:<20}"
            f"Rs.{item['price']:<10.2f}"
            f"{item['quantity']:<10}"
        )


# Add a new item
def add_item():
    if len(items) >= MAX_ITEMS:
        print("\nInventory is full!")
        return

    item_id = int(input("\nEnter Item ID: "))

    if find_item(item_id) is not None:
        print("\nItem ID already exists!")
        return

    name = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))
    quantity = int(input("Enter Item Quantity: "))

    if price < 0 or quantity < 0:
        print("\nInvalid price or quantity!")
        return

    new_item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    items.append(new_item)

    print("\nItem added successfully!")


# Search item using ID
def search_item():
    item_id = int(input("\nEnter Item ID to search: "))

    item = find_item(item_id)

    if item is not None:
        print("\nItem Found!")
        print("ID       :", item["id"])
        print("Name     :", item["name"])
        print("Price    : Rs.", item["price"])
        print("Quantity :", item["quantity"])
    else:
        print("\nItem not found!")


# Purchase an item
def purchase_item():
    global total_sales, total_revenue

    item_id = int(input("\nEnter Item ID: "))

    item = find_item(item_id)

    if item is None:
        print("\nItem not found!")
        return

    print("Item Name:", item["name"])
    print("Price: Rs.", item["price"])
    print("Available Stock:", item["quantity"])

    quantity = int(input("Enter Quantity to Purchase: "))

    if quantity <= 0:
        print("\nInvalid quantity!")
        return

    if quantity > item["quantity"]:
        print("\nInsufficient Stock!")
        return

    bill = item["price"] * quantity

    item["quantity"] -= quantity

    total_sales += 1
    total_revenue += bill

    print("\n========== CUSTOMER BILL ==========")
    print("Item Name :", item["name"])
    print("Quantity  :", quantity)
    print("Price     : Rs.", item["price"])
    print("-" * 35)
    print(f"Total Bill: Rs. {bill:.2f}")
    print("=" * 35)

    print("\nPurchase Successful!")


# Update stock
def update_stock():
    item_id = int(input("\nEnter Item ID: "))

    item = find_item(item_id)

    if item is None:
        print("\nItem not found!")
        return

    print("Item Name:", item["name"])
    print("Current Stock:", item["quantity"])

    quantity = int(input("Enter New Stock Quantity: "))

    if quantity < 0:
        print("\nInvalid quantity!")
        return

    item["quantity"] = quantity

    print("\nStock Updated Successfully!")


# Display sales summary
def sales_summary():
    print("\n========== SALES SUMMARY ==========")
    print("Total Transactions :", total_sales)
    print(f"Total Revenue     : Rs. {total_revenue:.2f}")
    print("=" * 35)


# Find item by ID
def find_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item

    return None


# Main program
def main():
    while True:
        print("\n====================================")
        print("   STATIONERY SHOP MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Display Stationery Items")
        print("2. Add New Item")
        print("3. Search Item")
        print("4. Purchase Item")
        print("5. Update Stock")
        print("6. Sales Summary")
        print("7. Exit")

        print("------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_items()

        elif choice == "2":
            add_item()

        elif choice == "3":
            search_item()

        elif choice == "4":
            purchase_item()

        elif choice == "5":
            update_stock()

        elif choice == "6":
            sales_summary()

        elif choice == "7":
            print("\nThank you for visiting our shop!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Start the program
main()
