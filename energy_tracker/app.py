from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appliances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ApplianceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_name = db.Column(db.String(50), nullable=False)
    hours_of_use = db.Column(db.Float, nullable=False)
    wattage = db.Column(db.Float, nullable=False)
    energy_consumption = db.Column(db.Float, nullable=False)
    sustainability_tip = db.Column(db.String(200), nullable=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            appliance_name = request.form['appliance_name']
            hours_of_use = request.form['hours_of_use']
            wattage = request.form['wattage']
            energy_consumption = round(float(hours_of_use) * (float(wattage) / 1000), 2)  # kWh calculation
            sustainability_tip = request.form.get('sustainability_tip', None)

            new_log = ApplianceLog(appliance_name=appliance_name, 
                                    hours_of_use=hours_of_use, 
                                    wattage=wattage, 
                                    energy_consumption=energy_consumption, 
                                    sustainability_tip=sustainability_tip)
            db.session.add(new_log)
            db.session.commit()
            return redirect(url_for('logs'))
        except Exception as e:
            db.session.rollback()
            return str(e), 500
    
    return render_template('index.html')

@app.route('/logs')
def logs():
    logs = ApplianceLog.query.all()
    return render_template('logs.html', logs=logs)

@app.route('/clear_logs', methods=['POST'])
def clear_logs():
    db.session.query(ApplianceLog).delete()  # Delete all records from the table
    db.session.commit()
    return redirect(url_for('logs'))  # Redirect to the logs page

if __name__ == '__main__':
    with app.app_context():  # Wrap the database creation in the application context
        db.create_all()  # Create the database tables
    app.run(debug=True)