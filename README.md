---

# Meta (Little Lemon) Back End Developer Project

This project is a Django-based web application for managing restaurant reservations and displaying menu items. It provides features for customers to book reservations, view the menu, and filter menu items by name. The application also supports RESTful APIs for data access.

---

## Features

- **Home and About Pages**: User-friendly interfaces to introduce users to the application and its services.
- **Booking System**:
  - Form-based reservation system.
  - Validation to prevent double bookings for the same date and slot.
- **Menu Management**:
  - View all menu items with detailed descriptions and images.
  - Search for menu items by name.
  - View individual menu items by their unique ID.
- **RESTful APIs**:
  - Endpoints for fetching menu and booking data.
  - Supports JSON responses and template rendering.

---

## Technologies Used

### Backend
- **Django**: Web framework for rapid development.
- **Django REST Framework (DRF)**: For building RESTful APIs.

### Frontend
- **HTML Templates**: Rendered with Django's TemplateHTMLRenderer.

### Database
- **PostgreSQL**: Default database for local development.

### Additional Libraries
- **datetime**: For handling date and time operations.
- **CSRF Exemption**: Used for certain views that require bypassing CSRF protection.
- **JSON**: For handling JSON-based data.

---

## Architecture

### Models
1. **Booking**:
   - Fields: `first_name`, `reservation_date`, `reservation_slot`, `reservation_food`.
   - Allows customers to reserve a table and select a food choice.
   - Validates against duplicate bookings for the same date and slot.

2. **Menu**:
   - Fields: `name`, `price`, `menu_item_description`, `image`.
   - Stores details about menu items available at the restaurant.

### Serializers
1. **Bookingserial**:
   - Serializes all fields of the `Booking` model.
2. **Menuserial**:
   - Serializes all fields of the `Menu` model.

### Views
- Functional views for:
  - Rendering templates (`home`, `about`, `book`).
  - API views for CRUD operations on bookings and menu items.
  - Filtering menu items by name.
  - Displaying specific menu items or booking lists.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Information14/META-LITTLE-LEMON.git
   cd 
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---
