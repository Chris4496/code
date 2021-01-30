from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.splite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column('room_id', db.Integer, primary_key=True)
    room = db.Column(db.String(80))
    human = db.Column(db.Boolean)

    def __init__(self, room, human):
        self.room = room
        self.human = human


class Count:

    def __init__(self):
        self.items = {}

    # rest of your code here. . .

    def additem(self, room, person):
        self.items[str(room)] = person

    def delitem(self, item):
        del self.items[str(item)]

    def displayinventory(self):
        return self.items


count = Count()


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    content = request.get_json()
    print(content)
    count.additem(str(content['location']), bool(content['human']))

    rom = Room(str(content['location']), bool(content['human']))
    db.session.add(rom)
    db.session.commit()

    return 'JSON posted'


@app.route('/')
def view():
    return render_template('home.html', data=count.displayinventory().items())


@app.route('/db')
def viewDB():
    r = Room.query.filter_by(room='room69').first()
    return f'{r.room}'


@app.route('/<room>')
def viewRoom(room):
    return render_template('room.html', room=room)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
