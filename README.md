# Energy Consumption Tracker

This project is an Energy Consumption Tracker web application that allows users to log the energy usage of their appliances. Users can input the appliance name, hours of use, and wattage to calculate energy consumption in kilowatt-hours (kWh). The application features gamification elements, including user levels based on total energy consumption, and a dark mode toggle for enhanced user experience.

## About

This project was created for Hack the Valley 9, my first hackathon. It serves as a practical tool for individuals looking to track and understand their energy consumption better. 

## Features

- User-friendly interface for logging appliance energy usage
- Automatic calculation of energy consumption based on user input
- Gamification elements that display user levels based on total energy consumption
- Achievements that users can earn based on their energy-saving behaviors
- Option to toggle dark mode for better visibility
- Data visualization of logged energy consumption using charts
- Show/hide logs functionality to manage viewing preferences

## Technologies Used

- **Flask**: Web framework for building the application
- **SQLite**: Lightweight database for storing logs
- **HTML/CSS**: Frontend design and layout
- **JavaScript**: For form validation, dark mode toggle functionality, and dynamic updates to user score and achievements
- **Chart.js**: Library for data visualization in charts
- **Bootstrap**: CSS framework for responsive design

## Installation

1. Clone the repository:

   ```git clone https://github.com/yourusername/energy-consumption-tracker.git```

2. Navigate to the project directory:

   ```cd energy-consumption-tracker```

3. Create a virtual environment (optional but recommended):

   ```python -m venv venv```

4. Activate the virtual environment:

   - On Windows:
     ```venv\Scripts\activate```
   - On macOS/Linux:
     ```source venv/bin/activate```

5. Install the required packages:

   ```pip install Flask Flask-SQLAlchemy```

6. Run the application:

   ```python app.py```

## Usage

- On the homepage, enter the appliance name, hours of use, and wattage, then click "Submit" to log the data.
- View the logged entries by navigating to the "Logs" page.
- Clear all logs using the "Clear Logs" button on the logs page.
- Toggle dark mode for enhanced visibility.
- Track achievements and user scores based on energy consumption.

## Contributing

Feel free to fork the repository and make contributions. If you find any issues or have suggestions, please open an issue.

## Acknowledgements

- Special thanks to the Hack the Valley 9 organizers and participants for an incredible experience!
