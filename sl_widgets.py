import streamlit as sl

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