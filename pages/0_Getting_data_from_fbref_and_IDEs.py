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
    An 'IDE' is basically to coding what Microsoft Word is to writing text. It stands for 'integrated development 
    environment', and the only reason you need to know that at all is to help you google for options if you want to.
    
    They provide you with a place to write code as well as run it, and often have a range of useful things like 
    suggested autocomplete for code functions, easy formatting, syntax highlighting, etc.
    
    There are plenty of online IDE options, which I think are useful for beginners because they mean you don't have to 
    worry about setting up and downloading various things, including the coding language itself! There are two ways to 
    code that you might come across, but feel free to skip through to the suggested IDE options.
    """
)

with st.expander("Coding in files and coding in notebooks"):
    st.write(
        """
        The most common way of coding is to write in a file, like you'd do 'normal' writing in a form of text file. To 
        run the code from a file you then either run the whole file or can run parts of it in a 'console' or 'terminal'.
        Here's what that looks like, the top half being the file and the bottom half the console:
        """
    )
    st.image(Image.open("images/ide_screenshots/file_console_example.png"))
    st.write(
        """
        Another way, and the way that most online IDEs are set up, are notebooks (sometimes called 'Jupyter notebooks', 
        after the company which pioneered the format). Notebooks work as a series of 'blocks', and you can have text 
        blocks as well as code blocks. This can be useful for separating parts of your code or for sprinkling in bits of
        explanatory or thinking-space text. 
        
        Notebooks will also often have added features. Some will offer ways to create charts for you based on a table of
        data, without you having to write the code for the chart itself. This is how they can look:
        """
    )
    st.image(Image.open("images/ide_screenshots/notebook_example.png"))

st.write(
    """
    There are two examples of online IDEs below with short guides on how to get started with them. Others are available,
    but these should (hopefully) be fairly beginner-friendly (which not all software is, unfortunately).
    
    Generally, online IDEs will ask you to create an account, and offer an amount of storage for files. The amount of 
    storage is often something they'll offer as an upsell opportunity, but the amount you get for free is more than 
    enough for your use if you're getting started with coding.   
    """
)
with st.expander("JupyterLab"):
    st.write(
        """
        Link: https://jupyter.org/try-jupyter/lab/
        
        JupyterLab is pretty simple but that can be useful when you're starting out (a number of online IDEs _haven't_ 
        been included on this page because they're just a bit confusing for new users).
        
        The landing page looks like this: 
        """
    )
    st.image(Image.open("images/ide_screenshots/jupyter_lab.png"))
    st.write(
        """
        There's a brief welcome tour that it takes you on, but for these tutorials you can focus on the 'Notebook - 
        Python' option at the top of the 'Launcher' and the file directory on the left-hand side. 
        
        If you load a file into the main part of this file directory (i.e. not one of the folders) and you have a 
        Notebook file in the same area, you can reference the CSV file directly, like this (this is also covered in the 
        tutorials):
        """
    )
    st.code(
        """
        import pandas as pd
pd.read_csv('your_csv_file.csv')
        """
    )
    st.write(
        """
        If the CSV was in a folder, the `pd.read_csv` line would be something like 
        """
    )
    st.code(
        """
        pd.read_csv('folder/your_csv_file.csv')
        """
    )
    st.write(
        """
        The guide to notebooks that it offers you when you first create one is genuinely good (which can't be said for 
        all software guides). One further tip are some useful keyboard shortcuts: run a cellblock is 
        CTRL+ENTER(Windows)/CMD+ENTER(Mac); to run a cellblock and put your cursor in the following one (which also 
        creates a new cell if you're in the last one of the notebook) is SHIFT+ENTER.
        """
    )

with st.expander("Noteable"):
    st.write(
        """
        Link: https://app.noteable.io
        
        Noteable is the bells and whistles alternative to Jupyter Lab that I'm going to put forward. It gets the nod due
        to being fairly straightforward and [being a plugin for GPTPlus](https://docs.noteable.io/product-docs/chatgpt-plugin/get-started-with-the-plugin)
        (the paid version of Microsoft's GPT models). Disclaimer: I haven't tried this. However, it seems like an avenue
        that might make a more fancy online IDE worthwhile to try out.
        
        When you get through the sign-up process you'll have a screen like the screenshot below. Noteable's 
        organisational system gives you a 'Space' in which you can make 'Projects'. In these projects you can create 
        and upload files. 
        """
    )
    st.image(Image.open("images/ide_screenshots/noteable_home.png"))
    st.write(
        """
        Inside a Project will look like this
        """
    )
    st.image(Image.open("images/ide_screenshots/noteable_project_page.png"))
    st.write(
        """
        If you load a file into the main part of this file directory and you have a notebook file in the same area, you 
        can reference the CSV file directly, like this (this is also covered in the tutorials):
        """
    )
    st.code(
        """
        import pandas as pd
pd.read_csv('your_csv_file.csv')
        """
    )
    st.write("A notebook itself looks like this")
    st.image(Image.open("images/ide_screenshots/notebook_example.png"))
    st.write(
        """
        One further tip are some useful keyboard shortcuts: run a cellblock is CTRL+ENTER(Windows)/CMD+ENTER(Mac); to
        run a cellblock and put your cursor in the following one (which also creates a new cell if you're in the last 
        one of the notebook) is SHIFT+ENTER.
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
