# 🚀 Portfolio Backend (Flask + PostgreSQL)

A simple and powerful Portfolio Backend API built with **Flask**, **PostgreSQL**, and **Flask-Admin**.
This API allows you to manage portfolio projects through an admin dashboard and expose them via REST endpoints.

---

## ✨ Features

* 🗂️ Full CRUD operations via **Flask-Admin**
* 📦 PostgreSQL database with JSONB support
* 🌍 Public API endpoint to fetch projects
* 🔐 Environment variable configuration using `.env`
* 🔄 CORS enabled for frontend integration
* 🚀 Ready for deployment (Render, Railway, Heroku, etc.)

---

## 🛠️ Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Admin
* Flask-CORS
* PostgreSQL
* SQLAlchemy
* python-dotenv

---

## 📁 Project Structure

```
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_database
SECRET_KEY=your_secret_key_here
PORT=8000
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Server will run on:

```
http://localhost:8000
```

---

## 📡 API Endpoints

### 🏠 Home

```
GET /
```

Response:

```json
{
  "message": "Welcome to the Portfolio API!"
}
```

---

### 📂 Get All Projects

```
GET /projects
```

Response:

```json
[
  {
    "id": 1,
    "title": "My Project",
    "description": "Project description",
    "technologies": ["Flask", "PostgreSQL"],
    "image": "image_url",
    "repositoryLink": "https://github.com/...",
    "demoLink": "https://demo.com"
  }
]
```

---

## 🛡️ Admin Panel

Flask-Admin provides a full CRUD interface.

After running the server, visit:

```
http://localhost:8000/admin
```

You can:

* ➕ Add projects
* ✏️ Edit projects
* ❌ Delete projects
* 📋 View all entries

---

## 🗄️ Database Model

### Project Model

| Field           | Type    | Description                 |
| --------------- | ------- | --------------------------- |
| id              | Integer | Primary key                 |
| title           | String  | Project title               |
| description     | Text    | Project description         |
| technologies    | JSONB   | List of technologies used   |
| image           | String  | Image URL                   |
| repository_link | String  | GitHub repo link (optional) |
| demo_link       | String  | Live demo link (optional)   |

---

## 🚀 Deployment

You can deploy this API on:

* Render
* Railway
* Heroku
* VPS (DigitalOcean, AWS, etc.)

Make sure to:

* Set environment variables
* Use a production-ready PostgreSQL database
* Set a strong `SECRET_KEY`

---

## 📌 Example requirements.txt

```txt
Flask
Flask-SQLAlchemy
Flask-Admin
Flask-CORS
psycopg2-binary
python-dotenv
```

---

## 📜 License

This project is open-source and available under the MIT License.

---
[Frontend Link](https://github.com/San2021331091/portfolio/blob/main/README.md)


