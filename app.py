from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///furfinder.db"
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    kind = db.Column(db.String(80))
    color = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'<Fur {self.name}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'kind': self.kind,
            'color': self.color,
            'age': self.age
        }

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pets", methods=["POST"])
def pet_create():
    data = request.get_json()
    pet = Pet(
        name=data.get('name'),
        kind=data.get('kind'),
        color=data.get('color'),
        age=data.get('age'),
    )
    db.session.add(pet)
    db.session.commit()
    return jsonify(pet.serialize), 201

@app.route("/pets", methods=["GET"])
def pet_list():
    pets = db.session.execute(db.select(Pet)).scalars()
    return jsonify([p.serialize for p in pets])

if __name__ == '__main__':
    app.run(debug=True)
