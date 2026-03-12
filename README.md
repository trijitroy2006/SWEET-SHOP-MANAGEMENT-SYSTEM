

# Sweet Shop Management System

## 📌 Project Overview

The **Sweet Shop Management System** is a console-based application designed to streamline and automate the daily operations of a sweet shop. Built with Python and MySQL, this project helps reduce manual effort by efficiently managing inventory, tracking customer orders, and processing sales.

This project was developed by **Trijit Roy** for the AISSCE 2024-2025 Examination.

## 🚀 Features

The system provides two distinct interfaces based on user roles:

### 1. Owner Module

   **Add New Sweet:** Insert new sweet items into the inventory along with their ID, name, quantity, and price .

   **Update Sweet Information:** Modify the pricing of existing stock .

   **Delete Sweet:** Remove a sweet from the inventory using its Sweet ID .
   
   **Display All Sweets:** View the complete available stock.
   
   **Change Password:** Update the owner's login credentials securely .


### 2. Customer Module

  **View Available Items:** Browse the list of sweets currently in stock with their prices .
  
  **Item Bucket:** Add items to a virtual shopping cart by specifying the Sweet ID and quantity . This automatically deducts the purchased quantity from the main stock .
  
  **Payment:** Generate the final bill amount for the customer's order .


## 🛠️ Technology Stack

   **Front-End / Logic:** Python 3.11.3 / 3.12.0 


   **Back-End / Database:** MySQL 


   **Libraries Used:** `mysql-connector-python` 


   **Operating System:** Microsoft Windows 10 



## 📋 System Requirements

  **Processor:** Intel Core i3 / Celeron or equivalent 


  **RAM:** Minimum 4 GB RAM 


  **Storage:** 320 GB HDD desirable 



## ⚙️ Installation and Setup

  **1. Install MySQL Server**
        Ensure you have MySQL installed and running on your local machine.

  **2. Install Python & Required Libraries**
          Make sure Python is installed. Open your command prompt or terminal and install the MySQL connector:

```bash
pip install mysql-connector-python

```

**3. Configure Database Credentials**
          Open the `Sweet Shop Management system project.py` file. Locate the database connection line (around line 7) and update the `passwd` field to match your local MySQL root password:

```python
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="YOUR_MYSQL_PASSWORD")

```

**4. Run the Application**
     Execute the Python script . The script is designed to automatically create the necessary database (`Sweet_Shop`) and tables (`login`, `purchase`, `stock`) if they do not already exist .

## 🔐 Default Login Credentials

  Upon the first execution, the system creates a default owner profile:


**Password:** `3063` 


(Note: It is highly recommended to change this password using the "Change Password" option in the Owner menu.)

## 🗄️ Database Schema

The system automatically generates the following tables :

 * `login`: Stores owner credentials (`username`, `password`).


* `purchase`: Tracks sales records (`odate`, `name`, `s_id`, `amount`) .


* `stock`: Manages inventory (`s_id`, `s_name`, `quantity`, `price`) .


## 👨‍💻 Author

**Trijit Roy** Class XII, Section D, Humanities Stream Satish Chandra Memorial School
