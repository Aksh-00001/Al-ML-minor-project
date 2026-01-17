# 🎓 IILM University AI Chatbot

A smart AI-powered chatbot built using **Flask** and **Ollama (TinyLlama model)** to assist students with queries related to **IILM University, Greater Noida**.

---

## 🚀 Project Overview

This project is a web-based chatbot application designed to provide quick and accurate information about IILM University.
It answers student queries related to:

* Admission criteria
* Available undergraduate and postgraduate programs
* University details
* Contact information
* General college-related questions

The chatbot uses the **TinyLlama LLM model via Ollama** and is powered by a Flask backend.

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **AI Model:** TinyLlama (via Ollama)
* **Frontend:** HTML, CSS, JavaScript
* **API Handling:** JSON-based REST API

---

## 📂 Project Structure

```
project-folder/
│
├── templates/
│   └── index.html
│
├── static/
│   └── (CSS/JS files)
│
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚙ Features

* AI chatbot trained with predefined system knowledge about IILM University
* Real-time user interaction
* Simple and clean web interface
* REST API endpoint for chatbot communication
* Error handling for invalid inputs

---

## 🧠 System Knowledge Base

The chatbot is pre-configured with important details such as:

* University name and location
* Admission requirements
* Undergraduate programs
* Postgraduate programs
* General university information
* Contact details

All responses are generated based on this structured information to ensure accuracy.

---

## 🔧 Installation & Setup

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* Flask
* Ollama
* TinyLlama model

### Step 1 – Clone the Repository

```bash
git clone https://github.com/your-username/iilm-chatbot.git
cd iilm-chatbot
```

### Step 2 – Install Dependencies

```bash
pip install flask ollama
```

### Step 3 – Run the Application

```bash
python app.py
```

### Step 4 – Open in Browser

Go to:

```
http://localhost:5500
```

---

## 🔗 API Endpoint

### Chat Endpoint

**POST** `/chat`

#### Request Format:

```json
{
  "message": "Tell me about MBA programs"
}
```

#### Response Format:

```json
{
  "response": "MBA (Single Specialization), MBA (Dual Specialization)..."
}
```

---

## 💡 Future Improvements

* Add database for dynamic university data
* Support for multiple AI models
* Voice input and output
* User authentication
* Deployment on cloud platforms

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📧 Contact

For any queries related to the project:

* **Developer:** Aksh Raj
* **Email:** [akshrajsingh99310@gmail.com](mailto:akshrajsingh99310@gmail.com)

---

### ⭐ If you like this project, don’t forget to star the repository!
