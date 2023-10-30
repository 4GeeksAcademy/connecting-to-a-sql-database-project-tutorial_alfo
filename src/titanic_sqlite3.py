import pandas as pd

# Import the .csv into pandas
df = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv', sep =',')
# print(df)

import sqlite3 as sq

# Create a Database as archive
con = sq.connect("titanic.db")

# Convert DataFrame into SQL
df.to_sql('titanic', con, if_exists='replace', index=True)


# Responder a las siguientes preguntas usando SQL sobre la tabla que acabáis de crear:
# Cuántos supervivientes hay (columna Survived)
# De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)
# Cuál es el valor del ticket más caro que se compró (columna Fare)

# Create a cursor object
cursor = con.cursor()

# Query total survivors
cursor.execute("""SELECT COUNT(*) as Total_survived
              FROM titanic
              WHERE Survived = "1"
              """)

# Get one result
resultado = cursor.fetchone()

# Print the first column
total_survived = resultado[0]
print(f"Total Survived: {total_survived}")

# Query the total men
cursor.execute("""SELECT COUNT(*) as Men
              FROM titanic
              WHERE Sex = "male"
              """)

# Get one result
resultado = cursor.fetchone()

# Print the first column
men = resultado[0]
print(f"Men: {men}")

# Query the total women
cursor.execute("""SELECT COUNT(*) as Women
              FROM titanic
              WHERE Sex = "female"
              """)

# Get one result
resultado = cursor.fetchone()

# Print the first column
women = resultado[0]
print(f"Women: {women}")

# Query the maximal Fare
cursor.execute("""SELECT fare
              FROM titanic
              ORDER BY fare DESC
              LIMIT 1
              """)

# Get one result
resultado = cursor.fetchone()

# Print the first column
highest_fare = resultado[0]
print(f"Highest Fare: {highest_fare}")


