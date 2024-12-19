# TradeHub CLI
TradeHub is a command line interface(CLI) apllication designed to manage Users, Products and Orders within a trading hub environment.

## Features
- **User Management:** add,list,delete and search users by email

- **Product Management:** add,list,delete and serch Products

- **Order Management:** create, list and manage orders

- **data persistance:** use sqlite database(trade_hub.db) for data storage

## Technologies and dependencies used
1. python

2. sqlite database

3. sqlalchemy

4. alembic 

5. click

## Project structure
```bash
tradehub-cli/
├── lib/
│   ├── models.py
│   └── cli.py
├── tradehub.py
├── README.md
└── trade_hub.db
```       


## SetUp instructions
clone this repository

install dependencies
``` bash
pipenv install
pipenv shell
pipenv install sqlalchemy lambda click
```
to run my CLI
``` bash
python lib/cli.py
```
## Author Name
JOYCE WAMOCHO
