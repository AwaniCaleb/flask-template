# Professional Flask Template

A robust, production-ready Flask application template built with the Application Factory pattern. This repository is designed to be the perfect starting point for your next "Jinja-rendered" web application.

## 🚀 How to Use This Template

You do not need to clone this repository manually to start a new project! 

Click the green **"Use this template"** button at the top of this repository to generate a fresh repository with this exact structure. 
For more details, see the official GitHub documentation: [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## 📚 Documentation & Walkthroughs

Want to know how this template works under the hood? Need to know how to add new features, customize the database, or create new routes?

**👉 [Check out the Project Wiki](https://github.com/AwaniCaleb/flask-template/wiki)**

The Wiki includes detailed guides on:
* Project Architecture & Directory Structure
* How to add a new Blueprint
* Managing the Database with Flask-Migrate
* Understanding the Custom Security Decorators

## Getting Started (Local Development)
If you are developing locally, follow these steps to get your environment running...

### 1. Clone the repository
```bash
git clone https://github.com/AwaniCaleb/flask-template.git
cd flask-template
```
### 2. Set up a virtual environment
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```
#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the example environment file and rename it to `.env`
```bash
cp .env.example .env
```
Open `.env` and update the `SECRET_KEY` with a secure, random string

### 5. Set up the Database
```bash
flask db upgrade
```

### 6. Run the Application
Start the Flask development server:
```bash
flask run
```
Open your browser and navigate to `http://127.0.0.1:5000`.
