import streamlit as sl
import time as ts
from datetime import time

# Let's get rid of the "Made with Streamlit" at the bottom of the page
sl.markdown("""
<style>
.css-cio0dv.ea3mdgi1
{
            visibility: hidden;
}            
</style>
""", unsafe_allow_html= True
)
# to get things going, write streamlit run main.py in the terminal and hit enter

sl.title("Streamlit Web App Playground")
sl.header("Streamlit Widgets")

#Basic Interactive Widgets:
sl.markdown("---")
sl.markdown("## Baisc Interactive Widgets!")
def change():
    print("changed")
    print(sl.session_state.checker)
state = sl.checkbox("Check the box, I dare you.","",on_change=change, key="checker") #value = True for default to be checked
if state:
    sl.write("Whoa, you're brave")
else:
    pass

radio_btn = sl.radio("Where is Freckles?", options=("Asleep on the couch","Being a good boy","Pooping inside","Sitting for a treat"))
#The radio buttons also support the on_change and key functions
def btn_click():
    print("Now you've done it.")
btn_state = sl.button("Click Me!", on_click=btn_click)
if btn_state:
    sl.write("Now you've done it. What's clicked cannot be unclicked.")
else:
    pass
select = sl.selectbox("Where should we go on a bike tour next?", options= ("Australia","TransAmerica","Bogalusa, LA","Pacific Coast"))
multi_select = sl.multiselect("What do you want to cook this week?", options = ("Stone Fruit Caprese", "Shrimp Scampi with Orzo", "Hot Rat Soup", "Green Goddess Slaw"))
sl.write(multi_select)

val = sl.slider("This is a slider", min_value=50,max_value=150)

num_val = sl.number_input("Timber sale value")
print(num_val)
text_val2 = sl.text_area("Tell me what most excites you about this timbersale.")
print(text_val2)
date_val = sl.date_input("Enter the date of the timber sale")
print(date_val)

def converter(timer):
    m,s,mm = timer.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s

timer = sl.time_input("Set Timer", value = time(0,0,0))
if str(timer) == "00:00:00":
    sl.write("Please set timer")
else:
    sec = converter(str(timer))
    bar = sl.progress(0)
    per=sec/100
    progress_status=sl.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + "%")
        ts.sleep(per)
