import sqlite3

def select_all_products():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select name,price from Product where ProductID=?",(id,))
        product = cursor.fetchone()
        return product
if __name__ == "__main__":
    products = select_all_products()
    print(products)
    product = select_product(5)
    print(product)
