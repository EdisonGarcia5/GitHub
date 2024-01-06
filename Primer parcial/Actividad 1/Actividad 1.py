import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://pueblosoriginarios.com/lenguas/mayas.php'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'diccionario'})

    rows = table.find_all('tr')

    diccionario_data = []

    for row in rows[1:]:
        cols = row.find_all('td')

        if len(cols) == 2:
          maya_word = cols[0].text.strip()
          spanish_word = cols[1].text.strip()
          diccionario_data.append({'Maya': maya_word, 'Español': spanish_word})
    
    # Guardar en un archivo Excel
    df = pd.DataFrame(diccionario_data)
    df.to_excel('diccionario_maya.xlsx', index=False, encoding='utf-8')

    print("Datos extraídos y guardados en diccionario_maya.xlsx")

else:
    print("Error al conectarse a la web")

