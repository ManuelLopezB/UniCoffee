from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskblog import create_app, db

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
