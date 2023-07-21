from functions import create_product, get_products, delete_product, update_product, get_product, create_connection
from rich.console import Console
from rich.table import Table

create_connection()

def create():
    name = input("Please enter your product name: ")
    price = int(input("Please enter your product price: "))
    res = create_product(name, price)
    print(res)


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


def update(id):
    product = get_product(id)
    if product:
        name = input(
            "If you want update the product name, please enter the name, otherwise please enter 'n': ")
        price = input(
            "If you want update the product price, please enter the price, otherwise please enter 'n': ")
        if name.lower() == 'n':
            name = product['name']
        elif price.lower() == 'n':
            price = product['price']

        res = update_product(name, price, id)
        print(res)
    else:
        print("No Records Found.")


def delete(id):
    delete_product(id)


def go_back_menu():
    cont = input("\nDo you want to continue (y/n)? ")
    if cont.lower() == 'y':
        main()
    else:
        return


def main():
    print("1: Product List")
    print("2: Create Product")
    print("3: Edit Product")
    print("4: Delete product")
    print("5: Quit")

    choose = int(input("Enter your choice: "))

    match choose:
        case 1:
            get()
            go_back_menu()
        case 2:
            create()
            go_back_menu()
        case 3:
            id = int(input("Enter the product id: "))
            update(id)
            go_back_menu()
        case 4:
            id = int(input("Enter the product id: "))
            delete(id)
            go_back_menu()
        case 5:
            return


print("******* Welcome to the Restaurant *******")

main()
