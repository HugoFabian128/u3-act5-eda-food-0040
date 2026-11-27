import pandas as pd
import matplotlib.pyplot as plt
# Hugo Fabian NC 0040
# 1. Leer el archivo CSV comida pais india
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEIOS DESDE CSV, comida india 0040---")
print(df_food_india)
print("\n--- mostrar nombre comida + ingredientes 0040---")
recetas = df_food_india[["name", "ingredients"]]
print(recetas)
print("\n--- tiempo de cocinado mostrar registros con head 0040---")
nombre_y_hora = df_food_india[["name", "cook_time"]].head(10)
print(nombre_y_hora)
print("\n--- Grafica comida(X) tiempo de cocinado (y)---")
print("\n--- Grafica comida (x) texto a 30 grados---")
nombre_y_hora.plot.bar(x="name", y="cook_time", rot=30)
plt.title("comida tipica de india Hugo 0040")
plt.xlabel("nombre platillo")
plt.ylabel("tiempo cocinado")
plt.show()

































