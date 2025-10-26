# M2.851 - Tipología y Ciclo de Vida de los Datos - Práctica 1

## Integrantes del Grupo

* **Integrante 1:** Xavier Cortes Marsa
* **Integrante 2:** Luis Alfonso Serrano Valcárcel

---

## Título del Dataset

Ofertas de Empleo para Data Analyst en España (Indeed)

## Sitio Web Elegido

**URL:** https://es.indeed.com/
**Idioma:** Español

---

## Descripción de los Archivos del Repositorio

Este repositorio contiene los elementos esenciales de la Práctica 1:

| Archivo/Carpeta | Contenido | Descripción |
| :--- | :--- | :--- |
| `README.md` | Documentación del proyecto. | Documento actual con la información necesaria para replicar la práctica. |
| `requirements.txt` | Dependencias de Python. | Lista las librerías necesarias con sus versiones para recrear el entorno. |
| **`/source`** | Código fuente en Python. | Contiene el script principal para la extracción de datos. |
| **`/dataset`** | Dataset resultante. | Contiene el archivo **`indeed_ofertas.csv`**, el conjunto de datos obtenido tras la ejecución del script. |

---

## ⚙️ Uso del Código (Web Scraper)

El script implementado utiliza **Selenium** para la extracción de ofertas de empleo del portal Indeed, permitiendo la navegación autónoma entre las páginas de resultados.

### Requisitos Previos

1.  **Clonar el repositorio:**
    ```bash
    git clone PRACT1
    cd PRACT1
    ```
2.  [cite_start]**Crear y activar el entorno virtual** (recomendado, aunque no obligatorio [cite: 111]):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # .\venv\Scripts\activate   # En Windows
    ```
3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución del Script

El script principal se encuentra en la carpeta `/source` y acepta parámetros de línea de comandos para la palabra clave y la ubicación de la búsqueda.

#### Parámetros del Script

| Parámetro | Descripción | Valor por Defecto |
| :--- | :--- | :--- |
| **`--keyword`** | La palabra clave o cargo a buscar. | `"data analyst"` |
| **`--location`** | La ubicación geográfica de las ofertas. | `"España"` |
| **`--max-pages`** | Número máximo de páginas (saltos de 10 resultados) a extraer (e.g., 50 resultados = 5 páginas). | `5` |

#### [cite_start]Ejemplos Replicables de Uso [cite: 175]

1.  **Ejecución con parámetros por defecto** (busca 'data analyst' en 'España', 50 resultados):
    ```bash
    python3 source/nombre_de_su_script.py
    ```

2.  **Búsqueda específica** (busca 'data scientist' en 'Madrid', 100 resultados):
    ```bash
    python3 source/nombre_de_su_script.py --keyword "data scientist" --location "Madrid" --max-pages 10
    ```

El script guardará automáticamente el dataset resultante en la carpeta `/dataset` con el nombre `indeed_ofertas.csv`.

---

## 🔗 Enlace al Dataset en Zenodo

El dataset obtenido de este proyecto ha sido publicado en Zenodo para su acceso abierto (o simulado, si aplica).

**DOI de Zenodo:** `https://doi.org/10.5281/zenodo.17450003`