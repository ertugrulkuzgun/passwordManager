from mysql.connector import cursor
import db_connector
import masterpass_hash_generator
import db_functions
from hashlib import sha256
import hashlib
import mysql.connector
import MySQLdb.cursors
import password_generator
import os
from after_login import after_login
import sys

connection = db_connector.db_connection()
mycursor = connection.cursor(MySQLdb.cursors.DictCursor)

def menu():
    print("------------------------")
    print("----Password Manager----")
    print("------------------------")
    print("1) Log in to your exist account: ")
    print("2) Create account: ")
    print("3) Exit: ")
    selection = str(input("Selection: "))

    if(selection == "1"):
        email1 = input("E-mail address: ")
        password1 = input("Password: ")
        masterPass1 = masterpass_hash_generator.master_password_gen(password1)
        query1 = str(db_functions.select_db(email1,masterPass1))
        mycursor.execute(query1)
        account = mycursor.fetchall()
        if account:
            for x in account:
                #print(x)
                accountID = x[0]
                accountEmail = x[1]
                accountPassword = x[2]
            #print(accountID)
            print("\nWelcome {}".format(accountEmail))
            after_login(accountID,accountPassword)
        else:
            print("Wrong credentials.")

    elif(selection == "2"):
        email = input("E-mail Address: ")
        passSelection = str(input("Do you want to enter the password yourself?(1) Or shall we generate a password for you?(2): "))
        if passSelection == "1":
            password = input("Password: ")
            #encryption function must be found in here
            masterPass = masterpass_hash_generator.master_password_gen(password)
            print("Master Password: " + str(masterPass))
            #then encrypted password and email will send to the database
            query = str(db_functions.insert_db(email,masterPass))
            mycursor.execute(query)
            connection.commit()
            mycursor.close()
            connection.close()
            os.system('cls')
            menu()

        elif passSelection == "2":
            #random password generator will come here
            password = password_generator.password_gen(10)
            print("Please note that. Password: " + str(password))
            #then random password generator function's return value will send to the master password generator
            masterPass = masterpass_hash_generator.master_password_gen(password)
            print("Master Password: " + str(masterPass))
            query = str(db_functions.insert_db(email,masterPass))
            mycursor.execute(query)
            connection.commit()
            mycursor.close()
            connection.close
            os.system('cls')
            menu()
            
        else:
            print("Wrong input.")
            menu()

    elif selection == "3":
        sys.exit()

    else:
        print("Wrong input.")
        menu()

menu()

