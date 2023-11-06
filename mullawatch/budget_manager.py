from mullawatch import models

class BudgetManager:
    def create_budget(self, category_id, amount, start_date, end_date):
        budget = models.Budget(category_id=category_id, amount=amount, start_date=start_date, end_date=end_date)

        db.session.add(budget)
        db.session.commit()

        return budget

    def get_budget_by_id(self, budget_id):
        budget = models.Budget.query.get(budget_id)

        return budget

    def get_all_budgets(self):
        budgets = models.Budget.query.get(budget_id)

        return budgets

    def update_budget(self, budget, category_id, amount, start_date, end_date):