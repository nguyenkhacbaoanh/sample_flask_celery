#from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app

from app.apis import blueprint


manager = Manager(app)

def routes():
    'Display registered routes'
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))
    return rules

@manager.command
def run():
    print(routes())
    app.register_blueprint(blueprint, url_prefix='')
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == '__main__':
    manager.run()