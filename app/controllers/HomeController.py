from flask  import render_template

class HomeController:
    def home(self):
        return render_template('frontend/home.html')
    
    def about(self):
        return render_template('frontend/about.html')