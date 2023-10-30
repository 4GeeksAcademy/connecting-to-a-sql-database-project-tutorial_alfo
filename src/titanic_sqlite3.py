import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv', sep =',')
# print(df)

import sqlite3 as sq

con = sq.connect("titanic.db")

df.to_sql('titanic', con, if_exists='replace', index=True)


# Responder a las siguientes preguntas usando SQL sobre la tabla que acabáis de crear:
# Cuántos supervivientes hay (columna Survived)
# De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)
# Cuál es el valor del ticket más caro que se compró (columna Fare)

cursor = con.cursor()
cursor.execute("""SELECT COUNT(*) as Total_survived
              FROM titanic
              WHERE Survived = "1"
              """)

# Obtener el resultado
resultado = cursor.fetchone()

# Imprimir la columna calculada
total_survived = resultado[0]
print(f"Total Survived: {total_survived}")

cursor.execute("""SELECT COUNT(*) as Men
              FROM titanic
              WHERE Sex = "male"
              """)

# Obtener el resultado
resultado = cursor.fetchone()

# Imprimir la columna calculada
men = resultado[0]
print(f"Men: {men}")

cursor.execute("""SELECT COUNT(*) as Women
              FROM titanic
              WHERE Sex = "female"
              """)

# Obtener el resultado
resultado = cursor.fetchone()

# Imprimir la columna calculada
women = resultado[0]
print(f"Women: {women}")

cursor.execute("""SELECT fare
              FROM titanic
              ORDER BY fare DESC
              LIMIT 1
              """)

# Obtener el resultado
resultado = cursor.fetchone()

# Imprimir la columna calculada
highest_fare = resultado[0]
print(f"Highest Fare: {highest_fare}")


