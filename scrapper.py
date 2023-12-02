from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())


def scrap_college_dunia(url):
    data = []
    driver.get(url)
    content = bs(driver.page_source, 'html.parser')

    records = content.find_all(
        "div", class_="jsx-2968715513 faculty-card d-flex align-items-start p-2")

    for x in records:
        if x.find("p", class_="jsx-2968715513 deprt text-primary font-weight-bold text-capitalize text-md mb-1") != None:
            department = x.find(
                "p", class_="jsx-2968715513 deprt text-primary font-weight-bold text-capitalize text-md mb-1").text.strip()

            keywords = ('computer science', 'computer', 'ece', 'ee', 'electronics',
                        'electricals', 'technology', 'engineering', 'biotechnology')
            res = any(ele in department for ele in keywords)

            if res:
                name = x.find(
                    "h5", class_="jsx-2968715513 name text-success font-weight-bold text-capitalize mb-1").text.strip()

                if content.find(id="collegePageTitle") != None:
                    univ = content.find(id="collegePageTitle").text.strip(
                        ' - List of Professors and Faculty ')
                else:
                    univ = ""
                if content.find("span", class_="jsx-201813991 text-white text-capitalize font-weight-medium text-md") != None:
                    location = content.find(
                        "span", class_="jsx-201813991 text-white text-capitalize font-weight-medium text-md").text.strip()
                else:
                    location = ""

                if x.find("p", class_="jsx-2968715513 email text-secondary font-weight-bold text-capitalize text-md mb-1 d-flex") != None:
                    email = x.find(
                        "p", class_="jsx-2968715513 email text-secondary font-weight-bold text-capitalize text-md mb-1 d-flex").text.strip('Email - ')
                else:
                    email = ""

                data.append(
                    {
                        'name': name,
                        'department': department,
                        'email': email,
                        'college': univ,
                        'location': location
                    }
                )
    return data


# if __name__ == '__main__':
#     scrapped_data = scrap_college_dunia(
#         "https://collegedunia.com/university/28330-indian-institute-of-engineering-science-and-technology-iiest-shibpur-howrah/faculty")
#     print(scrapped_data)

#     data_df = pd.DataFrame(scrapped_data)
#     data_df.to_excel("./scrapped.xlsx")
