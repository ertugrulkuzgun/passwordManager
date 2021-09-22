from mysql.connector import cursor


def insert_db(email,password):
    query1 = "INSERT INTO accounts(email,masterPassword) VALUES ('{}','{}');".format(email,password)
    return query1

def select_db(email,password):
    query2 = "SELECT * FROM accounts WHERE email = '{}' AND masterPassword = '{}'".format(email,password)
    return query2

def insert_password_db(id,url,username,password):
    query3 = "INSERT INTO passwords(acc_id,website,username,passwd) VALUES ({},'{}','{}','{}');".format(id,url,username,password)
    return query3

def select_passwords_db(id):
    query4 = "SELECT * FROM passwords WHERE acc_id={};".format(id)
    return query4

def update_password_db(id,url,password):
    query5 = "UPDATE passwords SET passwd = '{}' WHERE acc_id = {} AND website = '{}';".format(password,id,url)
    return query5

def delete_password_db(id,url):
    query6 = "DELETE FROM passwords WHERE acc_id = {} AND website = '{}';".format(id,url)
    return query6
