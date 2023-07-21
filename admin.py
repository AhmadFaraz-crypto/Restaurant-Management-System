from functions import create_product, get_products, delete_product, update_product, get_product, create_connection

create_connection()

def create():
    name = input("Please enter your product name: ")
    price = int(input("Please enter your product price: "))
    res = create_product(name, price)
    print(res)


def get():
    products_list = get_products()
    print("---\t----\t\t-----")
    print("|id\tname\t\tprice|")
    print("---\t----\t\t-----")
    if products_list:
        for product in products_list:
            print(f"{product['id']}\t{product['name']}\t{product['price']}")
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
    cont = input("Do you want to continue (y/n)? ")
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
