import streamlit as st
from PIL import Image

# TODO: Add in a 'why Python?' thing?

st.title("Getting data from FBref, and where to code")

st.write(
    """
    The tutorials on this site will usually start with taking a CSV of data from FBref, using the tools that 
    the FBref website provides itself. To save space and time in the tutorials (as people might go back and 
    reference these for the skills learned in the tutorial), this 'get the CSV' part of the process will live here.
    
    This page will also give some tips for what you can use to actually code in as well. 
    """
)

st.write("----------------------------------------------------------------")

st.subheader("Places to code (IDEs)")
st.write(
    """
    If you're googling for what to use as your coding software, 'IDE' ('integrated development environment') will be 
    the easily-googleable search term. IDEs are to coding as word processing software is to writing. They provide you 
    with a place to write code as well as run it, and usually have a range of useful things like syntax highlighting or
    easy formatting options. 
    
    There are plenty of online IDE options, which I think are useful for beginners because they mean you don't have to 
    worry about setting up and downloading various things, including the coding language itself! [JupyterLab](https://jupyter.org/try-jupyter/lab/) 
    and [Google Colab](https://colab.research.google.com/) are both free options.
    
    These two, and others, provide an option to code in a notebook format; unlike a blank file, this arranges code 
    into 'cells', and you can intersperse these with cells of regular text as well (e.g. for notes or explanation). 
    (Notebooks are popular particularly among people who share code, or the output of code, frequently, for example 
    people who produce reports featuring data). 
    
    If you prefer an offline option, [Pycharm](https://www.jetbrains.com/pycharm/) has a free 'Community Edition', 
    although other IDEs are available.
    """
)

st.write("----------------------------------------------------------------")

st.subheader("Getting CSVs from FBref")
st.write(
    """
    'CSV' stands for 'comma separated values' and is a form that data can come in - and, handily, is one which FBref 
    makes their data available in on the website. Here's an example of how to get data from the site into a CSV 
    which you can then use in your coding.
    
    For this example, we're heading for the player season stats for the Premier League 2022/23 season. Hover over 
    'Squad & Player Stats' for the player data and click 'Standard Stats'.
    """
)

st.image(Image.open("images/fbref/Find player standard stats.png"))

st.write(
    """
    At the top of the 'Standard Stats' page there'll be a table of team data, and once you scroll past that you'll 
    get to the player data. Hover over the 'Share & Export' option. 
    """
)

st.image(Image.open("images/fbref/save as csv.png"))

st.write(
    """
    Clicking the 'Get table as CSV' option will turn the table into something like this:
    """
)

st.image(Image.open("images/fbref/a wild comma separated values appeared.png"))

st.write(
    """
    The easiest way that I know to select all of this data is to start off by highlighting the first part of it, 
    then scroll all the way down the page to the end. Hold the shift key and click at the end of the data - if you 
    need to you can keeping holding shift and use the arrow keys to get the selection exactly right. It should look 
    like this:
    """
)

st.image(Image.open("images/fbref/highlight EVERYTHING.png"))

st.write(
    """
    Copy that selection and paste it in Microsoft Excel or other spreadsheet software. There should be an option 
    in the software to convert text to columns of data (in Excel it's under 'Text to Columns' in the 'Data' tab; 
    NUMBERS APPLE)
    """
)

st.image(Image.open("images/fbref/pasting into excel.png"))

st.write(
    """
    The process may differ between software, but you'll want to look out for any option that separates on certain 
    characters, and when you get the chance to choose which character to separate on you'll want to select commas.
    """
)

st.image(Image.open("images/fbref/text to columns.png"))

st.write(
    """
    When that's done, save the file as a CSV, and there you go! Ready to read into some Python code. Best to save it 
    in a file location which is easy to remember to save you going 'oh where did I put this?' when writing the file 
    import code. 
    
    This whole process might be a bit of a pain if you're new to working with things like CSV data, but it's 
    repeatable and lets you focus your energy on learning to code rather than learning to import data. 
    """
)
