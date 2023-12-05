from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs


driver = webdriver.Chrome(ChromeDriverManager().install())


def generate_statewise_links(url):
    driver.get(url)

    def scroll_to_bottom():
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(2)

    while True:
        before_height = driver.execute_script(
            "return document.body.scrollHeight")
        scroll_to_bottom()

        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, "//*"))
        )

        after_height = driver.execute_script(
            "return document.body.scrollHeight")

        if before_height == after_height:
            break

    page_source = driver.page_source
    content = bs(page_source, 'html.parser')

    college_links = []
    college_links_anchors = content.find_all(
        "a", class_="jsx-3462784614 college_name underline-on-hover")

    for a in college_links_anchors:
        print(a['href'])
        college_links.append("https://collegedunia.com/"+a['href']+"/faculty")
    return college_links


# if __name__ == '__main__':
#     url = "https://collegedunia.com/btech/west-bengal-colleges"
#     links = generate_statewise_links(url)
#     with open('./links/west-bengal.txt', 'w') as f:
#         for line in links:
#             f.write(line + "\n")
