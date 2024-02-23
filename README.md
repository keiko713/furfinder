## FurFinder

Find furs! 🐕🐈

### Development

```bash
# Create and activate venv
python -m venv .venv
. .venv/bin/activate

# Install Flask and SQLAlchemy
pip install Flask
pip install Flask-SQLAlchemy

# Run app
flask --app app run
```

### Usage

```bash
# Get list of pets
curl http://127.0.0.1:5000/pets

# Add a new pet
curl -X POST -H 'Content-Type: application/json' \
--data '{"name":"shiro","kind":"dog","color":"white","age":3}' \
http://127.0.0.1:5000/pets
```
