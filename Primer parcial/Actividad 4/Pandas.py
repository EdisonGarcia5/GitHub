import pandas as pd
import json

# Cargar klos datos desde el archivo json
with open('diccionario_maya.json', 'r', encoding='utf-8') as file:
  diccionario_data = json.load(file)

# Crear un dataframe
df = pd.DataFrame(diccionario_data)

# 1.Estadistica descriptiva
descripcion_maya = df['Maya'].describe()
descripcion_espanol = df['Español'].describe()

print("Estadistica descriptiva de llas palabras Maya")
print(descripcion_maya)


# 2.filtrar datos

palabras_con_a = df[df['Maya'].str.startswith('a',na=False)]

print("palabras que cominesan con 'a' :")
print(palabras_con_a)

# 3.Ordenar datos

df_ordenado = df.sort_values(by='Maya',key=lambda x: x.str.len(), ascending=True)
print("Palabras ordenadas")
print(df_ordenado)

# 4. Contar duplicados

duplicados_maya = df[df.duplicated(subset='Maya', keep=False)]

print("Palabras que se duplican en Maya")
print(duplicados_maya)
