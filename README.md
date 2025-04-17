# Django Blog Platform

A full-featured blog platform built with Django, featuring Persian (Jalali) date support and modern content management capabilities.

## Features

- **Content Management System**
  - Create, edit, and delete blog posts
  - Post categorization
  - Draft and publish workflow
  - Reading time estimation
  - Image management with automatic resizing
  - Search functionality with TrigramSimilarity

- **User Management**
  - User registration and authentication
  - User profiles with customizable information
  - Profile images with automatic resizing
  - Author dashboards

- **Interactive Features**
  - Comment system with moderation
  - Contact form (ticket system)
  - Responsive design

- **Localization**
  - Persian (Farsi) interface
  - Jalali date support for Persian calendar

## Technology Stack

- **Backend**: Django 5.1
- **Database**: SQLite (default), PostgreSQL support
- **Date Handling**: django-jalali for Persian calendar support
- **Image Processing**: django-resized

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-blog-platform.git
   cd django-blog-platform
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```
   cp .env-example .env
   ```
   Edit the `.env` file with your specific configuration.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Visit http://127.0.0.1:8000/ to access the blog, and http://127.0.0.1:8000/admin/ for the admin interface.

### Admin Interface

The admin interface provides comprehensive management capabilities:
- Post creation and management
- User management
- Comment moderation
- Media management

### Content Creation

1. Log in with your account
2. Navigate to your profile
3. Click "Create New Post"
4. Fill in the post details (title, description, category, etc.)
5. Add images to your post
6. Save as draft or publish immediately

### User Interaction

- Visitors can read posts and search for content
- Registered users can comment on posts
- Contact form available for user feedback

## Project Structure

- `blog/` - Main application with models, views, and templates
- `base/` - Project configuration and settings
- `media/` - Uploaded media files
- `templates/` - HTML templates
