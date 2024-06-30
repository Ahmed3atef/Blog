# Personal Website

![License](https://img.shields.io/badge/license-MIT-blue.svg)

This repository contains the source code for my personal website. It is built using Django, Django REST Framework, and Bootstrap 4, providing an elegant and responsive design for showcasing my portfolio, blog posts, and other personal information.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Home page with personal introduction
- Portfolio section showcasing projects
- Blog section with posts and comments
- Contact form for getting in touch
- Responsive design with Bootstrap 4
- RESTful API for blog posts and portfolio items

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 4
- **Database**: SQLite (default), can be configured to use other databases like PostgreSQL or MySQL
- **Deployment**: Instructions for deploying on Heroku or any other server

## Installation

Follow these steps to get a local copy up and running:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ahmed3atef/Personal_website.git
   cd Personal_website
   ```
2.  **Create and activate a virtual environment**:

    ```bash

    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations**:

    ```bash
    
    python manage.py migrate
    ```

6.  **Create a superuser**:

    ```bash
    
    python manage.py createsuperuser
    ```

7.  **Run the development server**:

    ```bash

    python manage.py runserver
    ```

Usage
-----

Once the server is running, you can access the website at `http://127.0.0.1:8000/`. The admin interface is available at `http://127.0.0.1:8000/admin/` where you can manage content like blog posts and portfolio items.

### Customizing the Site

-   **Templates**: Located in the `templates` directory, customize the HTML files to change the layout and content.
-   **Static Files**: Located in the `static` directory, update CSS, JavaScript, and image files as needed.
-   **Configuration**: Update `settings.py` for changes like database configurations, static files location, etc.

API Endpoints
-------------

The project includes a RESTful API built with Django REST Framework. Here are some example endpoints:


-   **Create a new blog post**: `POST /api/send-comment/{id}`

-   **Delete a blog post**: `DELETE /api/delete-comment/{id}/`

Contributing
------------

Contributions are welcome! Please follow these steps to contribute:

1.  Fork the repository.
2.  Create a new branch for your feature (`git checkout -b feature/new-feature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/new-feature`).
5.  Open a pull request.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Contact
-------

For any inquiries or feedback, please contact me at:

-   Email: clay674302@gmail.com
-   GitHub: [Ahmed3atef](https://github.com/Ahmed3atef)

