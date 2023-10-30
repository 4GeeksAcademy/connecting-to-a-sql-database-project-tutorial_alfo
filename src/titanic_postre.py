import psycopg2
import pandas as pd
from sqlalchemy import create_engine

con = psycopg2.connect(host = "localhost",
    user = "gitpod", 
    password = "postgres",
    database = "titanic_post", 
)

cur = con.cursor()

df = pd.read_csv(
    'https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv', sep =','
    )

engine = create_engine('postgresql+psycopg2://gitpod:postgres@localhost/titanic_post')

nombre_de_tabla = 'titanic_table'
df.to_sql(nombre_de_tabla, engine, if_exists='replace', index=False)

# Responder a las siguientes preguntas usando SQL sobre la tabla que acabáis de crear:
# Cuántos supervivientes hay (columna Survived)
# De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)
# Cuál es el valor del ticket más caro que se compró (columna Fare)

cur.execute("""SELECT COUNT(*) as Total_survived
              FROM titanic_table
              WHERE "Survived" = 1
              """)

# Obtener el resultado
resultado = cur.fetchone()

# Imprimir la columna calculada
total_survived = resultado[0]
print(f"Total Survived: {total_survived}")

cur.execute("""SELECT "Sex", COUNT(*) as Total_gender
              FROM titanic_table
              GROUP BY "Sex"
              """)

# Obtener el resultado
resultado = cur.fetchmany(2)

# Imprimir la columna calculada
total_gender = resultado[0], resultado [1]
print(f"Total Genders: {total_gender}")

cur.execute("""SELECT MAX("Fare") 
              FROM titanic_table
              """)

# Obtener el resultado
resultado = cur.fetchone()

# Imprimir la columna calculada
max_fare = resultado[0]
print(f"Highest Fare: {max_fare}")

