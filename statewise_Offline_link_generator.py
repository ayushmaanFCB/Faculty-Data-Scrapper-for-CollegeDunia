from bs4 import BeautifulSoup as bs

location = 'karnataka'

with open(f"./templates/{location}.html", "r", encoding='utf-8') as file:
    html_content = file.read()

content = bs(html_content, 'html.parser')

college_links = []
college_links_anchors = content.find_all(
    "a", class_="jsx-3462784614 college_name underline-on-hover")

for a in college_links_anchors:
    print(a['href'])
    college_links.append(a['href']+"/faculty")

try:
    with open(f"./links/{location}.txt", "w") as file:
        for college_link in college_links:
            file.write(str(college_link)+"\n")
    print(
        f"\n\n\033[1;32;40mCollege Links from {location} saved successfully !!!\033[m")
except:
    print(
        "\n\n\033[1;31;40mSome Error occurred, check the input properly !!!\033[m")
