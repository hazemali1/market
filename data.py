from app import db
from app import app
from classes import databasecls
from classes import User


def create_tables():
    with app.app_context():
        db.create_all()

def drop_tables():
    with app.app_context():
        db.drop_all()

def addobj():
    with app.app_context():
        obj1 = databasecls(name="phone", price=500, description="This is a greatest phone you can ever know 'it's lie :)'")
        obj2 = databasecls(name="labtop", price=1000, description="This is a greatest labtop you can ever know 'it's lie :)'")
        obj3 = databasecls(name="PC", price=2500, description="This is a greatest PC you can ever know 'it's lie :)'")
        obj4 = databasecls(name="headphone", price=150, description="This is a greatest headphone you can ever know 'it's lie :)'")

        u1 = User(username="zoome", email="hazemali1343@gmail.com", password="123456789")
        u2 = User(username="hazem", email="hazem@gmail.com", password="123456789")


        db.session.add(obj1)
        db.session.add(obj2)
        db.session.add(obj3)
        db.session.add(obj4)

        db.session.add(u1)
        db.session.add(u2)


        db.session.commit()

if __name__ == '__main__':
    # create_tables()
    addobj()
    # drop_tables()
