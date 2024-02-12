# Expense-Tracker-Flask

Overview
Expense Tracker is a web application built using Flask, a Python web framework, designed to help users track their expenses efficiently. With this application, users can easily add, view, edit, and delete their expenses, providing them with a convenient way to manage their financial transactions.

Features
User Authentication: Users can register, login, and logout securely to access their personal expense data.
Add Expense: Users can add new expenses by providing details such as date, category, amount, and description.
View Expenses: Users can view their expenses in a dashboard format, displaying all expenses with options to filter and sort them.
Edit and Delete Expenses: Users can edit or delete existing expenses, providing flexibility in managing their financial records.
Responsive Design: The application features a responsive design, ensuring optimal user experience across different devices and screen sizes.
Technologies Used
Flask: Flask is a lightweight Python web framework used for building web applications. It provides flexibility and simplicity, making it ideal for developing small to medium-sized projects.
SQLAlchemy: SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library for Python. It simplifies database interactions and allows seamless integration with Flask applications.
HTML/CSS: HTML (HyperText Markup Language) is used for creating the structure of web pages, while CSS (Cascading Style Sheets) is used for styling and layout.
Bootstrap: Bootstrap is a front-end framework for developing responsive and mobile-first websites. It provides pre-designed components and styles, facilitating faster development.
SQLite: SQLite is a lightweight, serverless database engine used for storing application data. It's well-suited for small-scale applications like Expense Tracker.
Installation and Setup
Clone the Repository: Clone the Expense Tracker repository to your local machine.
bash
Copy code
git clone https://github.com/yourusername/expense-tracker.git
Install Dependencies: Navigate to the project directory and install the required dependencies using pip.
bash
Copy code
cd expense-tracker
pip install -r requirements.txt
Database Setup: Ensure that you have SQLite installed. Initialize the SQLite database by running the following commands.
csharp
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the Application: Start the Flask development server.

flask run
Access the Expense Tracker application in your web browser at http://localhost:5000.
Usage
Register/Login: Create a new account or log in with existing credentials.
Add Expense: Navigate to the "Add Expense" page, fill in the expense details, and submit the form.
View Expenses: Visit the dashboard to view all your expenses. You can filter and sort the expenses based on different criteria.
Edit/Delete Expense: Click on an expense to edit or delete it as needed.

Contributing
Contributions to the Expense Tracker project are welcome! If you have any ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

