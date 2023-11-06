from mullawatch import models

class UserManager:
    def create_user(self, username, email, password):
        user = models.User(username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return user

    def get_user_by_id(self, user_id):
        user = models.User.query.get(user_id)

        return user

    def get_all_users(self):
        users = models.User.query.all()

        return users

    def update_user(self, user, username, email, password):
        user.username = username
        user.email = email
        user.password = password

        db.session.commit()

        def delete_user(self, user):
            db.session.delete(user)
            db.session.commit()

