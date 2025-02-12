# 🚀 Data Validation Framework (WIP)  
*A Scalable, AI-Assisted Data Quality Platform*

## **🌟 Overview**
The **Data Validation Framework** is an **extensible, AI-assisted platform** designed to ensure **data quality and integrity** across different data sources. Built on **FastAPI**, **Great Expectations**, and **modern data engineering principles**, this framework provides a **structured way to define and enforce data contracts** while integrating with multiple databases and validation engines. This work is extension from my master thesis which is based on data quality and the most popular tools on the market.

## **🔧 Current Features**
✅ **FastAPI-based REST API** for managing and executing data validation tasks.  
✅ **Data Contracts** defined in a standardized **YAML format**, specifying schema constraints & expectations.  
✅ **Great Expectations (GX) Integration** to apply and enforce validation rules.  
✅ **Custom Checkpoints & Expectation Suites** automatically generated from data contracts.  
✅ **Flexible Data Ingestion** (CSV files, and soon, direct database connections).  
✅ **Structured Logging & Debugging** with a scalable event-driven architecture.  

## **🚀 Future Roadmap**
🔹 **Interactive CLI & Chatbot Assistant** – Users will be guided through data contract creation using **AI-powered prompts**.  
🔹 **Live Database Validation** – Support for **PostgreSQLa and MongoDBL**, and cloud storage validation.  
🔹 **Multi-Engine Data Quality Framework** – Expand beyond GX, integrating **custom Python checks** and external validation tools.  
🔹 **User-Friendly Web Interface** – Build a **React-based UI** to visualize validation results & manage contracts.  
🔹 **Versioned Data Contracts & SLA Monitoring** – Implement **data lineage, contract history, and alerts** for quality violations.  
🔹 **Integration with AI & Knowledge Graphs** – Automate metadata extraction & recommendation-based validation rules.  

## **📦 Tech Stack**
- **Backend:** FastAPI, Python 3.x  
- **Data Quality Engine:** Great Expectations (GX)  
- **Database (Planned):** MongoDB, PostgreSQL  
- **Deployment:** Docker (Planned for scalability)  
- **AI & Automation (Future):** LLM-based contract suggestions, automated rule mapping  

## **⚡ Getting Started**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/data-validation-framework.git
cd data-validation-framework
python3 -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
✅ API is now live at: http://127.0.0.1:8000
✅ Swagger UI for testing: http://127.0.0.1:8000/docs
