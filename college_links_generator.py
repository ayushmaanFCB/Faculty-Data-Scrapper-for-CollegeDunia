import requests
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def generate_statewise_links(url):
    driver.get(url)
    content = bs(driver.page_source, 'html.parser')

    college_links = []
    college_links_anchors = content.find_all(
        "a", class_="jsx-3462784614 college_name underline-on-hover")

    for a in college_links_anchors:
        college_links.append("https://collegedunia.com/"+a['href']+"/faculty")

    return college_links


# if __name__ == '__main__':
#     url = "https://collegedunia.com/btech/west-bengal-colleges"
#     links = generate_statewise_links(url)
#     with open('./links/west-bengal.txt', 'w') as f:
#         for line in links:
#             f.write(line + "\n")
