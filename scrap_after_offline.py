from scrapper import scrap_college_dunia
import pandas as pd

location = "karnataka"
links = []
final_data = []

with open(f"./links/{location}.txt", "r", encoding='utf-8') as file:
    for line in file:
        links.append(line.strip())

links = links[150:]
count = 0

try:
    try:
        for link in links:
            count = count + 1
            scrapped_data = scrap_college_dunia(link)
            print(f"\n\n\033[1;32;40m{count}\033[m")
            print(scrapped_data)
            for d in scrapped_data:
                final_data.append(d)
        data_df = pd.DataFrame(final_data)
        data_df.to_excel(f"./data/{location}2.xlsx")
        print(
            f"\n\n\033[1;32;40mFaculty Details from {location.upper()} saved successfully !!!\033[m")
    except:
        data_df = pd.DataFrame(final_data)
        data_df.to_excel(f"./data/{location}2.xlsx")
        print(
            f"\n\n\033[1;32;40mFaculty Details from {location.upper()} saved successfully !!!\033[m")

except:
    print(
        "\n\n\033[1;31;40mSome Error occurred, check the input properly !!!\033[m")
