from database import db

class Tarea(db.Model):
    __tablename__ = "tareas"

    # id, title, descripcion, status, create_at, assigned_to"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    create_at = db.Column(db.String(100), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)

    def __init__(self, title, description, status, create_at, assigned_to):
        self.title = title
        self.description = description
        self.status = status
        self.create_at = create_at
        self.assigned_to = assigned_to

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Tarea.query.all()

    @staticmethod
    def get_by_id(id):
        return Tarea.query.get(id)

    def update(self, title=None, description=None, status=None, create_at=None, assigned_to=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if create_at is not None:
            self.create_at = create_at
        if assigned_to is not None:
            self.assigned_to = assigned_to
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
