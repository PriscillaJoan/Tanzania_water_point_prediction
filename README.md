# Predicting Functional Status Of Water Wells In Tanzania

## Repository Structure

-**Data Folder**: Contains original and cleaned training and testing datasets, along with predicted well functionality results.

- **Final workbook.ipynb**: Jupyter notebook containing the whole workflow: data transformation,EDA and Modelling
  
- **TANZANIA WATER WELLS PREDICTIONS.pdf:** pdf version of project presentation slides
  
- **Wells table creation.sql:** SQL script for creating the water wells table
  
- **Images** : C Contains interactive HTML visualizations generated in the notebook, showing distributions and mapping of water wells in Tanzania.
  
- **pictures**: Contains static images used in the pdf presentation
  
- **Water wells automation**: 
  
| File                     | Description                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------|
| `.env`                   | Stores PostgreSQL credentials securely                                                      |
| `automate_waterwells.py`| Python script to load, clean, validate, and insert new wells data into PostgreSQL database   |
| `wells_data.xlsx`        | Raw input Excel file containing water well records                                           |
| `Audit Table Creation.sql` | SQL script that creates an audit log table used to record when and what data is inserted into the database|
| `creation.sql`| SQL script that defines the schema for the `wells_data` table|


### Key Automation Steps:
- Cleans and standardizes column values 
- Validates required fields
- Automatically inserts cleaned data into a structured PostgreSQL table
- Designed to be modular and run multiple times with different datasets
  
## Business problem
>
By leveraging data driven methods, this study aims to forecast the current functional condition of Tanzanian water wells, using machine learning classification algorithms trained on historical and environmental data such as location, installation details, water quality, management structure, and construction parameters.
The outcome of this model has practical implications: it enables decision-makers, NGOs, and local governments to be proactive in prioritizing and improving the long term water accessibility for communities across tanzania through maintenance efforts and  allocation of resources efficiently.

## Data
>
The data used for this project is from the Data Driven website. The link to the website to obtain the data for yourself is: <https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/>

## Approach
>
This project followed a structured data science workflow. I began by cleaning and preprocessing the data to ensure quality and consistency. Exploratory data analysis (EDA) was conducted to understand key patterns and relationships. I then applied classification algorithms to predict the functional status of water wells in Tanzania, optimizing model performance using cross-validation and relevant evaluation metrics. The results were visualized using dashboards to provide actionable insights.

