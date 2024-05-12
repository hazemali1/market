from app import db, bcrypt

class databasecls(db.Model):
    id = db.Column(db.Integer() , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer() , primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('databasecls', backref='owned_user', lazy=True)

    @property
    def password_hash(self):
        return self.password_hash

    @password_hash.setter
    def password_hash(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
