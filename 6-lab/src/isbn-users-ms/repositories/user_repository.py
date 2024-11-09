from models.user import User, db

class UserRepository:

    @staticmethod
    def create_user_repository(name, email):

        user = User(name=name, email=email)
        
        db.session.add(user)
        db.session.commit()

        return user