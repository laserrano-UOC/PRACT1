import requests
from bs4 import BeautifulSoup
import csv

# URL base del sitio web
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
BOOK_BASE_URL = "https://books.toscrape.com/catalogue/"

# Lista para almacenar los datos de los libros
books_data = []

# Recorremos las primeras 5 páginas del catálogo
for page_num in range(1, 6):
    url = BASE_URL.format(page_num)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontramos todos los contenedores de libros
    articles = soup.find_all('article', class_='product_pod')

    # Extraemos los datos de cada libro
    for article in articles:
        # Título del libro
        title = article.h3.a['title']

        # Precio del libro (convertido correctamente a UTF-8)
        price_raw = article.find('p', class_='price_color').text.strip()
        price = price_raw.encode('latin1').decode('utf-8')

        # Disponibilidad del libro
        availability = article.find('p', class_='instock availability').text.strip()

        # Calificación por estrellas (por ejemplo: One, Two, Three...)
        star_rating = article.p.get('class')[1]

        # URL de la imagen de portada
        image_url = "https://books.toscrape.com/" + article.find('img')['src'].replace('../', '')

        # URL relativa y absoluta del libro
        book_relative_url = article.h3.a['href']
        book_url = BOOK_BASE_URL + book_relative_url

        # Visitamos la página de detalle del libro para obtener la categoría
        book_response = requests.get(book_url)
        book_response.raise_for_status()
        book_soup = BeautifulSoup(book_response.text, 'html.parser')

        # Extraemos la categoría desde la ruta de navegación (breadcrumb)
        breadcrumb = book_soup.select('ul.breadcrumb li a')
        category = breadcrumb[2].text.strip() if len(breadcrumb) > 2 else 'Unknown'

        # Añadimos los datos del libro a la lista
        books_data.append({
            'Título': title,
            'Precio': price,
            'Disponibilidad': availability,
            'Calificación': star_rating,
            'Categoría': category,
            'URL_Imagen': image_url,
            'URL_Libro': book_url
        })

# Guardamos los datos en un archivo CSV
csv_file = 'books_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['Título', 'Precio', 'Disponibilidad', 'Calificación', 'Categoría', 'URL_Imagen', 'URL_Libro']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(books_data)

print(f"Scraping completado. Datos guardados en {csv_file}.")