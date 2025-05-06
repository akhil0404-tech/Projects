#!/usr/bin/env python
# coding: utf-8

# In[64]:


# etl_pipeline.py

import pandas as pd
import psycopg2
from psycopg2 import sql
import os

# Set up database connection
conn = psycopg2.connect(
    host="localhost",
    database="job_etl",      
    user="postgres",     
    password="Akhil@0499",
    port="5432"
)

cur = conn.cursor()
print("Connected to PostgreSQL!")


# In[40]:


# Step 2: Load and preview CSV data
# -------------------------------

import pandas as pd

# Since the CSV is in the same folder as this script
csv_path = "jobposts.csv"

# Load CSV into a pandas DataFrame
df = pd.read_csv(csv_path)

# Print basic info and first few rows
print(" CSV Loaded Successfully!")
print(" Shape of dataset:", df.shape)
print(" Columns:")
print(df.columns.tolist())




# In[41]:


print(df.head())


# In[42]:


# -------------------------------
# Step 3: Clean and Prepare the Data
# -------------------------------

# 1. Lowercase + clean all column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w_]", "", regex=True)

# 2. Rename specific columns to match PostgreSQL table
df = df.rename(columns={
    "announcementcode": "announcement_code",
    "jobrequirment": "job_requirement",
    "requiredqual": "required_qual",
    "applicationp": "application_procedure",
    "aboutc": "about_company",
    "startdate": "start_date",
    "jobdescription": "job_description",
    "openingdate": "opening_date"
})

# 3. Convert 'date' to proper datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 4. Convert 'year' and 'month' to integers
df['year'] = pd.to_numeric(df['year'], errors='coerce').fillna(0).astype(int)
df['month'] = pd.to_numeric(df['month'], errors='coerce').fillna(0).astype(int)

# 5. Fill all NaNs with empty string (safer for inserts)
df = df.fillna("")

# 6. Confirm column structure
print("Cleaned Column Names:")
print(df.columns.tolist())
print("Cleaned Data Preview:")
print(df.head(3))


# In[43]:


#  Keep only these 23 columns in exact order for PostgreSQL
required_columns = [
    'jobpost', 'date', 'title', 'company', 'announcement_code', 'term', 'eligibility',
    'audience', 'start_date', 'duration', 'location', 'job_description', 'job_requirement',
    'required_qual', 'salary', 'application_procedure', 'opening_date', 'deadline', 'notes',
    'about_company', 'attach', 'year', 'month', 'it'
]

df = df[required_columns]



# In[45]:


print("Final DataFrame shape:", df.shape)
print("Final DataFrame columns:")
for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")


# In[47]:


print("\n DEBUG: Column value types in row 0:")
for col in df.columns:
    print(f"{col}: {df[col].iloc[0]} (type: {type(df[col].iloc[0])})")


# In[48]:


required_columns = [
    'jobpost', 'date', 'title', 'company', 'announcement_code', 'term', 'eligibility',
    'audience', 'start_date', 'duration', 'location', 'job_description', 'job_requirement',
    'required_qual', 'salary', 'application_procedure', 'opening_date', 'deadline', 'notes',
    'about_company', 'attach', 'year', 'month', 'it'
]

# Force only these 23, no matter how crazy jobpost is
df = df.loc[:, required_columns].copy()

# Double-check before inserting
print("FINAL column count:", df.shape)
print("First row type:", type(df.iloc[0]['jobpost']))


# In[49]:


data_tuples = [tuple(row) for row in df.itertuples(index=False)]


# In[ ]:





# In[29]:


print("Number of columns in DataFrame:", len(df.columns))
print("DataFrame columns:", df.columns.tolist())


# In[30]:


# Debug: Check column count and names before inserting into DB
print("Number of columns in DataFrame:", len(df.columns))
print("DataFrame columns:")
for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")


# In[31]:


df = df.rename(columns={"applicationp": "application_procedure"})


# In[32]:


df = df.rename(columns={
    "announcementcode": "announcement_code",
    "jobrequirment": "job_requirement",
    "requiredqual": "required_qual",
    "aboutc": "about_company"
})


# In[33]:


print(" Final column count:", len(df.columns))
print(df.columns.tolist())


# In[65]:


#  Keep only 23 required columns
required_columns = [
    'date', 'title', 'company', 'announcement_code', 'term', 'eligibility',
    'audience', 'start_date', 'duration', 'location', 'job_description', 'job_requirement',
    'required_qual', 'salary', 'application_procedure', 'opening_date', 'deadline', 'notes',
    'about_company', 'attach', 'year', 'month', 'it'
]

df = df.loc[:, required_columns].copy()
print(" DataFrame trimmed to 23 columns:", df.shape)

#  Convert NaT/NaN to None for PostgreSQL NULL compatibility
df = df.where(pd.notnull(df), None)

#  Convert DataFrame to list of tuples (safe for insert)
data_tuples = df.values.tolist()
print("Sample row length:", len(data_tuples[0]))  # Should be 23


# In[73]:


import psycopg2
import pandas as pd
from tqdm import tqdm

#  1. Define the exact 24 column names (No 'jobpost')
required_columns = [
    'date', 'title', 'company', 'announcement_code', 'term', 'eligibility',
    'audience', 'start_date', 'duration', 'location', 'job_description', 'job_requirement',
    'required_qual', 'salary', 'application_procedure', 'opening_date', 'deadline', 'notes',
    'about_company', 'attach', 'year', 'month', 'it'
]

# 2. Trim to required columns
df = df.loc[:, required_columns].copy()
print(" Trimmed to 23 columns:", df.shape)

#  3. Replace NaN and NaT with None (PostgreSQL will treat as NULL)
df = df.where(pd.notnull(df), None)

#  4. Convert to list of row tuples
data_tuples = df.values.tolist()
print(" Sample row length:", len(data_tuples[0]))  # should be 23

#  5. Reconnect to PostgreSQL
try:
    conn = psycopg2.connect(
        host="localhost",
        database="job_etl",        # change if needed
        user="postgres",           # your PostgreSQL username
        password="Akhil@0499",       # your PostgreSQL password
        port="5432"
    )
    print(" PostgreSQL connection successful")
except Exception as e:
    print(f" Connection failed: {e}")
    raise

#  6. Define the INSERT query (exactly 23 placeholders)
insert_query = """
    INSERT INTO job_postings (
        date, title, company, announcement_code, term, eligibility,
        audience, start_date, duration, location, job_description, job_requirement,
        required_qual, salary, application_procedure, opening_date, deadline, notes,
        about_company, attach, year, month, it
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

#  7. Insert the rows
inserted_rows = 0
failed_rows = 0

try:
    cur = conn.cursor()
    print(" Inserting rows into PostgreSQL...")

    for idx, row in tqdm(enumerate(data_tuples), total=len(data_tuples)):
        try:
            cur.execute(insert_query, row)
            inserted_rows += 1
        except Exception as e:
            print(f" Row {idx} insert failed: {e}")
            conn.rollback()  # rollback only this failed one
            failed_rows += 1

    conn.commit()
    cur.close()
    conn.close()
    print("\n Insert complete!")
    print(f"Rows inserted: {inserted_rows}")
    print(f" Rows failed: {failed_rows}")

except Exception as e:
    print(f" PostgreSQL insertion failed: {e}")


# In[72]:


# Convert NaT to string 'NaT', then replace all 'NaT' or NaN with None
df = df.astype(object).where(pd.notnull(df), None)



# In[ ]:




