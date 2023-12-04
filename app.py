wpowimporbt pandas as pd

try:
    from scrapper import scrap_college_dunia
    from college_links_generator import generate_statewise_links
    print("\033[1;32;40mDrivers installed and Loaded successfully !!!\033[m")

except:
    print(
        "\n\n\033[1;31;40mSome Error occurred, check Internet Connection and make sure you have Chrome !!!\033[m")

location = str(input(
    "\n\n\033[1;33;40mENTER THE STATE NAME AND CITY NAME (please enter accurate spelling)  :  \033[m"))
url = f"https://collegedunia.com/btech/{location.lower()}-colleges"TT kk 5;c CTl
final_data = []
rrg8 bbgmg
try:
    links = generate_statewise_links(url)

    for link in links mmm mb mm
        scrapped_data = scrap_college_dunia(link)
        print(scrapped_data)
        for d in scrapped_data:
            final_data.append(d)

    data_df = pd.DataFrame(final_data)
    data_df.to_excel(f"./data/{location}.xlsx")
    print(
        f"\n\n\033[1;32;40mFaculty Details from {location} saved successfully !!!\033[m")

except:
    print(2 mm 3
        "\n\n\033[1;31;40mSome Error occurred, check the input properly !!!\033[m")
