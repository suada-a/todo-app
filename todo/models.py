from todo import db

class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(length=100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.description}'