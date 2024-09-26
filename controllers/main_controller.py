from database.db_session import get_session
from database.models import User


class MainController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.session = get_session()
        self.load_user()

    def add_user(self, name, age, email):
        new_user = User(name=name, age=age, email=email)
        self.session.add(new_user)
        self.session.commit()
        self.load_user()

    def del_user(self, item):
        user = self.session.query(User).filter(item.text() == User.id).first()
        self.session.delete(user)
        self.session.commit()
        self.load_user()

    def filter_user(self, ageAt, ageTo, fname, fage):
        user = self.session.query(User)
        if fage:
            user = user.filter(User.age >= ageAt, User.age <= ageTo)
        if fname:
            user = user.order_by(User.name)
        users = user.all()
        self.main_window.display_user(users)

    def load_user(self):
        user = self.session.query(User).all()
        self.main_window.display_user(user)
