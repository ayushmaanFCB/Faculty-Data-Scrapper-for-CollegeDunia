import gradio as gr
import pandas as pd


try:
    from scrapper import scrap_college_dunia
    from college_links_generator import generate_statewise_links
    print("\033[1;32;40m\n\nDrivers installed and Loaded successfully !!!\033[m")

except:
    print(
        "\n\n\033[1;31;40mSome Error occurred, check Internet Connection and make sure you have Chrome !!!\033[m")


def scrap(input):
    final_data = []
    url = f"https://collegedunia.com/btech/{input.replace(' ','-').lower()}-colleges"
    links = generate_statewise_links(url)
    for link in links:
        scrapped_data = scrap_college_dunia(link)
        print(scrapped_data)
        for d in scrapped_data:
            final_data.append(d)
    data_df = pd.DataFrame(final_data)
    return data_df


choice_states = ["TAMIL NADU", "ANDHRA PRADESH",
                 "TELANGANA", "KERALA", "KARNATAKA", "WEST BENGAL", "MIZORAM"]
choice_states.sort()


with gr.Blocks() as main_block:
    with gr.Row():
        gr.HTML(
            "<h1 style='text-align:center'>FACULTY DATA SCRAPPER (from <a href='https://collegedunia.com'>CollegeDunia</a>)</h1><hr>"
        )
    with gr.Row():
        with gr.Column():
            state = gr.Dropdown(
                choices=choice_states
            )
        with gr.Column():
            scrap_btn = gr.Button(value="SCRAP")
    with gr.Row():
        scrap_btn.click(
            fn=scrap,
            inputs=state,
            outputs=gr.DataFrame()
        )

main_block.launch()
