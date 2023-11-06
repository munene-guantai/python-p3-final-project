from mullawatch import models

def generate_report(start_date, end_date):

    transactions = models.Transaction.query.filter(models.Transaction.date >= start_date, models.Transaction.date <= end_date).all()

    income = 0
    expenses = 0
    for transaction in transactions:
        if transaction.account.type == models.Account.TYPE_INCOME:
            income += transaction.amount
        else:
            expenses += transaction.amount


    return {
        'income': income,
        'expenses': expenses,
    }