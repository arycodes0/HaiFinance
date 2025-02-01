# 🏦 Haipriori

Haipriori is a **simple full-stack finance management web application** built with **React (Vite)** on the frontend and **Django (Django REST Framework)** on the backend. It allows users to manage financial data, and loans seamlessly.

---

## 🚀 Features

- 🔹 **User Authentication** – Secure login & registration.
- 🔹 **Loan Management** – Apply for loans, track approvals.
- 🔹 **Financial Dashboard** – View key financial insights.
- 🔹 **Real-Time Data** – Updates transactions dynamically.
- 🔹 **RESTful API** – Backend powered by Django REST Framework.
- 🔹 **Modern UI** – Built with React, CSS, and Vite.
- 🔹 **Database Integration** – PostgreSQL for secure data storage.
- 🔹 **Error Handling & Validation** – Secure form validation.

---

## 🏗️ Tech Stack

### **Frontend**

- ⚛️ **React (Vite)**
- 🎨 **CSS**
- 🌍 **Axios (for API requests)**
- 📦 **Prettier** (for code formatting)

### **Backend**

- 🐍 **Django & Django REST Framework**
- 🗄️ **PostgreSQL (Database)**
- 🔒 **JWT Authentication**
- 🚀 **Django ORM**
- 🌐 **DRF Serializers & Views**

---

## 🛠️ Installation Guide

### **1️⃣ Clone the Repository**

```sh
git clone https://git@github.com:arycodes0/HaiFinance.git
cd HaiFinance

--------------- Backend Setup (Django) ----------------

cd backend
python3 -m venv venv   # Create virtual environment
source venv/bin/activate  # Activate it (Mac/Linux)
venv\Scripts\activate     # (Windows)
pip install -r requirements.txt  # Install dependencies
python manage.py migrate  # Apply migrations
python manage.py runserver  # Start backend server
# Backend will run on: http://127.0.0.1:8000/

--------------- Frontend Setup (React) ----------------

cd frontend
npm install  # Install dependencies
npm run dev  # Start frontend server
# Frontend will run on: http://localhost:5173/
