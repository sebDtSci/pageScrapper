# Les imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')
import pandas as pd

import sys
sys.path.append("../loader")
# from loaderA import goodLoader
import loaderA as lo


# Les fonctions
def scrap(url):
    #for elem in url:
    driver.get(url)
    list_category_elements = driver.find_element(By.XPATH,'/html/body')
        # nom = list_category_elements.find_elements(By.CLASS_NAME, 'actor-item-title')
    nom = list_category_elements.find_elements(By.CSS_SELECTOR, 'p')
    text=[]
    name=[]
    for i in range(len(nom)):
        name.append(nom[i].text)
    text.append(" ".join(name))
    return text

# recup l'url
url = str(input("Entrez l\' URL de la page souhaité: "))
nameOutput = str(input("Entrez le nom du fichier que vous voulez en sortie: "))
# Load bar
# lo.goodLoader('dots', 'red')
lo.classicLoader()

# Installation du driver
driver = webdriver.Chrome('chromedriver', options=options, service= Service(ChromeDriverManager().install()))
# Scrap
res = scrap(url)

df = pd.DataFrame(res, columns = ['Text'])
df.to_csv(f"{nameOutput}.csv", index=False)
# spinner.end()
