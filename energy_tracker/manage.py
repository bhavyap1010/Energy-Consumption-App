from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db  # Make sure your app and db are imported correctly

migrate = Migrate(app, db)
manager = Manager(app)

# Add the migrate command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()