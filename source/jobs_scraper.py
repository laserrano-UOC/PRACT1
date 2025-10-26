import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ==========================================
# CONFIGURACIÓN DEL NAVEGADOR
# ==========================================
chrome_opts = Options()
chrome_opts.add_argument("--headless=new")
chrome_opts.add_argument("--no-sandbox")
chrome_opts.add_argument("--disable-gpu")
chrome_opts.add_argument("--window-size=1920,1080")
chrome_opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

driver = webdriver.Chrome(options=chrome_opts)

# ==========================================
# PARÁMETROS DE BÚSQUEDA
# ==========================================
keyword = "data analyst"
location = "España"
base_url = f"https://es.indeed.com/jobs?q={keyword}&l={location}&start={{}}"

# ==========================================
# LISTA DE RESULTADOS
# ==========================================
ofertas = []

# ==========================================
# SCRAPING
# ==========================================
for page in range(0, 50, 10):  # Indeed usa saltos de 10 resultados por página
    url = base_url.format(page)
    print(f"📄 Extrayendo resultados desde: {url}")
    driver.get(url)
    time.sleep(4)

    # Cada oferta está dentro de un div con data-jk
    job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")

    print(f"   → Ofertas encontradas en esta página: {len(job_cards)}")

    for card in job_cards:
        try:
            title_elem = card.find_element(By.CSS_SELECTOR, "h2.jobTitle span")
            title = title_elem.text.strip()

            try:
                company = card.find_element(By.CSS_SELECTOR, "span[data-testid='company-name']").text.strip()
            except:
                company = "No disponible"

            try:
                location = card.find_element(By.CSS_SELECTOR, "div[data-testid='text-location']").text.strip()
            except:
                location = "No disponible"

            try:
                salary = card.find_element(By.CSS_SELECTOR, "div[data-testid='attribute_snippet_testid']").text.strip()
            except:
                salary = "No disponible"

            try:
                summary = card.find_element(By.CSS_SELECTOR, "div.job-snippet").text.strip().replace("\n", " ")
            except:
                summary = "No disponible"

            try:
                job_id = card.get_attribute("data-jk")
                link = f"https://es.indeed.com/viewjob?jk={job_id}"
            except:
                link = "No disponible"

            ofertas.append({
                "titulo": title,
                "empresa": company,
                "ubicacion": location,
                "salario": salary,
                "descripcion": summary,
                "url": link
            })

        except Exception as e:
            print("   ⚠️ Error leyendo una oferta:", e)

    time.sleep(5)  # pausa entre páginas

driver.quit()

# ==========================================
# GUARDAR RESULTADOS
# ==========================================
df = pd.DataFrame(ofertas)
df.to_csv("dataset/indeed_ofertas.csv", index=False, encoding="utf-8")

print(f"\n✅ Extracción completada. Total ofertas: {len(df)}")
