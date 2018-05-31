import sqlite3
#made by Nhmanas

conn = sqlite3.connect('users.db')
c = conn.cursor()


def welcome():
    print("Welcome to Nhmanas' store! You must login or register to see all the goodies!\n"
          "Type the number of your selection to continue...")
    selection = int(input("1) Register\n2) Login\n3) Exit\n-| "))
    if selection == 1:
        register()
    if selection == 2:
        login()
    if selection == 3:
        return True
    else:
        input("\nInvalid selection\nPress enter to continue\n")
        welcome()


def register():
    print("You selected registration")
    username = input("Username: ")
    password = input("Password: ")
    authority = input("Authority level (1 or 2): ")
    name = input("Name           : ")
    surname = input("Surname        : ")
    idnum = input("Identity Number: ")
    c.execute("CREATE TABLE IF NOT EXISTS userInfo(username TEXT, password TEXT, "
              "authority REAL, name TEXT, surname TEXT, idnum TEXT)")
    c.execute("INSERT INTO userInfo (username, password, authority, name, surname, idnum) "
              "VALUES(?, ?, ?, ?, ?, ?)", (username, password, authority, name, surname, idnum))

    conn.commit()
    login()


def login():
    print("\nYou're in login section")
    username = input("Username: ")
    password = input("Password: ")
    find_user = 'SELECT * FROM userInfo WHERE username = ? AND password = ?'
    c.execute(find_user, [username, password])
    data = c.fetchall()
    if data:
        for row in data:
            if row[2] == 1:
                print('\nWelcome customer ' + username)
                customer()
            if row[2] == 2:
                print('\nWelcome admin ' + username)
                admin()
    else:
        print("Username or password didn't match any information in database")
        again = input("Try login again or go to register function? (y/n)\n-| ")
        if again.lower() == "n":
            register()
        elif again.lower() == "y":
            login()
        else:
            input("\nInvalid selection\nPress enter to continue\n")
        login()


def customer():
    selection = int(input("1) Select a category to list sub-items\n2) List all items\n"
                          "3) My shopping basket\n4) Logout\n-| "))

    if selection == 4:
        welcome()
    if selection == 3:
        c.execute('SELECT * FROM basket')
        data = c.fetchall()
        for row in data:
            print(row)
        again = (input("Buy all? (y/n)\n-| "))
        if again.lower() == "n":
            c.execute("DELETE FROM basket")

            conn.commit()
            print("List cleaned")
            customer()
        if again.lower() == "y":
            buy()
        else:
            input("\nInvalid selection\nPress enter to continue\n")
            customer()
    if selection == 2:
        shopall()
    if selection == 1:
        shop()
    else:
        input("\nInvalid selection\nPress enter to continue\n")
        customer()


def shop():
    c.execute('SELECT * FROM mainTable')
    data = c.fetchall()
    for row in data:
        print(row)
    cat = int(input("-|"))

    if cat == 1:
        find_sub = 'SELECT * FROM subTable WHERE id1 = ?'
        c.execute(find_sub, [cat])
        sub = c.fetchall()
        for row in sub:
            print(row)
        cat = int(input("-|"))

        if cat == 1:
            find_sub = 'SELECT * FROM productTable WHERE id2 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchall()
            for row in sub:
                print(row)
            cat = int(input("-|"))
            find_sub = 'SELECT * FROM productTable WHERE id3 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchone()
            c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
                      "VALUES(?, ?, ?)", (str(sub[0]) + str(sub[1]) + str(sub[2]), str(sub[3]), sub[4]))

            conn.commit()
            print("\nFollowing item is added to your basket:")
            print(sub)
            again = input("Shop again? (y/n)\n-| ")
            if again.lower() == "n":
                customer()
            elif again.lower() == "y":
                shop()
        if cat == 2:
            find_sub = 'SELECT * FROM productTable WHERE id2 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchall()
            for row in sub:
                print(row)
            cat = int(input("-|"))
            find_sub = 'SELECT * FROM productTable WHERE id3 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchone()
            c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
                      "VALUES(?, ?, ?)", (str(sub[0]) + str(sub[1]) + str(sub[2]), str(sub[3]), sub[4]))

            conn.commit()
            print("\nFollowing item is added to your basket:")
            print(sub)
            again = input("Shop again? (y/n)\n-| ")
            if again.lower() == "n":
                customer()
            elif again.lower() == "y":
                shop()
        else:
            input("\nInvalid selection\nPress enter to continue\n")
            shop()

    if cat == 2:
        find_sub = 'SELECT * FROM subTable WHERE id1 = ?'
        c.execute(find_sub, [cat])
        sub = c.fetchall()
        for row in sub:
            print(row)
        cat = int(input("-|"))

        if cat == 3:
            find_sub = 'SELECT * FROM productTable WHERE id2 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchall()
            for row in sub:
                print(row)
            cat = int(input("-|"))
            find_sub = 'SELECT * FROM productTable WHERE id3 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchone()
            c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
                      "VALUES(?, ?, ?)", (str(sub[0]) + str(sub[1]) + str(sub[2]), str(sub[3]), sub[4]))

            conn.commit()
            print("\nFollowing item is added to your basket:")
            print(sub)
            again = input("Shop again? (y/n)\n-| ")
            if again.lower() == "n":
                customer()
            elif again.lower() == "y":
                shop()
        if cat == 4:
            find_sub = 'SELECT * FROM productTable WHERE id2 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchall()
            for row in sub:
                print(row)
            cat = int(input("-|"))
            find_sub = 'SELECT * FROM productTable WHERE id3 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchone()
            c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
                      "VALUES(?, ?, ?)", (str(sub[0]) + str(sub[1]) + str(sub[2]), str(sub[3]), sub[4]))

            conn.commit()
            print("\nFollowing item is added to your basket:")
            print(sub)
            again = input("Shop again? (y/n)\n-| ")
            if again.lower() == "n":
                customer()
            if again.lower() == "y":
                shop()
            else:
                input("\nInvalid selection\nPress enter to continue\n")
                shop()
        else:
            input("\nInvalid selection\nPress enter to continue\n")
            shop()

    if cat == 3:
        find_sub = 'SELECT * FROM subTable WHERE id1 = ?'
        c.execute(find_sub, [cat])
        sub = c.fetchall()
        for row in sub:
            print(row)
        cat = int(input("-|"))

        if cat == 5:
            find_sub = 'SELECT * FROM productTable WHERE id2 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchall()
            for row in sub:
                print(row)
            cat = int(input("-|"))
            find_sub = 'SELECT * FROM productTable WHERE id3 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchone()
            c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
                      "VALUES(?, ?, ?)", (str(sub[0]) + str(sub[1]) + str(sub[2]), str(sub[3]), sub[4]))

            conn.commit()
            print("\nFollowing item is added to your basket:")
            print(sub)
            again = input("Shop again? (y/n)\n-| ")
            if again.lower() == "n":
                customer()
            elif again.lower() == "y":
                shop()
        if cat == 6:
            find_sub = 'SELECT * FROM productTable WHERE id2 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchall()
            for row in sub:
                print(row)
            cat = int(input("-|"))
            find_sub = 'SELECT * FROM productTable WHERE id3 = ?'
            c.execute(find_sub, [cat])
            sub = c.fetchone()
            c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
                      "VALUES(?, ?, ?)", (str(sub[0]) + str(sub[1]) + str(sub[2]), str(sub[3]), sub[4]))

            conn.commit()
            print("\nFollowing item is added to your basket:")
            print(sub)
            again = input("Shop again? (y/n)\n-| ")
            if again.lower() == "n":
                customer()
            elif again.lower() == "y":
                shop()
        else:
            input("\nInvalid selection\nPress enter to continue\n")
            shop()
    else:
        input("\nInvalid selection\nPress enter to continue\n")
        shop()


