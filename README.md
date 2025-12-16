# 📘 Google Sheets → PostgreSQL (NeonDB) Migration  
### Automated ETL, Real-Time Ingestion & SQL Analytics

This project demonstrates an end-to-end backend data engineering workflow that migrates spreadsheet-driven processes into a scalable PostgreSQL (NeonDB) backend with automated ETL, real-time ingestion, and optimized SQL analytics.

---

## 🚀 Project Overview

The system replaces manual Google Sheets–based data handling with a robust backend architecture that provides:

- Strong data integrity using relational constraints  
- Automated batch data migration (ETL)  
- Real-time auto-registration from Google Sheets  
- Efficient SQL analytics and reporting  
- Secure credential management using environment variables  

---

## 🏗️ System Architecture

```
Google Sheets (Data Entry)
        ↓
Google Apps Script (Validation & Trigger)
        ↓
Python Backend API (Flask)
        ↓
PostgreSQL Database (NeonDB)
        ↓
SQL Views & Analytical Queries
```

---

## 📂 Project Structure

```
attendance-backend/
├── api.py                  # Backend API for real-time ingestion
├── etl/
│   └── etl.py             # Batch ETL pipeline
├── sql/
│   ├── schema.sql         # Database schema
│   ├── queries.sql        # Analytical SQL queries
│   ├── views.sql          # SQL views
│   └── procedures.sql     # Stored functions
├── logs/
│   └── etl_errors.log     # ETL error logs
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

- **Database:** PostgreSQL (NeonDB)  
- **Backend:** Python, Flask  
- **ETL:** Python  
- **Automation:** Google Apps Script  
- **SQL:** PostgreSQL (Views, Functions, Indexes)  
- **Version Control:** Git & GitHub  

---

## 🔐 Environment Variables

Database credentials are managed securely using environment variables.

### `.env` file (not committed to Git)

```env
DATABASE_URL=postgresql://username:password@host/dbname
```

Ensure `.env` is included in `.gitignore`.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/attendance-backend.git
cd attendance-backend
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧱 Database Setup

Run the schema script using the NeonDB SQL Editor:

```sql
-- Execute in order
sql/schema.sql
```
### Database Schema

![Database Schema](screenshots/schema.png)
*Entity-Relationship diagram showing tables, relationships, and constraints*
---

## 🔄 ETL Pipeline (Batch Ingestion)

The ETL pipeline migrates CSV / Google Sheets–style data into PostgreSQL.

### Run ETL

```bash
python etl/etl.py
```

### ETL Features

- Deduplication and validation
- Timestamp normalization
- Batched inserts for performance
- Error logging without pipeline failure
- Idempotent execution

### ETL Output

![ETL Pipeline Output](screenshots/etl.png)
---

## 🔁 Real-Time Ingestion (Google Apps Script)

Google Sheets acts as a frontend for real-time data entry.

### Workflow

1. User edits or adds a row in Google Sheets
2. Installable Apps Script trigger validates the row
3. Data is sent as JSON to the backend API
4. Backend inserts validated data into NeonDB

### Visual Feedback

- 🔴 Red: Invalid data or API error
- 🟢 Green: Successfully inserted into database

### Google Sheets Demo

![Red Entry - Invalid Data | Green Entry - Success](screenshots/google_sheet_entry.png)

---

## 🔍 SQL Development & Optimization

The project includes:

- Aggregation queries (COUNT, AVG, MAX)
- Join-heavy analytical queries
- Data quality validation queries
- Reusable SQL views
- Stored functions for parameterized reports
- Query optimization using indexes and EXPLAIN ANALYZE

### SQL Query Examples

![SQL Query 1](screenshots/sql_query.png)

![SQL Query 2](screenshots/sql_query_2.png)

![SQL Query 3](screenshots/sql_query-3.png)
---

## 🧪 Verification

System correctness was verified through:

- ETL execution logs
- SQL row-count and integrity checks
- Real-time Google Sheets auto-registration
- Database query verification
- Enforcement of constraints and indexes

---

## ⚠️ Notes

- Database credentials are never committed to GitHub
- ngrok is used only during development to expose the local backend
- NeonDB access remains restricted to the project owner

---

## 🎯 Future Improvements

- Production deployment
- Authentication & role-based access
- Interactive dashboards
- Incremental streaming ingestion
- CI/CD pipeline integration

---

## ✅ Assignment Status

- ✔ Environment Setup
- ✔ Data Audit & Assessment
- ✔ Database Design & ER Diagram
- ✔ ETL Pipeline
- ✔ SQL Development & Optimization
- ✔ Google Apps Script Automation
- ✔ Documentation
- ✔ Final Presentation

---

## 📎 Resources

- **NeonDB:** https://neon.tech
- **PostgreSQL:** https://www.postgresql.org/
- **Google Apps Script:** https://developers.google.com/apps-script

---

## 👤 Author

**Gauri Shukla**

