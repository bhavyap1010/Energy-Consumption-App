from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appliances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Needed for flashing messages
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class ApplianceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appliance_name = db.Column(db.String(50), nullable=False)
    hours_of_use = db.Column(db.Float, nullable=False)
    wattage = db.Column(db.Float, nullable=False)
    energy_consumption = db.Column(db.Float, nullable=False)
    sustainability_tip = db.Column(db.String(200), nullable=True)
    points_earned = db.Column(db.Integer, default=0)  # New column for points

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            appliance_name = request.form['appliance_name']
            hours_of_use = float(request.form['hours_of_use'])
            wattage = float(request.form['wattage'])
            energy_consumption = round(hours_of_use * (wattage / 1000), 2)  # kWh calculation
            sustainability_tip = request.form.get('sustainability_tip', None)

            # Calculate points: 1 point per kWh saved
            points_earned = int(energy_consumption * 1)  # Example calculation

            new_log = ApplianceLog(appliance_name=appliance_name, 
                                    hours_of_use=hours_of_use, 
                                    wattage=wattage, 
                                    energy_consumption=energy_consumption, 
                                    sustainability_tip=sustainability_tip,
                                    points_earned=points_earned)
            db.session.add(new_log)
            db.session.commit()
            flash(f'Success! You earned {points_earned} points.', 'success')
            return redirect(url_for('logs'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/logs')
def logs():
    logs = ApplianceLog.query.all()
    
    # Prepare data for visualization
    appliance_names = [log.appliance_name for log in logs]
    energy_consumptions = [log.energy_consumption for log in logs]
    
    # Update the total points calculation to handle None values
    total_points = sum(log.points_earned if log.points_earned is not None else 0 for log in logs)  # Total points

    return render_template('logs.html', logs=logs, appliance_names=appliance_names, 
                           energy_consumptions=energy_consumptions, total_points=total_points)

@app.route('/clear_logs', methods=['POST'])
def clear_logs():
    db.session.query(ApplianceLog).delete()  # Delete all records from the table
    db.session.commit()
    flash('All logs cleared successfully!', 'success')
    return redirect(url_for('logs'))  # Redirect to the logs page

if __name__ == '__main__':
    with app.app_context():  # Wrap the database creation in the application context
        db.create_all()  # Create the database tables
    app.run(debug=True)