def welcome():
    print("Welcome to Nhmanas' store! You must login or register to see all the goodies!\nType the number of your selection to continue...")
    selection = int(input("1) Register\n2) Login\n-| "))
    if selection == 1:
        register()
    elif selection == 2:
        login()
    else:
        print("Wrong Selection")
        welcome()
def register():
    print("You selected registration")
    reg = open("users.txt", "a")
    username = input("Username: ")
    password = input("Password: ")
    authority= input("Authority level (1 or 2): ")
    name     = input("Name           : ")
    surname  = input("Surname        : ")
    idnum    = input("Identity Number: ")
    reg.write(username + " " + password + " " + authority + " " + name + " " + surname + " " + idnum + "\n")
    reg.close()
    login()
def login():
    print("\nYou're in login section")
    username = input("Username: ")
    password = input("Password: ")
    sonuc = 0
    for line in open("users.txt", "r").readlines():
        info = line.split()
        if username == info[0] and password == info[1]:
            sonuc = 1
            global auth
            auth = info[2]
            if auth == "1":
                print("Customer " + info[3] + ", I'll take you to the marketplace.")
                customer()
            elif auth == "2":
                print("Welcome admin " + info[3] + ".")
                admin()
            else:
                print("Authority level is other than 1 or 2. Call admin to fix it!")
                welcome()
        else:
            sonuc = 0
    if sonuc == 0:
        print("Wrong Username or Password.")
        welcome()
def customer():
    selection = int(input("1) Select a category to list sub-items\n2) List all items\n3) Logout\n-| "))
    if selection == 3:
        welcome()
    elif selection == 2:
        for line in open("productTable.txt.txt", "r").readlines():
            table = line.split()
            print(table[3])
        customer()
    elif selection == 1:
        for line in open("mainTable.txt", "r").readlines():
            table = line.split()
            print(table)
        cat = int(input("Select a category: "))
        if(cat == 1):
            for line in open("subTable.txt", "r").readlines():
                table = line.split()
                if(table[0] == "1"):
                    print(table[1] + " " + table[2])
            subCat = int(input("Select a sub category: "))
            for line in open("productTable.txt.txt", "r").readlines():
                table = line.split()
                if (table[1] == str(subCat)):
                    print(table[2] + " " + table[3])
            item = int(input("Select a item: "))
            for line in open("productTable.txt.txt", "r").readlines():
                table = line.split()
                if (table[2] == str(item)):
                    print(table[0]+table[1]+table[2] + " " + table[3])

        elif(cat == 2):
            for line in open("subTable.txt", "r").readlines():
                table = line.split()
                if(table[0] == "2"):
                    print(table[1] + " " + table[2])
            subCat = int(input("Select a sub category: "))
            for line in open("productTable.txt.txt", "r").readlines():
                table = line.split()
                if (table[1] == str(subCat)):
                    print(table[2] + " " + table[3])
            item = int(input("Select a item: "))
            for line in open("productTable.txt.txt", "r").readlines():
                table = line.split()
                if (table[2] == str(item)):
                    print(table[0]+table[1]+table[2] + " " + table[3])
        elif(cat == 3):
            for line in open("subTable.txt", "r").readlines():
                table = line.split()
                if(table[0] == "3"):
                    print(table[1] + " " + table[2])
            subCat = int(input("Select a sub category: "))
            for line in open("productTable.txt.txt", "r").readlines():
                table = line.split()
                if (table[1] == str(subCat)):
                    print(table[2] + " " + table[3])
            item = int(input("Select a item: "))
            for line in open("productTable.txt.txt", "r").readlines():
                table = line.split()
                if (table[2] == str(item)):
                    print(table[0]+table[1]+table[2] + " " + table[3])

        a = input()
    else:
        print("\nEntered number is other than 1 or 2!\nTRY AGAIN\n")
        customer()
def admin():
    print("\nYou can edit lists here.\nSelect the list that you want to change:")
    selection = int(input("1) Main Category table\n2) Sub Category table\n3) Product list\n4) Logout\n-| "))
    if selection == 1:
        count = 1
        for line in open("mainTable.txt", "r").readlines():
            table = line.split()
            print(table)
            count += 1
        print("You're going to add category to Main table.")
        edit = open("mainTable.txt", "a")
        listNumber = count
        catName = input("Category name: ")
        edit.write(str(listNumber) + " " + catName + "\n")
        edit.close()
    elif selection == 2:
        count = 1
        for line in open("subTable.txt", "r").readlines():
            table = line.split()
            print(table)
            count += 1
        print("You're going to add category to Sub-category table.")
        edit = open("subTable.txt", "a")
        listNumberMain = input("Main category number: ")
        listNumberSub  = count
        catName        = input("Sub-category name   : ")
        edit.write(str(listNumberMain) + " " + str(listNumberSub) + " " + catName + "\n")
        edit.close()
    elif selection == 3:
        count = 1
        for line in open("productTable.txt.txt", "r").readlines():
            table = line.split()
            print(table)
            count += 1
        print("You're going to add category to Product table.")
        edit = open("productTable.txt.txt", "a")
        listNumberMain = input("Main category number: ")
        listNumberSub  = input("Sub-category number : ")
        listNumberPro  = count
        catName = input("Sub-category name   : ")
        edit.write(str(listNumberMain) + " " + str(listNumberSub) + " " + str(listNumberPro) + " " + catName + "\n")
        edit.close()
    elif selection == 4:
        welcome()
    else:
        print("Wrong number selection!\nTRY AGAIN\n")
        admin()
#MAIN STARTS HERE_________________________________________________________________________
import time
import os
import sys
attempt = 3
auth = 0
welcome()