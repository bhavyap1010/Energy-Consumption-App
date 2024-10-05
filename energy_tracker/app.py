from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy.db'
db = SQLAlchemy(app)

class ApplianceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_name = db.Column(db.String(100), nullable=False)
    hours_of_use = db.Column(db.Float, nullable=False)
    wattage = db.Column(db.Float, nullable=False)
    date_logged = db.Column(db.Date, nullable=False)  # Date field

    def __repr__(self):
        return f"ApplianceLog('{self.appliance_name}', '{self.hours_of_use}', '{self.wattage}', '{self.date_logged}')"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    appliance_name = request.form['appliance_name']
    hours_of_use = float(request.form['hours_of_use'])
    wattage = float(request.form['wattage'])
    
    # Convert the date from string to datetime object
    date_logged_str = request.form['date_logged']
    date_logged = datetime.strptime(date_logged_str, '%Y-%m-%d').date()  # Convert to Python date object

    # Create a new ApplianceLog entry
    new_log = ApplianceLog(appliance_name=appliance_name, hours_of_use=hours_of_use, wattage=wattage, date_logged=date_logged)

    try:
        db.session.add(new_log)
        db.session.commit()
        return "Log submitted successfully!"
    except Exception as e:
        db.session.rollback()  # Rollback if there's an error
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)