def shopall():
    c.execute('SELECT * FROM productTable')
    data = c.fetchall()
    for row in data:
        print(row)
    id = int(input("Select an ID from 3rd row to buy it: "))
    buyID = 'SELECT * FROM productTable WHERE id3 = ?'
    c.execute(buyID, [id])
    basket = c.fetchone()
    c.execute("INSERT INTO basket (listing_id, listing_name, listing_price) "
              "VALUES(?, ?, ?)", (str(basket[0]) + str(basket[1]) + str(basket[2]), str(basket[3]), basket[4]))

    conn.commit()
    print("\nFollowing item is added to your basket:")
    print(basket)
    again = input("\nShop from this list again? (y/n)\n-| ")
    if again.lower() == "n":
        customer()
    elif again.lower() == "y":
        shopall()


def buy():
    c.execute('SELECT sum(listing_price) FROM basket')
    price_sum = c.fetchall()
    print("Bare total price (TL):")
    print(price_sum[0])
    c.execute('SELECT sum(listing_price)*18/100+sum(listing_price) FROM basket')
    price_sum_tax = c.fetchall()
    print("Total price with tax (TL):")
    print(price_sum_tax[0])
    input("Card number: ")
    input("Valid Thru:  ")
    input("CVC2: ")
    input("Address: ")
    c.execute("DELETE FROM basket")

    conn.commit()
    print("\nCongratulations! We have your order.\n"
          "It'll be on your address within 1 week based on your location.\n")
    input("\nPress enter to continue...\n")
    customer()


def admin():
    print("This is your admin panel. You can add new products here.\n"
          "1) List all products and add new one\n2) Remove a product\n3) Logout")
    selection = int(input("-| "))
    if selection == 1:
        admin_add()
    if selection == 2:
        admin_remove()
    if selection == 3:
        welcome()
    else:
        input("\nPress enter to continue...\n")
        admin()


def admin_add():
    c.execute('SELECT * FROM productTable')
    data = c.fetchall()
    for row in data:
        print(row)
    product_id1 = int(input("Main ID: "))
    product_id2 = int(input("Sub ID:  "))
    product_id3 = int(input("Product ID: "))
    product_name = input("Product Name: ")
    product_price = int(input("Product Price: "))
    c.execute("INSERT INTO productTable (id1, id2, id3, productName, productPrice) "
              "VALUES(?, ?, ?, ?, ?)",
              (product_id1, product_id2, product_id3, str(product_name), product_price))

    conn.commit()


def admin_remove():
    c.execute('SELECT * FROM productTable')
    data = c.fetchall()
    for row in data:
        print(row)
    delete_id = str(input("Select a product ID (3rd row) to delete\n-| "))
    c.execute('DELETE FROM productTable WHERE id3 = ?', (str(delete_id),))


welcome()
