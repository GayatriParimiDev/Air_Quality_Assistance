# 🌍 AQI Sense - Air Quality Chatbot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.2-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.2-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black)](https://www.javascript.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34C26?logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Goals & Outcomes](#project-goals--outcomes)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

**AQI Sense** is an intelligent web-based Air Quality Chatbot that enables users to query global air quality data interactively. Users can ask questions about Air Quality Index (AQI) levels in any city worldwide, receive health precautions, discover the most polluted areas, and access real-time air quality insights.

The application leverages natural language processing, fuzzy matching algorithms, and a comprehensive global air quality dataset to provide accurate, personalized responses to user queries.

---

## ✨ Features

- 💬 **Conversational AI Chatbot** - Ask questions about air quality in natural language
- 🌍 **Global City Lookup** - Search air quality data for any city with fuzzy matching
- 📊 **AQI Analysis** - Get detailed AQI values, categories, and pollutant information
- ⚕️ **Health Precautions** - Receive health recommendations based on pollution levels
- 🏆 **Top Polluted Cities Ranking** - Discover the world's most polluted locations
- 🎨 **Responsive UI** - Clean, intuitive interface accessible on all devices
- 🚀 **REST API** - Structured backend API for programmatic access
- 📈 **Data Processing** - Advanced pandas and scikit-learn powered analysis

---

## 🛠️ Tech Stack

### **Backend**
- **Framework**: Flask 2.3.2 - Lightweight Python web framework
- **Data Processing**: 
  - Pandas 2.2.2 - Data manipulation and analysis
  - NumPy 1.26.4 - Numerical computing
  - Scikit-learn 1.3.2 - Machine learning algorithms
  - RapidFuzz 2.15.1 - Fast fuzzy string matching
- **Server**: Gunicorn 21.2.0 - Production WSGI server
- **Utilities**:
  - Flask-CORS 3.0.10 - Cross-origin resource sharing
  - Python-dotenv 1.0.1 - Environment variable management

### **Frontend**
- **HTML5** - Semantic markup
- **CSS3** - Responsive styling and animations
- **JavaScript (ES6+)** - Dynamic interactions and API calls
- **Fetch API** - Asynchronous HTTP requests

### **Data**
- Global Air Quality CSV Dataset
- Automatic column detection and normalization

---

## 🎓 Project Goals & Outcomes

### **Goals**
1. **Make Air Quality Data Accessible** - Provide an intuitive interface to complex air quality metrics
2. **Promote Environmental Awareness** - Help users understand air quality impacts on health
3. **Enable Data-Driven Decisions** - Empower users with global air quality insights
4. **Demonstrate Full-Stack Development** - Showcase integration of frontend, backend, and data science

### **Outcomes**
✅ **Functional Chatbot System** - Intelligent natural language processing for air quality queries  
✅ **Comprehensive REST API** - Four main endpoints for flexible data access  
✅ **Responsive Web Interface** - User-friendly design with real-time interactions  
✅ **Advanced Data Processing** - Fuzzy matching and AQI categorization algorithms  
✅ **Health Recommendations** - Context-aware precautions based on pollution levels  
✅ **Scalable Architecture** - Production-ready with Gunicorn support  

---

## 📦 Installation

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/airquality-chatbot.git
cd airquality-chatbot
```

### **Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

### **Step 4: Verify Data File**
Ensure `backend/data/globalAirQuality.csv` exists in the backend directory.

---

## 🚀 Usage

### **Running the Application**

#### **Terminal 1 - Start Backend Server**
```bash
cd backend
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

#### **Terminal 2 - Open Frontend**
```bash
# Windows
cd frontend
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

Or manually navigate to: `file:///path/to/airquality-chatbot/frontend/index.html`

### **Using the Chatbot**

1. **Ask about a specific city**
   - "What is the AQI in Delhi?"
   - "What's the air quality in New York?"
   - "Show me AQI for Tokyo"

2. **Get health precautions**
   - "What precautions for AQI 220?"
   - "Is AQI 150 dangerous?"

3. **Find most polluted cities**
   - "Show top 5 polluted cities"
   - "What are the worst AQI cities?"

---

## 📡 API Documentation

