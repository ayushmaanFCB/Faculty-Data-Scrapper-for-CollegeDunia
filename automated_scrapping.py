import pandas as pd

try:
    from scrapper import scrap_college_dunia
    from college_links_generator import generate_statewise_links
    print("\033[1;32;40m\n\nDrivers installed and Loaded successfully !!!\033[m")

except:
    print(
        "\n\n\033[1;31;40mSome Error occurred, check Internet Connection and make sure you have Chrome !!!\033[m")

location = "tamil-nadu"

# for location in ("maharashtra", "andhra-pradesh", "karnataka", "kerala", "west-bengal", "telangana", "delhi-ncr"):
final_data = []
url = f"https://collegedunia.com/btech/{location.lower()}-colleges"

try:
    links = generate_statewise_links(url)

    for link in links:
        print(link)
        scrapped_data = scrap_college_dunia(link)
        print(scrapped_data)
        for d in scrapped_data:
            final_data.append(d)

    data_df = pd.DataFrame(final_data)
    data_df.to_excel(f"./data/{location}.xlsx")
    print(
        f"\n\n\033[1;32;40mFaculty Details from {location} saved successfully !!!\033[m")

except:
    print(
        f"\n\n\033[1;31;40mSome Error occurred, check the input for {location.lower()} properly !!!\033[m")
