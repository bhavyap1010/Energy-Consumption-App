from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_consumption.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ApplianceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_name = db.Column(db.String(100), nullable=False)
    hours_of_use = db.Column(db.Float, nullable=False)
    wattage = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    appliance_name = request.form['appliance_name']
    hours_of_use = request.form['hours_of_use']
    wattage = request.form['wattage']
    
    new_log = ApplianceLog(appliance_name=appliance_name, hours_of_use=hours_of_use, wattage=wattage)
    db.session.add(new_log)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():  # Ensure this is inside the application context
        db.create_all()  # Create database tables
    app.run(debug=True)