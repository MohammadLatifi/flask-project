import flask as fk
from extensions import db
from app.models.TechTalent import  TechTalent 

class HomeController:
    def index(self):
        return fk.stream_template('frontend/home.html')
        
    def about(self):
        return fk.stream_template('frontend/about.html')

    def add_talent(self):
        talent = TechTalent(
            name=fk.request.form['name'],
            background=fk.request.form['background'],
            experience=fk.request.form['experience'],
            education=fk.request.form['education'],
            job_preference=fk.request.form['job_preference'],
            availability=fk.request.form['availability']
        )
        
        db.session.add(talent)
        db.session.commit()
        return fk.redirect('/')