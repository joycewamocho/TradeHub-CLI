from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Order,Product,User
import click
import time

DATABASE_URL = "sqlite:///trade_hub.db"

engine = create_engine(DATABASE_URL)
Session =sessionmaker(bind=engine)

session =Session()

def init_db():
    Base.metadata.create_all(engine)
    click.echo("database initialized" )
    time.sleep(2)

def get_user_by_id(user_id):
    return session.query(User).filter(User.id == user_id).first()

def get_product_by_id(product_id):
    return session.query(Product).filter(Product.id == product_id).first()

def get_order_by_id(order_id):
    return session.query(Order).filter(Order.id == order_id).first()


class Trade_hub:
    def __init__(self):
        self.running =True

    def run(self):
        while self.running:
            click.clear()
            click.echo("== Welcome to TradeHub==")
            click.echo("1.User Management")
            click.echo("2.Product Management")
            click.echo("3.Order Management")
            click.echo("4.Exit")
            choice=click.prompt("choose an option", type=int)

            if choice ==1:
                self.user_menu()
            elif choice == 2:
                self.product_menu()
            elif choice ==3:
                self.order_menu()
            elif choice==4:
                self.exit()
            else:
                click.echo("Invalid choice,Please try again")
    def exit(self):
        self.running = False
        click.echo("Thank you for using TradeHub,Goodbye!")

    def user_menu(self):
        while True:
            click.echo("== User Management ==")
            click.echo("1.Add User")
            click.echo("2.List all users")
            click.echo("3.Delete User")
            click.echo("4.Find User By Email")
            click.echo("5.Back to Main Menu")
            choice=click.prompt("choose an option", type=int)

            if choice == 1:
                self.add_user()
            elif choice == 2:
                self.list_all_users()
            elif choice == 3:
                self.delete_user()
            elif choice == 4:
                self.find_user_by_email()
            elif choice == 5:
                break
            else:
                click.echo("Invalid Choice,Please try Again")

    def add_user(self):
        name = click.prompt("Enter user name")
        email = click.prompt("Enter user email")
        if session.query(User).filter(User.email==email).first():
            click.echo("Error.Email already exists")
            return
        user =User(name=name,email=email)
        session.add(user)
        session.commit()
        click.echo(f"user '{name}' added successfully")
    def list_all_users(self):
        users =session.query(User).all()
        if not users:
            click.echo("users do not exist")
            return
        for user in users:
            click.echo(f"ID:{user.id}, Name:{user.name},Email:{user.email} ")

    def delete_user(self):
        user_id= click.prompt("Enter user id to delete",type=int)
        user = session.query(User).filter(User.id==user_id).first()

        if user:
            session.delete(user)
            session.commit()
            session.close()
            click.echo("user deleted successfully")
        else:
            click.echo("user not found")

    def find_user_by_email(self):
        user_email = click.prompt("Enter the user email to retrieve their details")
        user= session.query(User).filter(User.email == user_email).first()
        if user:
            click.echo(f"found User ID:{user.id}, Name:{user.name}, Email:{user.email}")
        else:
            click.echo("user not found")


    # product menu
    def product_menu(self):
        while True:
            click.echo("== Product Management ==")
            click.echo("1.Add Product")
            click.echo("2.List all products")
            click.echo("3.Delete Product")
            click.echo("4.Find Product By Name")
            click.echo("5.Back to Main Menu")
            choice=click.prompt("choose an option", type=int)

            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.list_all_products()
            elif choice == 3:
                self.delete_product()
            elif choice == 4:
                self.find_product_by_name()
            elif choice == 5:
                break
            else:
                click.echo("Invalid Choice,Please try Again")

    def add_product(self):
        name = click.prompt("Enter Product name")
        price = click.prompt("Enter Product Price")
        description = click.prompt("Enter Product description")
        image_url = click.prompt("Enter Product image url")
        user_id= click.prompt("Enter user(seller) ID")

        user = get_user_by_id(user_id)
        if not user:
            click.echo("Error:user not found")
            return
        product =Product(name=name,price=price, description =description, image_url=image_url,user_id=user_id)
        session.add(product)
        session.commit()
        click.echo(f"product '{name}' added successfully")
    def list_all_products(self):
        products=session.query(Product).all()
        if not products:
            click.echo("Product do not exist")
            return
        for product in products:
            click.echo(f"ID:{Product.id}, Name:{product.name},Price:{product.price},Description:{product.description}, Image Url:{product.image_url} ")

    def delete_product(self):
        product_id= click.prompt("Enter user id to delete",type=int)
        product = get_product_by_id(product_id)

        if product:
            session.delete(product)
            session.commit()
            session.close()
            click.echo("Product deleted successfully")
        else:
            click.echo("Product not found")

    def find_product_by_name(self):
        product_name = click.prompt("Enter the Product name to retrieve their details")
        product= session.query(Product).filter(Product.name == product_name).first()
        if product:
            click.echo (f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}, Image Url: {product.image_url}")
        else:
            click.echo("Product not found")


    # order menu
    def order_menu(self):
        while True:
            click.echo("=== Order Management ===")
            click.echo("1. Add Order")
            click.echo("2. List All Orders")
            click.echo("3. Delete Order")
            click.echo("4. Back to Main Menu")
            choice = click.prompt("Choose an option", type=int)

            if choice == 1:
                self.add_order()
            elif choice == 2:
                self.list_orders()
            elif choice == 3:
                self.delete_order()
            elif choice == 4:
                break
            else:
                click.echo("Invalid choice. Try again.")

    def add_order(self):
        product_id = click.prompt("Enter Product ID", type=int)
        buyer_id = click.prompt("Enter Buyer ID", type=int)

        if not get_product_by_id(product_id) or not get_user_by_id(buyer_id):
            click.echo("Error: Invalid Product ID or Buyer ID.")
            return
        order = Order(product_id=product_id, buyer_id=buyer_id)
        session.add(order)
        session.commit()
        click.echo("Order added successfully.")

    def list_orders(self):
        orders = session.query(Order).all()
        for order in orders:
            click.echo(f"ID: {order.id}, Product ID: {order.product_id}, Buyer ID: {order.buyer_id}")

    def delete_order(self):
        order_id = click.prompt("Enter Order ID to delete", type=int)
        order = get_order_by_id(order_id)
        if order:
            session.delete(order)
            session.commit()
            click.echo("Order deleted successfully.")
        else:
            click.echo("Order not found.")







if __name__ == "__main__":
    init_db()
    app =Trade_hub()
    app.run()
    

