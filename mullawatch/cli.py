import argparse
import sys

from mullawatch import app

def main():
    parser = argparse.ArgumentParser(description='MullaWatch CLI application')
    parser.add_argument('--init', action='store_true', help='Initialize the database')
    parser.add_argument('--create-user', action='store_true', help='Create a new user account')
    parser.add_argument('--create-account', action='store_true', help='Create a new account')
    parser.add_argument('--create-category', action='store_true', help='Create a new category')
    parser.add_argument('--record-transaction', action='store_true', help='Record a new transaction')
    parser.add_argument('--view-transaction', action='store_true', help='View all transactions')
    parser.add_argument('--generate-report', action='store_true', help='Generate a report on income and expenses')

    args = parser.parse_args()

    if args.init:
        app.run()

    elif args.create-user:
        username = input('Enter username: ')
        email = input('Enter email: ')
        password = input('Enter password: ')

        user = models.User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        print('User account created successfully!')

    elif args.create-account:
        user_id = int(input('Enter user ID: '))
        name = input('Enter account name: ')
        type = input('Enter account type (income/expense): ')
        balance = float(input('Enter account balance: '))

        account = models.Account(user_id=user_id, name=name, type=type, balance=balance)
        db.session.add(account)
        db.session.commit()

        print('Account created successfully!')

    elif args.create-category:
        name = input('Enter category name: ')
        parent_id = int(input('Enter parent category ID (optional): '))

        category = models.Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()

        print('Category created successfully!')

    elif args.record-transaction:
        account_id = int(input('Enter account ID: '))
        category_id = int(input('Enter category ID: '))
        amount = float(input('Enter amount: '))
        date = input('Enter date (YYYY-MM-DD): ')

        transaction = models.Transaction(account_id=account_id, category_id=category_id, amount=amount, date=date)
        db.session.add(transaction)
        db.session.commit()

        print('Transaction recorded successfully!')

    elif arg.view-transactions:
        transactions = models.Transaction.query.all()

        for transaction in transactions:
            print(transaction)

    elif args.generate-report:
        start_date = input('Enter start date (YYYY-MM-DD): ')
        end_date = input('Enter end date (YYYY-MM-DD): ')

        report = models.Transaction.generate_report(start_date, end_date)

        print('Income:')
        print(report['income'])

        print('Expenses:')
        print(report['expenses'])

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()