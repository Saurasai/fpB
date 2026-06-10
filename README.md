# FastAPI Blog Application

A lightweight blog application built with FastAPI that combines server-side rendering with REST API endpoints. This project demonstrates modern web development practices using Python's fastest web framework.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Project Files](#project-files)
- [Technologies Used](#technologies-used)

## Overview

This FastAPI Blog is a full-stack web application that serves blog posts through both traditional HTML templates and REST API endpoints. It demonstrates core FastAPI concepts including static file serving, template rendering, and API design.

## Features

- **Blog Post Display**: View a collection of blog posts on the home page
- **Server-Side Rendering**: Uses Jinja2 templates for dynamic HTML generation
- **REST API**: Dedicated `/api/posts` endpoint for programmatic access to posts
- **Static File Serving**: Efficiently serves CSS, JavaScript, images, and icons
- **Responsive Design**: Bootstrap-based responsive UI that works on all devices
- **Progressive Web App Support**: Includes web manifest and icon configuration
- **SEO Optimized**: Open Graph meta tags for social media sharing

## Project Structure

```
fastapi/
├── main.py                 # FastAPI application (primary app)
├── test.py                 # Test endpoint (experimental)
├── ll.py                   # Teams status automation script
├── README.md               # This file
├── static/                 # Static files directory
│   ├── css/
│   │   └── main.css       # Main stylesheet
│   ├── js/
│   │   └── utils.js       # Utility JavaScript functions
│   ├── icons/             # Application icons (favicon, etc.)
│   ├── profile_pics/      # User profile picture storage
│   └── site.webmanifest   # PWA manifest file
└── templates/              # Jinja2 HTML templates
    ├── layout.html        # Base template with navbar and structure
    └── home.html          # Home page template (extends layout.html)
```

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**:
   ```bash
   cd c:\Users\Lenovo\Documents\fastapi
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

3. **Install required dependencies**:
   ```bash
   pip install fastapi uvicorn python-multipart
   ```

   Optional dependencies:
   ```bash
   pip install pyautogui  # For ll.py Teams status automation
   ```

## Running the Application

### Start the FastAPI Server

```bash
uvicorn main:app --reload
```

- The application will be available at `http://localhost:8000`
- The `--reload` flag enables auto-restart on code changes
- API documentation available at `http://localhost:8000/docs`
- Alternative documentation at `http://localhost:8000/redoc`

### Access the Application

- **Home Page**: `http://localhost:8000/` or `http://localhost:8000/posts`
- **Blog Posts via API**: `http://localhost:8000/api/posts`
- **Interactive Docs**: `http://localhost:8000/docs`

## API Endpoints

### Home Page
- **GET** `/` - Renders home page with blog posts (HTML)
- **GET** `/posts` - Renders home page with blog posts (HTML)

**Response Type**: HTML template
**Parameters**: None
**Query Parameters**: None

### Blog Posts API
- **GET** `/api/posts` - Returns all blog posts as JSON

**Response Type**: JSON
**Status Code**: 200 OK
**Response Format**:
```json
[
  {
    "id": 1,
    "author": "Corey Schafer",
    "title": "FastAPI is Awesome",
    "content": "This framework is really easy to use and super fast.",
    "date_posted": "April 20, 2025"
  },
  {
    "id": 2,
    "author": "Jane Doe",
    "title": "Python is Great for Web Development",
    "content": "Python is a great language for web development, and FastAPI makes it even better.",
    "date_posted": "April 21, 2025"
  }
]
```

## Project Files

### [main.py](main.py)
**Primary FastAPI Application**

The main application file containing:
- FastAPI app initialization
- Static file mounting configuration
- Jinja2 template configuration
- In-memory post data storage
- Route handlers for home page and API

Key Components:
- `posts`: List of blog post dictionaries
- `/` & `/posts` routes: Server-side rendered home page
- `/api/posts` route: JSON API endpoint

### [test.py](test.py)
**Testing/Experimental File**

A basic FastAPI test endpoint (`/home`) that returns "hello world". This file appears to be for testing purposes and can be used for development experimentation.

### [ll.py](ll.py)
**Teams Status Automation**

A utility script that keeps Microsoft Teams status active by:
- Simulating mouse movements every 60 seconds
- Preventing idle status on Teams
- Running in an infinite loop

**Usage**: Run separately from the main application
```bash
python ll.py
```

**Note**: Requires `pyautogui` package

### [templates/layout.html](templates/layout.html)
**Base Template (Master Layout)**

The main HTML template providing:
- Document structure with semantic HTML5
- Bootstrap 5.3.8 integration for responsive design
- Navbar with navigation links
- Meta tags for SEO and Open Graph sharing
- CSS and JavaScript resource linking
- PWA (Progressive Web App) support
- Custom fonts from Google Fonts (Montserrat & Nunito)
- Dark-themed navigation bar

### [templates/home.html](templates/home.html)
**Home Page Template**

Displays blog posts with:
- Post author information
- Profile pictures (circular images)
- Post titles (as links)
- Post publication dates
- Post content preview
- Bootstrap utility classes for responsive layout

### [static/css/main.css](static/css/main.css)
**Main Stylesheet**

Contains custom styling for:
- Blog post styling
- Color scheme and theme
- Typography
- Layout adjustments
- Component-specific styles

### [static/js/utils.js](static/js/utils.js)
**Utility JavaScript Functions**

Provides client-side utilities for:
- DOM manipulation
- Event handling
- Helper functions
- Interactive features

### [static/site.webmanifest](static/site.webmanifest)
**Progressive Web App Manifest**

PWA configuration including:
- App name and description
- Start URL
- Display mode
- Theme colors
- Icons for different resolutions

### [static/icons/](static/icons/)
**Application Icons**

Contains:
- `favicon.ico` - Classic favicon
- `icon.svg` - SVG icon for modern browsers
- `icon.png` - Apple touch icon (180x180px)
- Default profile pictures and brand assets

### [static/profile_pics/](static/profile_pics/)
**User Profile Picture Storage**

Directory for storing user profile images, currently contains default profile pictures referenced in templates.

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Modern web framework for building APIs |
| **Uvicorn** | ASGI server for running FastAPI applications |
| **Jinja2** | Template engine for server-side rendering |
| **Bootstrap 5** | Responsive CSS framework |
| **Python 3** | Programming language |
| **HTML5** | Semantic markup |
| **CSS3** | Styling and layout |
| **JavaScript** | Client-side interactivity |

## Development Tips

### Adding New Posts
Edit the `posts` list in [main.py](main.py) to add new blog posts:
```python
posts.append({
    "id": 3,
    "author": "Your Name",
    "title": "Your Blog Title",
    "content": "Your blog content here.",
    "date_posted": "May 26, 2026"
})
```

### Accessing FastAPI Docs
Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Hot Reload
Use the `--reload` flag with uvicorn to automatically restart the server when code changes:
```bash
uvicorn main:app --reload
```

### Static File Changes
Changes to CSS and JavaScript will be reflected immediately in the browser (no server restart needed).

## Future Enhancements

Potential features for expanding this application:
- Database integration (SQLAlchemy + PostgreSQL)
- User authentication and authorization
- Post creation/editing endpoints
- Comment system
- Search functionality
- Pagination
- Admin dashboard
- Post categories/tags
- Email notifications

## Troubleshooting

### Port Already in Use
If port 8000 is in use, specify a different port:
```bash
uvicorn main:app --reload --port 8001
```

### Static Files Not Loading
Ensure the `static/` directory exists in the same location as `main.py` and that file paths are correct.

### Templates Not Found
Ensure the `templates/` directory exists in the same location as `main.py`.

## License

This project is provided as-is for educational and development purposes.

---

**Last Updated**: May 26, 2026
