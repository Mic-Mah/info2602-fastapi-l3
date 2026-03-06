import typer
from app.database import create_db_and_tables, get_session, drop_all
from app.models import User, Todo, Category
from fastapi import Depends
from sqlmodel import select
from sqlalchemy.exc import IntegrityError

cli = typer.Typer()

@cli.command()
def initialize():
    with get_session() as db: # Get a connection to the database
        drop_all() # delete all tables
        create_db_and_tables() #recreate all tables
        
        bob = User(username='bob', email='bob@mail.com') # Create a new user (in memory)
        bob.set_password("bobpass")

        db.add(bob) # Tell the database about this new data
        db.commit() # Tell the database persist the data
        db.refresh(bob) # Update the user (we use this to get the ID from the db)

        new_todo = Todo(text='Wash dishes', user_id=bob.id)

        db.add(new_todo) # Tell the database about this new data
        db.commit() # Tell the database persist the data
        db.refresh(new_todo) # Update the user (we use this to get the ID from the db)

        print("Database Initialized")

@cli.command()
def add_task(username:str, task:str):
    # Task 4.1 code here. Remove the line with "pass" below once completed
    pass

@cli.command()
def toggle_todo(todo_id:int, username:str):
    # Task 4.2 code here. Remove the line with "pass" below once completed
    pass

@cli.command()
def list_todo_categories(todo_id:int, username:str):
    # Task 5.3 code here. Remove the line with "pass" below once completed
    pass

@cli.command()
def create_category(username:str, cat_text:str):        
    # Task 5.4 code here. Remove the line with "pass" below once completed
    pass

@cli.command()
def list_user_categories(username:str):
    # Task 5.5 code here. Remove the line with "pass" below once completed
    pass

@cli.command()
def assign_category_to_todo(username:str, todo_id:int, category_text:str):
    # Task 5.6 code here. Remove the line with "pass" below once completed
    pass
# 11. Conclusion
# Thus concludes your introduction to flask-sqlalchemy. The usage of this library is at the very core of this course.

# You can view a completed version of this lab at the following link

if __name__ == "__main__":
    cli()