### **Base URL**
```
http://127.0.0.1:5000
```

### **Endpoints**

#### **1. Health Check**
```http
GET /
```
**Response:**
```json
{
  "status": "AQI Chatbot API running"
}
```

---

#### **2. Chat with Chatbot**
```http
POST /api/chat
Content-Type: application/json

{
  "message": "What is the AQI in Delhi?"
}
```
**Response:**
```json
{
  "reply": "🌍 Air Quality — Delhi (India)\nAQI: 285  •  Category: Hazardous\n\n⚕️ Precautions: Avoid outdoor activities..."
}
```

---

#### **3. City Air Quality Lookup**
```http
GET /api/city?name=Singapore
```
**Response:**
```json
{
  "matched_name": "Singapore",
  "score": 100,
  "data": {
    "AQI": 68,
    "country": "Singapore",
    "PM2.5": 45.2,
    "PM10": 62.1,
    "NO2": 18.5,
    ...
  }
}
```

---

#### **4. Top N Polluted Cities**
```http
GET /api/top?n=10
```
**Response:**
```json
{
  "top_cities": [
    {
      "city": "Delhi",
      "country": "India",
      "AQI": 285,
      "category": "Hazardous"
    },
    {
      "city": "Lahore",
      "country": "Pakistan",
      "AQI": 278,
      "category": "Very Unhealthy"
    },
    ...
  ]
}
```

---

## 📁 Project Structure

```
airquality-chatbot/
├── backend/
│   ├── app.py                 # Flask application & route definitions
│   ├── chatbot.py             # NLP & message handling logic
│   ├── database.py            # Data loading & city matching
│   ├── utils.py               # AQI categorization & precautions
│   ├── requirements.txt       # Python dependencies
│   └── data/
│       └── globalAirQuality.csv  # Air quality dataset
│
├── frontend/
│   ├── index.html             # Main HTML structure
│   ├── script.js              # Frontend logic & API calls
│   └── style.css              # Styling & responsive design
│
└── README.md                  # This file
```

### **Key Files Description**

| File | Purpose |
|------|---------|
| `app.py` | Flask server, route handlers, CORS configuration |
| `chatbot.py` | Natural language parsing, message handling |
| `database.py` | CSV loading, fuzzy city matching, data retrieval |
| `utils.py` | AQI categorization, health precautions logic |
| `script.js` | Frontend API communication, UI interactions |
| `style.css` | Responsive design, animations, theme |

---

## 🔧 Troubleshooting

### **Error: Socket Permission Denied (Port 5000)**

**Solution:**
1. Change port in `backend/app.py`:
```python
app.run(host="localhost", port=8000, debug=True)
```

2. Update frontend `script.js`:
```javascript
const API_BASE = "http://127.0.0.1:8000";
```

3. Run server:
```bash
python app.py
```

---

### **Error: CSV File Not Found**

**Solution:** Ensure `backend/data/globalAirQuality.csv` exists in the backend folder.

---

### **Error: CORS Error in Browser Console**

**Solution:** Verify CORS is enabled in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

### **Error: Cannot Connect to Backend**

1. Verify backend is running: `python app.py`
2. Check correct API_BASE URL in `script.js`
3. Ensure firewall allows localhost:5000
4. Check browser console for detailed error messages

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💻 Author

Parimi Gayatri Srivarshini

---

## 📞 Support & Feedback

For issues, questions, or feature requests:
- Open an Issue on GitHub
- Check existing documentation
- Review API responses for error details

---

## 🌟 Acknowledgments

- Global Air Quality Dataset providers
- Flask and Python community
- Open-source contributors

---

**Last Updated:** April 2026  
**Version:** 1.0.0

---

## 📊 AQI Categories Reference

| AQI Range | Category | Health Effect |
|-----------|----------|---------------|
| 0-50 | Good | No health impact |
| 51-100 | Moderate | Acceptable quality |
| 101-150 | Unhealthy for Sensitive Groups | Health advisories |
| 151-200 | Unhealthy | General public effects |
| 201-300 | Very Unhealthy | Health warnings |
| 301+ | Hazardous | Emergency conditions |

---

**Made with ❤️ for better air quality awareness worldwide**
