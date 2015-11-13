#!/usr/bin/env python
from portal import app
import sys

def main():
    valid_actions = {'db.create','db.migrate','run'}
    action = sys.argv[1]
    if action == 'run': run()
    elif action == 'db.create':
        from cli import db
        db.create_db()
    elif action == 'db.migrate':
        from cli import db
        db.migrate()


def run():
    app.run(debug = True)

if __name__ == "__main__":
    main()