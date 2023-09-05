from app import app, db, User

# Create a new user
new_user = User(name='John Doe', email='john@example.com')
db.session.add(new_user)
db.session.commit()

# Read a user
user = User.query.filter_by(name='John Doe').first()
print(f'User: {user.name}, Email: {user.email}')

# Update a user
user.name = 'Noel Loise'
db.session.commit()

# Delete a user
db.session.delete(user)
db.session.commit()
