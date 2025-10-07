# Django Flight Routes System

## Overview

The **Django Flight Routes System** is a web application to manage and analyze airport routes.  
It allows users to:  

- Add airport routes with **airport code, position, and duration**.  
- Find the **Nth node** in a route (left or right traversal).  
- Identify the **longest route** based on duration.  
- Calculate the **shortest duration** between two airports.  

This project uses **Django, Bootstrap, and Python** for a clean, responsive, and professional web interface.

---

## Technology Stack

- Python 3.12+  
- Django 5.x
- Bootstrap 5 (via CDN)
- SQLite  
---

## Features

1. **Add Airport Route**  
   - Add new routes using a form.  
   - View all existing routes on the same page.  

2. **Find Nth Node**  
   - Input start airport, N, and direction (left/right).  
   - Displays the resulting airport node.  

3. **Longest Route**  
   - Displays the airport route with the **maximum duration**.  

4. **Shortest Duration**  
   - Calculate the **total duration between any two airports**.  

5. **Professional UI**  
   - Bootstrap-styled forms and tables.  
   - Responsive and clean layout.  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Ananthu303/air-route-management.git
cd airport_project
```
### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project. Here’s how to create and activate it:

For **Windows**:
```bash
python -m venv venv

venv\Scripts\activate
```

For **macOS/Linux**:
```bash
python3 -m venv venv

source venv/bin/activate
```

Once activated, your terminal should show something like `(venv)` indicating that the virtual environment is active.

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Apply the database migrations to set up the necessary database schema:

```bash
python manage.py migrate
```

### 5. Create superuser

Run the following command to create the superuser:

```bash
python manage.py createsuperuser
```

You will be prompted to enter the following information:

- Username
- Email
- Password

This superuser have full control over the django admin panel

### 6. Run the Development Server

Once everything is set up, run the Django development server:

```bash
python manage.py runserver
```

Now, you can access the application at `http://127.0.0.1:8000/`.

---
| URL Path            | View Name           | Description                                          |
| ------------------- | ------------------- | ---------------------------------------------------- |
| `/routes/add/`      | `add_airport_route` | Add a new airport route and list existing routes     |
| `/routes/find-nth/` | `find_nth_node`     | Find the Nth node from a given airport               |
| `/routes/longest/`  | `longest_node`      | Display the airport route with the longest duration  |
| `/routes/shortest/` | `shortest_duration` | Calculate the shortest duration between two airports |


## Notes
- The system currently works with a linked-list style route where each airport points to the next.
- Shortest duration calculation works in both directions (forward/backward).
- All forms are Bootstrap-styled for a clean UI.