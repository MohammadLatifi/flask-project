from extensions import db

class TechTalent(db.Model):
    __tablename__ = 'tech_talent'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    background = db.Column(db.String(100))
    experience = db.Column(db.String(100))
    education = db.Column(db.String(100))
    job_preference = db.Column(db.String(300))
    availability = db.Column(db.String(300))

    