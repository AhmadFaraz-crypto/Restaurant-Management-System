from functions import get_products, create_order, create_connection, get_order_history

create_connection()

arr = []


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


def order():
    product_id = int(input("Please enter your product id: "))
    quantity = input("Please enter your product quantity: ")
    arr.append({"product_id": product_id, "quantity": quantity})
    res = create_order(product_id, quantity)
    print(res)


def bill_details(orders):
    products_list = get_products()
    print("---\t----\t\t-----\t--------\t-----------")
    print("|id\tname\t\tprice\tquantity\tTotal Price|")
    print("---\t----\t\t-----\t--------\t-----------")
    if len(orders):
        for order in orders:
            if products_list:
                for product in products_list:
                    if order['product_id'] == product['id']:
                        total_price = 0
                        total_price = total_price + product['price']
                        print(
                            f"{product['id']}\t{product['name']}\t{product['price']}\t{order['quantity']}")
                        print("---\t----\t\t-----\t--------\t-----------")
                        print(f"\t\t\t\t\t\t {total_price}")
            else:
                print("No Records Found.")
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
