from flask  import render_template
from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from app.models.TechTalent import  TechTalent 

class HomeController:
    def index(self):
        talents = TechTalent()
        talents = talents.query.all() or []
        
        return render_template('frontend/home.html',talents=talents)
        
    def about(self):
        return render_template('frontend/about.html')

    def add_talent(self):
        talent = TechTalent(
            name=request.form['name'],
            background=request.form['background'],
            experience=request.form['experience'],
            education=request.form['education'],
            job_preference=request.form['job_preference'],
            availability=request.form['availability']
        )
        
        db.session.add(talent)
        db.session.commit()
        return redirect('/')