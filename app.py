from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
from sqlalchemy.dialects.postgresql import JSONB
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS globally

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(JSONB, nullable=False)  # Use JSONB for list of strings
    image = db.Column(db.String(255), nullable=False)
    repository_link = db.Column(db.String(255), nullable=True)
    demo_link = db.Column(db.String(255), nullable=True)

admin = Admin(app, name="Portfolio Admin", template_mode="bootstrap4")
admin.add_view(ModelView(Project, db.session))  # Full CRUD via admin panel

with app.app_context():
    db.create_all()

def project_to_dict(p):
    return {
        "id": p.id,
        "title": p.title,
        "description": p.description,
        "technologies": p.technologies,
        "image": p.image,
        "repositoryLink": p.repository_link,
        "demoLink": p.demo_link
    }

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Portfolio API!"})

@app.route('/projects')
def get_projects():
    projects = Project.query.all()
    return jsonify([project_to_dict(p) for p in projects])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
