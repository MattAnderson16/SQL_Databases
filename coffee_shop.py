import sqlite3

def display_menu():
    print("""Product Table Menu

1. (Re)Create Product Table
2. Add new product
3. Edit existing product
4. Delete existing product
5. Search for products
0. Exit

""")

def get_menu_choice():
    display_menu()
    valid = False
    while not valid:
        menu_choice = input("Please select an option >> ")
        if menu_choice not in [0,1,2,3,4,5]:
            print("Please input a valid option (1-5 or 0 to exit).")
        else:
            valid = True
    return menu_choice

def create_product_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor
        cursor.execute("select name from sqlite_master where name = ?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n) >> ".format(table_name))
            if response == "y":
                keep_table = False
                print("The table {0} will be recreated - all existing data will be lost.".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table will be kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
    
    
