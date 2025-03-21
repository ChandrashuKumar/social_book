# Socialbook

Welcome to **Socialbook**, a social media platform built using the Django web framework. Explore the live application at [https://chandrashu.pythonanywhere.com/](https://chandrashu.pythonanywhere.com/).

## Overview

Socialbook is a Django-based web application that allows users to register, log in, and interact with each other by creating posts, following other users, and engaging with content. This project was developed following the tutorial "Build a Social Media App with Django – Python Web Framework Tutorial" by freeCodeCamp.org.

## Features

- **User Authentication**: Secure user registration and login functionality.
- **User Profiles**: Personalized user profiles displaying user information and posts.
- **Post Creation**: Users can create, edit, and delete their own posts.
- **Follow System**: Ability to follow and unfollow other users to see their posts in your feed.
- **Like and Comment**: Engage with posts through likes.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/socialbook.git
   cd socialbook
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Deployment

Socialbook is deployed on PythonAnywhere. To deploy your own instance:

1. **Sign up for a PythonAnywhere account**.

2. **Upload your project files** to PythonAnywhere.

3. **Set up a virtual environment** on PythonAnywhere and install the required dependencies.

4. **Configure the web app** on PythonAnywhere to point to your Django project.

For detailed instructions, refer to PythonAnywhere's guide on [Deploying an existing Django project](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*This project is based on the tutorial "Build a Social Media App with Django – Python Web Framework Tutorial" by freeCodeCamp.org.* 
