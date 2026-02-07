# Python Personal Finance Manager

## Project Overview
The Personal Finance Manager is a command-line based Python application designed to help users track, manage, and analyze their personal expenses. The project demonstrates core Python programming concepts including object-oriented programming, file handling, error handling, modular code organization, and basic data analysis.

This project was developed as part of **Month 1 – Python Programming Mastery** and follows best practices for clean and maintainable Python code.

---

## Features
- Add new expenses with amount, category, date, and description
- View all recorded expenses
- Category-wise expense summary
- Generate monthly expense reports
- Search expenses by category or description
- CSV-based data persistence
- Input validation and error handling
- Data backup and restore functionality
- Modular and well-organized code structure
- Interactive command-line menu system

---

## Technologies Used
- Python 3
- CSV module for file handling
- Datetime module for date validation
- OS and shutil modules for file operations

---

## Project Structure

finance-manager/
│
├── main.py # Application entry point
├── README.md # Project documentation
├── requirements.txt # Project dependencies
│
├── src/
│ ├── expense.py # Expense class (OOP)
│ ├── file_manager.py # CSV read/write operations
│ ├── menu.py # Command-line menu interface
│ ├── reports.py # Reporting and analysis functions
│ └── utils.py # Validation and utility functions
│
├── data/
│ ├── expenses.csv # Expense data file
│ └── expenses_backup.csv # Backup file (generated)
│
├── screenshots/ # Application screenshots
└── docs/ # Additional documentation



---

## Installation & Setup
1. Ensure Python 3.8 or above is installed.
2. Clone or download the project repository.
3. Navigate to the project directory.

---

## How to Run the Application
Run the following command from the project root directory:


---

## Usage Guide
1. Launch the application.
2. Choose options from the menu:
   - Add expenses
   - View expense list
   - Generate reports
   - Search expenses
   - Backup data
3. Follow on-screen instructions for input.

---

## Error Handling
- Invalid numeric inputs are handled gracefully.
- Incorrect date formats are validated.
- User input errors do not crash the application.

---

## Sample Outputs
Screenshots demonstrating application functionality are included in the `screenshots/` folder.

---

## Future Enhancements
- Data visualization using charts
- Budget planning and alerts
- Export reports to Excel or PDF
- User authentication

---

## Conclusion
This project successfully implements a complete Python-based personal finance management system using object-oriented design, file handling, and modular programming principles.

