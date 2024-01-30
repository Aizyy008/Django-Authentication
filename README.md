**Recipe Project Readme**

The Recipe Project is a Django web application showcasing basic CRUD functionalities for managing recipes. Users can create, view, update, and delete recipes. Additionally, the project incorporates Django user authentication, allowing users to register, log in, and log out.

### Project Structure:

- **Models:**
  - A `Receipe` model is defined to store information about each recipe.
  - Fields include `receipe_name`, `receipe_description`, `receipe_image`, and a foreign key to the `User` model for associating recipes with specific users.

- **Views:**
  - **`create_receipe`:** A function to create a new recipe based on form data.
  - **`receipes`:** Displays a list of recipes, supports adding new recipes, and allows filtering by name.
  - **`delete_receipe`:** Deletes a selected recipe.
  - **`update_receipe`:** Updates the details of a specific recipe.
  - **`login_page`:** Handles user login.
  - **`logout_page`:** Handles user logout.
  - **`register`:** Handles user registration.

### Basic Workflow:

1. **Recipe Creation:**
   - Users can add new recipes by providing a name, description, and an optional image.

2. **Recipe Listing:**
   - The `receipes` view displays a list of all recipes, allowing users to view details, update, or delete them.

3. **Recipe Update and Delete:**
   - Recipes can be updated or deleted using the respective functionalities.

4. **User Authentication:**
   - Users can register for an account, log in, and log out using the provided views (`login_page`, `logout_page`, `register`).

### Usage:

1. **Installation:**
   - Clone the repository.
   - Install required dependencies using `pip install -r requirements.txt`.

2. **Database Setup:**
   - Run database migrations using `python manage.py makemigrations` followed by `python manage.py migrate`.

3. **Run the Application:**
   - Start the development server with `python manage.py runserver`.
   - Access the application at `http://localhost:8000/`.

4. **Access Admin Panel:**
   - An admin panel is available at `http://localhost:8000/admin/`.
   - Superuser credentials can be created using `python manage.py createsuperuser`.

### Project URLs:

- `/`: Home page.
- `/success-page/`: Example success page.
- `/contact_us/`: Contact us page.
- `/about/`: About page.
- `/receipes/`: Recipe listing and CRUD operations.
- `/login/`: User login page.
- `/register/`: User registration page.
- `/logout/`: User logout.

### Additional Notes:

- Ensure proper Django settings, including database configuration, media file settings, and static file settings.
- Debug mode is enabled in the `urls.py` file for development. Update it for production use.
- Media files are served during development; include proper configurations for production.

### Technologies Used:

- Django
- Python
- HTML/CSS
- Bootstrap

Feel free to explore, enhance, and customize the Recipe Project for your specific requirements!
