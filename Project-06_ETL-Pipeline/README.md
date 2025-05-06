# 🛠️ Project 06: ETL Pipeline with Python + PostgreSQL

A real-world end-to-end ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL to process over 19,000 job postings. Data was cleaned, transformed, and loaded into a PostgreSQL database table for future analysis.

---

## 📂 Folder Contents

- `jobposts.csv` – Raw dataset downloaded from Kaggle
- `etl_script.py` – Python script for ETL process
- `ERD.png` – ER diagram of the final database schema
- `screenshot_pgadmin.png` – Proof of data loaded in PostgreSQL
- `README.md` – Project overview and steps followed

---

## 🛠️ Tools Used

- Python (pandas, psycopg2, tqdm)
- PostgreSQL
- pgAdmin 4
- dbdiagram.io (for ER diagram)
- Git + GitHub

---

## 📌 Key Tasks Performed

### ✅ 1. Extract
- Loaded the job posts dataset using pandas
- Handled file encoding and header mismatches

### ✅ 2. Transform
- Cleaned column names (standardized to snake_case)
- Converted missing values (`NaN`, `NaT`) to `None`
- Trimmed to 23 required columns
- Validated data types before load

### ✅ 3. Load
- Connected to PostgreSQL using `psycopg2`
- Inserted all 19,001 rows into `job_postings` table
- Handled row-level errors with try-except blocks
- Verified success via pgAdmin

---

## 📸 Sample Output Preview

📷 Screenshot of table in pgAdmin available in: `screenshot_pgadmin.png`

📊 ER Diagram of the table schema available in: `ERD.png`

---

## 🔗 Dataset Source

[Kaggle – Online Job Postings](https://www.kaggle.com/datasets/PromptCloudHQ/online-job-postings)

---

## 🙌 Author

**Akhil**  
*Master’s in Data Science & Analytics (Florida Atlantic University)*  
[GitHub Profile](https://github.com/akhil0404-tech)
