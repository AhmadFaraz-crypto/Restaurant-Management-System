from functions import get_products, create_order, create_connection, get_order_history
from rich.console import Console
from rich.table import Table

create_connection()

arr = []


def get():
    table = Table(title="Products")
    
    products_list = get_products()
    columns = ["id", "Name", "Price"]
    for column in columns:
        table.add_column(column)
    if products_list:
        for product in products_list:
            table.add_row(str(product["id"]), product["name"], str(product["price"]), style='bright_green')
        console = Console()
        console.print(table)
    else:
        print("No Records Found.")


def order():
    product_id = int(input("Please enter your product id: "))
    quantity = int(input("Please enter your product quantity: "))
    arr.append((product_id, quantity))
    res = create_order(product_id, quantity)
    print(res)


def bill_details(orders):
    products_list = get_products()
    total_price = 0
    table = Table(title="Order details")
    columns = ["id", "Name", "Price", "Quantity", "Total Price"]

    for column in columns:
        table.add_column(column)

    if len(orders):
        for order in orders:
            if products_list:
                for product in products_list:
                    print(product)
                    print(order)
                    if order["product_id"] == product["id"]:
                        total_price = total_price + product["price"]
                        table.add_row(str(product["id"]), product["name"], str(product["price"]), str(order["quantity"]), "", style='bright_green')
                console = Console()
                console.print(table)
            else:
                print("No Records Found.")
        print(total_price)
        table.add_row("", "", "", "", str(total_price), style='bright_red')
        console = Console()
        console.print(table)
    else:
        print("No Records Found.")


def go_back_menu():
    cont = input("Do you want to continue (y/n)? ")
    if cont.lower() == 'y':
        main()
    else:
        return


def main():
    get()
    print("1: Create Order")
    print("2: Get Bill")
    print("3: Product Sales List")
    print("4: Quit")

    choose = int(input("Enter your choice: "))

    match choose:
        case 1:
            order()
            go_back_menu()
        case 2:
            bill_details(arr)
            go_back_menu()
        case 3:
            res = get_order_history()
            bill_details(res)
            go_back_menu()
        case 4:
            return


print("******* Welcome to the Restaurant *******")

main()
