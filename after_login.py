
import db_functions
import os
import password_generator
import masterpass_hash_generator
import crypt_functions
import db_connector
from mysql.connector import cursor
import mysql.connector
import MySQLdb.cursors

#connection = db_connector.db_connection()
#mycursor = connection.cursor(MySQLdb.cursors.DictCursor)

def after_login(acc_id,acc_passwd):
    connection = db_connector.db_connection()
    mycursor = connection.cursor(MySQLdb.cursors.DictCursor)
    #os.system('cls')
    print("\n------------------------")
    print("----Password Manager----")
    print("------------------------")
    print("1) List of all passwords")
    print("2) Add password")
    print("3) Update password")
    print("4) Delete password")
    print("5) Exit")
    
    selection = input("Selection: ")

    if selection == "1":
        query = str(db_functions.select_passwords_db(acc_id))
        mycursor.execute(query)
        passwdDB = mycursor.fetchall()
        if passwdDB:
            for x in passwdDB:
                print("\n***************************************")
                urlPasswd = crypt_functions.decrypt_password(x[1],acc_passwd)
                print("| ",end="")
                print(x[3],end=" | ")
                print(x[4],end=" | ")
                print(str(urlPasswd.decode('utf-8')),end=" |")
            print("\n***************************************")
        after_login(acc_id,acc_passwd)

    elif selection == "2":
        url = input("Enter website name where you want to save your credentials(Google, Udemy etc.): ")
        username = input("Enter your username: ")
        passSelection = input("Do you want to enter the password yourself?(1) Or shall we generate a password for you?(2): ")
        if passSelection == "1":
            password = input("Enter password: ")
            #encrypt function will come right here
            encryptedPassword = crypt_functions.encrypt_password(password,acc_passwd)
            query = str(db_functions.insert_password_db(acc_id,url,username,encryptedPassword))
            mycursor.execute(query)
            connection.commit()
            mycursor.close()
            connection.close()
            after_login(acc_id,acc_passwd)
            
        elif passSelection == "2":
            password = password_generator.password_gen(12)
            print("Please note that. Password: " + str(password))
            #encrypt function will come right here
            encryptedPassword = crypt_functions.encrypt_password(password,acc_passwd)
            query = str(db_functions.insert_password_db(acc_id,url,username,encryptedPassword))
            mycursor.execute(query)
            connection.commit()
            mycursor.close()
            connection.close()
            after_login(acc_id,acc_passwd)

    elif selection == "3":
        url = input("Enter the url of the account where password you want to change: ")
        passSelection = input("Do you want to enter the password yourself?(1) Or shall we generate a password for you?(2): ")
        if passSelection == "1":
            password = input("Enter password: ")
            #encrypt function will come right here
            encryptedPassword = crypt_functions.encrypt_password(password,acc_passwd)
            query = str(db_functions.update_password_db(acc_id,url,encryptedPassword))
            mycursor.execute(query)
            connection.commit()
            mycursor.close()
            connection.close()
            after_login(acc_id,acc_passwd)
            
        elif passSelection == "2":
            password = password_generator.password_gen(12)
            print("Please note that. Password: " + str(password))
            #encrypt function will come right here
            encryptedPassword = crypt_functions.encrypt_password(password,acc_passwd)
            query = str(db_functions.update_password_db(acc_id,url,encryptedPassword))
            mycursor.execute(query)
            connection.commit()
            mycursor.close()
            connection.close()
            after_login(acc_id,acc_passwd)

    elif selection == "4":
        url = input("Enter the url where you want to delete your account records: ")
        query = str(db_functions.delete_password_db(acc_id,url))
        mycursor.execute(query)
        connection.commit()
        mycursor.close()
        connection.close()
        print("Deletion successful.")
        after_login(acc_id,acc_passwd)

    elif selection == "5":
        pass
    else:
        print("Wrong input.")

