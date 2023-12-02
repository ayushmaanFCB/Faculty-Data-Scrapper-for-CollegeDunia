from scrapper import scrap_college_dunia
from college_links_generator import generate_statewise_links
import pandas as pd

url = "https://collegedunia.com/btech/tripura-colleges"
final_data = []


links = generate_statewise_links(url)


for link in links:
    scrapped_data = scrap_college_dunia(link)
    print(scrapped_data)
    for d in scrapped_data:
        final_data.append(d)

data_df = pd.DataFrame(final_data)
data_df.to_excel("./data/tripura.xlsx")
