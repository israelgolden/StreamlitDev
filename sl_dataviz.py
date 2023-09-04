import streamlit as sl
import pandas as pd
import numpy as np
import altair as alt

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

sl.title("Streamlit Web App Playground")
sl.header("Streamlit Data Viz")
#Displaying JSON and code
json = {"a":"1,2,3", "b":"4,5,6"}
sl.json(json)
code="""
print("hello world")
def funct():
    return 0;"""
sl.code(code, language = "python")

# Write and Tables
# Write can take lots of different arguments - the swiss army knife
sl.write('Hello, *World!* :sunglasses:')
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
sl.write(c)
#metric function
sl.metric(label="Wind Speed", value = "120ms⁻¹", delta="-1.4ms⁻¹")
#let's make a table
sl.text("First let's create a static table")
table = pd.DataFrame({"Column 1": [1,2,3,4,5], "Column 2": [11,12,13,14,15]})
sl.table(table)
# now let's make a dataframe...
sl.text("Next let's create a sortable dataframe")
sl.dataframe(table)