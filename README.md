📌 Django Post App

A simple blog-style Post application built with Django using Django Templates for rendering views. This project demonstrates basic CRUD functionality with server-side rendering.
[http://](http://149.28.123.143/)
========================================================================
🚀 Features

Create posts
View all posts
View single post detail
Update posts
Delete posts
Pagination
Filter by categories, content and title

Django Templates for frontend rendering
SQLite database (default)
========================================================================
🛠️ Tech Stack

Python

Django

HTML (Django Templates)

SQLite (default Django DB)
========================================================================
⚙️ Installation & Setup
1️⃣ Clone the repository
        git clone https://github.com/Swc19-code/Post-app.git
cd django-post-app
2️⃣ Create virtual environment
         python -m venv venv

Activate it:

Windows
        venv\Scripts\activate

Mac/Linux
        source venv/bin/activate
        
3️⃣ Install dependencies
pip install -r requirements.txt


4️⃣ Apply migrations
python manage.py migrate
5️⃣ Run the server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
========================================================================
🧱 Model Example
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

========================================================================

📄 License

This project is open-source and available under the MIT License.
