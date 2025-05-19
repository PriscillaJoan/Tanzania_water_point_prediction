import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

DB_NAME = "wells"
DB_USER = "postgres"
DB_PASSWORD = "0721711644"
DB_HOST = "localhost"
DB_PORT = 5432

# load CSV
df = pd.read_csv('wells_data.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# log missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

#standardize casing and whitespace
text_columns = ['status_group', 'funder', 'installer', 'basin', 'region', 'lga', 'ward',
                'extraction_type', 'management', 'payment', 'water_quality', 'quantity', 'source', 'waterpoint_type']

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

# Normalize status to Title
df['status_group'] = df['status_group'].astype(str).str.strip().str.title()

#fix the booleon field casing
df['public_meeting'] = df['public_meeting'].astype(str).str.strip().str.upper().map({'TRUE': True, 'FALSE': False})
df['permit'] = df['permit'].astype(str).str.strip().str.upper().map({'TRUE': True, 'FALSE': False})

# fill optional columns, drop rows with critical nulls
df['funder'] = df['funder'].fillna('Unknown')
df['installer'] = df['installer'].fillna('Unknown')
df.dropna(subset=['id', 'longitude', 'latitude'], inplace=True)

print("Data cleaned. Sample:")
print(df.head())

# insert cleaned data into PostgreSQL
db_port = int(DB_PORT) if DB_PORT else 5432
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=db_port
)
cur = conn.cursor()

# get existing ids from wells table
cur.execute("SELECT id FROM wells")
existing_ids = set(row[0] for row in cur.fetchall())

#filter new rows not in the db
new_rows = df[~df['id'].isin(existing_ids)]

print(f"Found {len(new_rows)} new rows to insert.")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO wells(
            id, status_group, amount_tsh, funder, gps_height, installer,
            longitude, latitude, basin, region, lga, ward, population,
            public_meeting, permit, extraction_type, management, payment,
            water_quality, quantity, source, waterpoint_type
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()
print("Data inserted into PostgreSQL successfully.")
