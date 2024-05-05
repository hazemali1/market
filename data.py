from main import db
from main import app
from main import databasecls


def create_tables():
    with app.app_context():
        db.create_all()

def addobj():
    with app.app_context():
        obj1 = databasecls(name="phone", price=500, description="This is a greatest phone you can ever know 'it's lie :)'")
        obj2 = databasecls(name="labtop", price=1000, description="This is a greatest labtop you can ever know 'it's lie :)'")
        obj3 = databasecls(name="PC", price=2500, description="This is a greatest PC you can ever know 'it's lie :)'")
        obj4 = databasecls(name="headphone", price=150, description="This is a greatest headphone you can ever know 'it's lie :)'")

        db.session.add(obj1)
        db.session.add(obj2)
        db.session.add(obj3)
        db.session.add(obj4)

        db.session.commit()

if __name__ == '__main__':
    # create_tables()
    addobj()
