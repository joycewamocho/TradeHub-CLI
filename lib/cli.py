from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Order,Product,User
import click

DATABASE_URL = "sqlite:///trade_hub.db"

engine = create_engine(DATABASE_URL)
Session =sessionmaker(bind=engine)

session =Session()

def init_db():
    Base.metadata.create_all(engine)
    click.echo("database initialized")

class Trade_hub:
    def __init__(self):
        self.running =True

    def run(self):
        while self.running:
            click.clear()
            click.echo("== Welcome to TradeHub")
            click.echo("1. User Management")
            click.echo("2.Product Management")
            click.echo("3.Order Management")
            click.echo("4.Exit")
            choice=click.prompt("choose an option", type=int)

            if choice ==1:
                self.user_menu()
            elif choice == 2:
                self.product_menu()
            elif choice ==3:
                self.product_menu()
            elif choice==4:
                self.exit()
            else:
                click.echo("Invalid choice,Please try again")
    def exit(self):
        self.running = False
        click.echo("Thank you for using TradeHub,Goodbye!")

    def user_menu(self):
        while True:
            click.clear()
            click.echo("== User Management ==")
            click.echo("1. Add User")
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


if __name__ == "__main__":
    init_db()
    app =Trade_hub()
    app.run()
    

