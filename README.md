# 🌱 EcoPackAI – AI-Powered Sustainable Packaging Recommendation System

## 📍 Project Overview

**EcoPackAI** is an intelligent **decision-support system** designed to help businesses identify the most **sustainable, cost-efficient, and durable packaging materials** based on product characteristics and supply-chain constraints.

The system leverages **machine learning** to evaluate multiple packaging alternatives and recommend optimal solutions that **minimize environmental impact** while ensuring **product safety, performance, and cost efficiency**.

---

## 🎯 Key Objectives

- Reduce dependency on **non-biodegradable packaging materials**
- Provide **eco-friendly and cost-optimized** packaging recommendations
- Enable **data-driven decision-making** for packaging selection
- Support **sustainability and ESG goals** for enterprises

---

## ✨ Key Features

- 🧠 **AI-based recommendation engine** for packaging materials  
- 📦 **Material comparison** based on durability, biodegradability, cost, and carbon footprint  
- 🔍 **Search and filter options** tailored to business requirements  
- 📊 **Analytics dashboard** for environmental impact insights  
- 📝 **Auto-generated packaging recommendation reports**  
- 🌐 **Full-stack web application** with interactive UI  

---

## 🧱 System Architecture

EcoPackAI follows a **modular and scalable pipeline architecture**, ensuring flexibility and extensibility.

### 🔹 Architecture Components

- **Input Module**  
  Collects product details such as type, weight, dimensions, shipping conditions, and constraints.

- **Material Database**  
  Stores structured data on eco-friendly packaging materials and their properties.

- **ML Recommendation Engine**  
  Uses machine learning models to predict optimal packaging material combinations.

- **Optimization & Scoring Module**  
  Evaluates materials based on **cost, sustainability metrics, and performance scores**.

- **Reporting Module**  
  Generates **downloadable and human-readable recommendation reports**.

- **Frontend Dashboard**  
  Provides visualization, insights, and report access through an intuitive interface.

---

## 🛠️ Technology Stack

### **Backend**
- **Framework:** Flask 3.1.2 - Lightweight Python web framework for REST API development
- **API:** RESTful endpoints for prediction, analytics, and data management
- **Database:** 
  - SQLite (Development) - Lightweight embedded database
  - PostgreSQL (Production) - Robust relational database with psycopg2-binary driver
- **ORM:** SQLAlchemy 3.1.1 - Python SQL toolkit and Object-Relational Mapping
- **Migration:** Flask-Migrate 4.0.7 - Database schema version control
- **Middleware:**
  - Flask-CORS 5.0.0 - Cross-Origin Resource Sharing support
  - Flask-Caching 2.3.0 - Server-side caching for performance optimization

### **Machine Learning & Data Science**
- **ML Frameworks:**
  - Scikit-learn ≥1.5.0 - Classical ML algorithms (Random Forest, preprocessing)
  - XGBoost 2.0.3 - Gradient boosting for predictive modeling
- **Data Processing:**
  - Pandas ≥2.1.0 - Data manipulation and analysis
  - NumPy ≥2.1.0 - Numerical computing and array operations
  - SciPy ≥1.11.4 - Scientific computing and statistical functions
- **Model Persistence:** Joblib 1.5.2 - Efficient model serialization
- **Configuration:** PyYAML 6.0.2 - YAML-based configuration management

### **Frontend**
- **Core Technologies:**
  - HTML5 - Semantic markup and structure
  - CSS3 - Modern styling with custom properties and animations
  - Vanilla JavaScript (ES6+) - Dynamic interactivity and API integration
- **UI Components:**
  - Responsive design with mobile-first approach
  - Interactive forms with real-time validation
  - Data visualization with dynamic charts
- **Key Pages:**
  - index.html - Landing page and product input
  - results.html - Packaging recommendations display
  - analytics.html - Environmental impact dashboard
  - product.html - Product management interface

### **Development & Deployment**
- **Containerization:** Docker - Application containerization with docker-compose
- **Environment Management:**
  - python-dotenv 1.2.1 - Environment variable management
  - Virtual environments for dependency isolation
