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
sl.header("Streamlit header")
sl.subheader("Streamlit Web App sub-header")
sl.text("This is the text function for writing paragraphs of text.")

# Let's play around with some markdown syntax
sl.markdown("# Markdown formatting") # for header (H1)
sl.markdown("## H2 type header")
sl.markdown("### H3 type header")
sl.markdown("**Hello** *World* it's me") #Hellow is bold, world is italic
sl.markdown("> this is a block quote.")
sl.markdown("For more information, visit the [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet)")
sl.caption("This is what a caption looks like")
sl.markdown("---")

#Latex stuff
sl.text("We can also do mathematical symbols")
sl.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
sl.markdown("For more information, visit the [latex cheat sheet](https://katex.org/docs/supported.html)")

#Now let's put some media on this website!
sl.markdown("## Media!")
sl.image("DSC_0560.jpg","ACPC 2019 at Purchase Knob")
sl.audio("1-12 Baby Beats.mp3")
sl.video("South Florida Bike Tour.mp4")
