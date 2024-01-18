from taskmanager import db


class Catagory(db.Model):
    # Schema for catagory model
    id = db.Column(db.Integer,primary_key=True)
    catagory_name = db.column(db.String(25))
    tasks = db.relationship("Task", backref="catagory", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.catagory_name


class Task(db.Model):
    # Schema for the Task Model
    id = db.Column(db.Integer,primary_key=True)
    task_name = db.Column(db.String(50), nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    catagory_id = db.Column(db.Integer, db.ForeignKey("catagory.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"#{self.id} - Task: {self.task_name} | Urgent:{self.is_urgent}"