- **API Server:** 
  - Uvicorn 0.38.0 - ASGI server for async operations
  - FastAPI 0.123.8 - Modern API framework (alternate/future enhancement)
- **Version Control:** Git - Source code management

### **Data Validation & Configuration**
- **Validation:** Pydantic 2.12.5 - Data validation and settings management
- **Configuration:** YAML-based configuration for ranking weights and parameters
- **Logging:** Python logging module with structured output

### **Testing & Quality Assurance**
- **Testing Framework:** Pytest - Unit and integration testing
- **E2E Testing:** Custom test suite for end-to-end workflows
- **Documentation:** Comprehensive markdown documentation in `/docs`

---

## 📁 Project Structure

```
EcoPackAI/
├── project/
│   ├── backend/              # Flask REST API
│   │   ├── app.py           # Main application entry point
│   │   ├── predict.py       # ML prediction logic
│   │   ├── models/          # Database models
│   │   └── middleware/      # Custom middleware
│   ├── frontend/            # Web interface
│   │   ├── index.html       # Landing page
│   │   ├── results.html     # Recommendations view
│   │   ├── analytics.html   # Analytics dashboard
│   │   ├── css/            # Stylesheets
│   │   └── js/             # JavaScript modules
│   ├── ml/                  # Machine learning artifacts
│   │   ├── models/         # Trained model files
│   │   ├── metrics/        # Model evaluation metrics
│   │   └── metadata/       # Model metadata
│   ├── data/               # Data pipeline
│   │   ├── raw/           # Original datasets
│   │   ├── processed/     # Cleaned data
│   │   └── final/         # Model-ready data
│   ├── notebooks/          # Jupyter notebooks
│   │   ├── 01_dataset_prep.ipynb
│   │   ├── 02_preprocessing_pipeline.ipynb
│   │   ├── 03_train_test_split_cv.ipynb
│   │   └── ...
│   ├── config/             # Configuration files
│   │   └── ranking_weights.yaml
│   ├── docs/               # Documentation
│   ├── tests/              # Test suite
│   └── environments/       # Docker & dependencies
│       ├── Dockerfile
│       ├── docker-compose.yml
│       └── requirements.txt
├── README.md
└── IMPLEMENTATION.md
```

---

##  ML Pipeline Workflow

1. **Data Ingestion** → Load raw packaging material data
2. **Preprocessing** → Clean, transform, and engineer features
3. **Train/Test Split** → Stratified splitting with cross-validation
4. **Model Training** → Random Forest & XGBoost model training
5. **Evaluation** → Performance metrics and validation
6. **Model Versioning** → Track experiments and model iterations
7. **Ranking Logic** → Multi-criteria scoring algorithm
8. **Explainability** → SHAP values and feature importance
9. **Deployment** → Model packaging and API integration

For detailed documentation, see the [/docs](project/docs/) directory.

---

## 🌍 Impact

EcoPackAI enables organizations to:
- Make **responsible packaging choices**
- Reduce **carbon footprint** by up to **40%**
- Balance **sustainability, cost, and durability** with data-driven insights
- Move towards **greener supply chains** and meet ESG targets
- Automate packaging decisions with **AI-powered recommendations**

---

## 📈 Key Metrics & Performance

- **Model Accuracy:** 85%+ on cost prediction
- **CO2 Prediction:** R² score of 0.82+
- **Response Time:** <500ms for recommendations
- **Materials Database:** 100+ sustainable packaging options
- **Decision Criteria:** 8+ weighted factors (cost, CO2, durability, recyclability, etc.)

---

## 📝 Documentation

Comprehensive documentation is available in the `/project/docs` directory:
- API Documentation
- Data Dictionary
- Feature Engineering Guide
- Model Evaluation Reports
- Analytics Testing Guide
- E2E Testing Guide

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

Anuska Dasgupta

---

> *EcoPackAI bridges the gap between sustainability goals and practical packaging decisions using AI.*
