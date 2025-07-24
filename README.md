# DietApollo 🍱

**DietApollo** is a pixel-themed web application that allows users to manage their personal meal plans, grocery lists, and calorie intake — all in one retro-styled interface. Built using Django for the back-end and JavaScript for dynamic front-end interactions, DietApollo aims to streamline daily food tracking with a nostalgic 8-bit twist.

<img width="1915" height="873" alt="DietApollo" src="https://github.com/user-attachments/assets/93b4b3db-040b-4cc7-a7eb-e7e0c24fd217" />

---

## 🚀 Distinctiveness and Complexity

DietApollo is distinct from other CS50W projects in both purpose and technical design. Unlike the provided social network, mail, or commerce projects, this application is not centered around public content sharing or transactional systems. Instead, it focuses on private, user-specific tools for health and nutrition tracking.

What sets DietApollo apart:
- **Multi-tab personal dashboard:** The app organizes user data into four separate views — Dashboard, Favorites, Grocery, and Calories — each with its own purpose and data flow.
- **AJAX-based interactivity:** Unlike traditional form submissions, DietApollo uses JavaScript `fetch` calls and CSRF-secure JSON APIs for creating, updating, and toggling recipe data in real-time, without page reloads.
- **Custom pixel-style design:** Inspired by retro video games, the styling uses Google Fonts (`Press Start 2P`) and custom CSS for a unique user experience.
- **Favorites toggle logic:** The "star" system dynamically adds recipes to the "Favorites" tab using API calls and condition-based rendering, a non-trivial state-management feature.
- **Full CRUD functionality** is implemented via a combination of Django views and JavaScript DOM manipulation for an interactive UX.
- **Custom data models and form handling** for Recipes, Groceries, and CalorieEntries.

These features demonstrate architectural complexity and interactivity well beyond the standard tutorial projects.

---

## 📁 File Structure and Contents

- **`mealprep/models.py`**: Contains the Django models for `User`, `Recipe`, `GroceryItem`, and `CalorieEntry`.
- **`mealprep/views.py`**: Django views for handling routing and API endpoints for JSON fetch.
- **`mealprep/forms.py`**: Custom Django form classes for recipe, grocery, and calorie input.
- **`mealprep/templates/mealprep/*.html`**:
  - `index.html`: Landing page
  - `dashboard.html`: Add, edit, and favorite recipes
  - `favorites.html`: Displays starred recipes only
  - `grocery.html`: Grocery list with notes
  - `calories.html`: Calorie tracker
- **`mealprep/static/mealprep/js/main.js`**: Handles dynamic JavaScript rendering and API interactions.
- **`mealprep/static/mealprep/css/styles.css`**: Custom pixel-theme design and responsive styling.
- **`requirements.txt`**: Lists Python packages needed to run the project.
- **`README.md`**: Project documentation (this file).

---

## 🔧 Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/trnahnh/DietApollo.git
   cd DietApollo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Visit the app in your browser:**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📱 Mobile-Responsiveness

The layout uses flexible grid and flexbox styling to ensure the application is usable on mobile and tablet screens. Font sizes, buttons, and containers scale appropriately for smaller devices.

---

## 📌 Additional Notes

- All AJAX operations are CSRF-protected and Django-authenticated.
- JavaScript rendering uses minimal libraries (vanilla JS) for maximum transparency.
- No third-party UI frameworks were used to preserve the retro aesthetic.

---

## 👩‍💻 Author

**Andrea Tran | tran3ah@mail.uc.edu**  
University of Cincinnati  
College of Engineering and Applied Science — Class of 2029
