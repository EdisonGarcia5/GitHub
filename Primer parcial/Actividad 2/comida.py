import requests
from bs4 import BeautifulSoup
import json

# URL de la página
url = "https://www.foodspring.es/magazine/alimentos-ricos-en-proteina"

# Obtener el contenido de la página
response = requests.get(url)
html_content = response.content

# Analizar el contenido HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar la tabla (ajusta el selector según la estructura de la página)
table = soup.find('table')

# Extraer datos de la tabla
data = []
for row in table.find_all('tr'):
    cols = row.find_all(['td', 'th'])
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Crear una lista de diccionarios
json_data = []
for row in data[1:]:
    json_data.append(dict(zip(data[0], row)))

# Guardar la lista de diccionarios en un archivo JSON
with open('tabla_comida.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print("Tabla extraída y guardada como 'tabla_comida.json'")
