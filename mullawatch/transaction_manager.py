from mullawatch import models

class TransactionManager:
    def record_transaction(self, account_id, category_id, amount, date):
        transaction = models.Transaction(account_id=account_id, category_id=category_id, amount=amount, date=date)

        db.session.add(transaction)
        db.session.commit()

        return transaction

    def get_transaction_by_id(self, transaction_id):
        transaction = models.Transaction.query.get(transaction_id)

        return transactions

    def get_all_transactions(self):
        transactions = models.Transaction.query.all()

        return transactions

    def update_transaction(self, transaction, account_id, category_id, amount, date):
        transaction.account_id = account_id
        transaction.category_id = category_id
        transaction.amount = amount
        transaction.date = date

        db.session.commit()

    def delete_transction(self, transaction):
        db.session.delete(transaction)
        db.session.commit()
        