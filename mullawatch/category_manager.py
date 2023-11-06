from mullawatch import models

class CategoryManager:
    def create_category(self, name, parent_id):
        category = models.Category(name=name, parent_id=parent_id)

        db.session.add(category)
        db.session.commit()

        return category

    def get_category_by_id(self, category_id):
        category = models.Category.query.get(category_id)

        return category

    def get_all_categories(self):
        categories = models.Category.query.all()

        return categories

    def update_category(self, category, name, parent_id):
        category.name = name
        category.parent_id parent_id

        db.session.commit()

    def delete_category(self, category):
        db.session.delete(category)
        db.session.commit()