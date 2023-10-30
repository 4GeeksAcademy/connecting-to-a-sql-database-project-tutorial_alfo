import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Generate connection with .env
con = psycopg2.connect(host = "localhost",
    user = "gitpod", 
    password = "postgres",
    database = "titanic_post", 
)

# Create a cursor object
cur = con.cursor()

# Import the .csv into pandas
df = pd.read_csv(
    'https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv', sep =','
    )

# Create an engine
engine = create_engine('postgresql+psycopg2://gitpod:postgres@localhost/titanic_post')

# Convert DataFrame into SQL
table_name = 'titanic_table'
df.to_sql(table_name, engine, if_exists='replace', index=False)

# Responder a las siguientes preguntas usando SQL sobre la tabla que acabáis de crear:
# Cuántos supervivientes hay (columna Survived)
# De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)
# Cuál es el valor del ticket más caro que se compró (columna Fare)

# Query total survivors
cur.execute("""SELECT COUNT(*) as Total_survived
              FROM titanic_table
              WHERE "Survived" = 1
              """)

# Get one result
resultado = cur.fetchone()

# Print the first column
total_survived = resultado[0]
print(f"Total Survived: {total_survived}")

# Query total gender
cur.execute("""SELECT "Sex", COUNT(*) as Total_gender
              FROM titanic_table
              GROUP BY "Sex"
              """)

# Get 2 results
resultado = cur.fetchmany(2)

#  Print the first and the second column
total_gender = resultado[0], resultado [1]
print(f"Total Genders: {total_gender}")

# Query the maximal Fare
cur.execute("""SELECT MAX("Fare") 
              FROM titanic_table
              """)

# Get one result
resultado = cur.fetchone()

# Print first column
max_fare = resultado[0]
print(f"Highest Fare: {max_fare}")

