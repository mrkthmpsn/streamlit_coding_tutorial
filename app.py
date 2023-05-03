import pandas as pd
import streamlit as st

st.title("Intro to coding in Python, using FBref data")
st.subheader("est. time, 5-10 minutes")
st.write(
    """
    This is a short tutorial that'll introduce some foundational skills for coding in Python: loading in data; 
    cleaning data; adding, removing, and filtering data. 
    
    You can read through the tutorial as you'd read through an article (there are some interactive sections to keep 
    things from getting too boring) or you can skip to the end to get the code and the CSV that the tutorial is 
    based on. (All the code at the end will be shown throughout the tutorial as well).
    
    The data comes from FBref (https://fbref.com/en/), a really great site for football stats.
    """
)
with st.expander(
    "Where/what to use to code in Python & more on getting CSVs from FBref"
):
    # Explain what an IDE is
    st.subheader("IDEs (and what an IDE is)")
    st.write(
        """
        'IDE' stands for 'integrated development environment', and it's kind of to writing code what 
        Microsoft Word is to word processing: software to do a task, with some handy tools. Just like word processing,
        different IDEs have different features and vibes; and just like word processing, there are online versions 
        available.
        
        I quite like JupyterLab, which you can try for free here: https://jupyter.org/try-jupyter/lab/. The advantage of
         an online IDE is that you don't have to worry about downloading software and the coding language etc, things 
        which can be a pain if you're just starting out coding.
        
        Another popular online option is Google Colab, and a popular downloadable IDE is Pycharm (there's a free 
        Community Version as well as their paid version which has some specialist features) 
        """
    )

    st.subheader("Getting free FBref data")
    st.write(
        """
        Every table on FBref (https://fbref.com/en/) has an option to its top left, 'Share & Export'. Selecting 
        'Get table as CSV' changes the table into text data that you can copy and paste into Microsoft Excel or another 
        spreadsheet software. There should be an option in that software to turn text into data, and when you get to 
        'delimiter' options you'll want to split the rows on commas. Save that, load it to wherever you want to work, 
        and you're away.
        """
    )

dataframe = pd.read_csv("fbref_player_data.csv", header=[0, 1])

st.write("--------------------------------")

st.subheader("Importing & cleaning the data")
st.write(
    """
    The following couple of lines gets you started loading in the CSV (if you're coding along elsewhere you might 
    need to check that your file path is correct if the Python file and CSV are in different folders). 
    """
)
st.code(
    """
import pandas as pd
dataframe = pd.read_csv('fbref_player_data.csv', header=[0,1])
"""
)
st.markdown(
    """
    This imports a helpful coding package, `pandas`, and uses it to save the CSV data to a variable called 
    `dataframe`. It'd give you something that looks like this:
    """
)

st.write(dataframe.head(2))

dataframe.columns = [
    f"{colname_1} {colname_2}" if "Unnamed" not in colname_1 else colname_2
    for colname_1, colname_2 in dataframe.columns
]
dataframe = dataframe.drop(["Rk", "Matches", "#NAME? -9999"], axis=1)
st.write(
    """
    There are actually two column headers for each column here, which is a bit of a pain to deal with, so we can 
    write over them. There are also a few columns that we definitely won't care about, so we'll remove them too.
    """
)
st.code(
    """
dataframe.columns = [f"{colname_1} {colname_2}" if 'Unnamed' not in colname_1 else colname_2 for colname_1, colname_2 in dataframe.columns]
dataframe = dataframe.drop(['Rk', 'Matches', '#NAME? -9999'], axis=1)
    """
)

with st.expander("More detail on these lines of code"):
    st.markdown(
        """
        These lines are a bit advanced to throw at the start of a beginner tutorial so it's worth explaining them a 
        little more. They're not as self-explanatory as the rest of the code in the tutorial but they contain some 
        useful tricks.
        
        The table above actually has two rows of column headers. That comes from the FBref data, and is enforced in 
        our code with the `header=[0, 1]` part of `pd.read_csv`. The `dataframe.columns` line then overwrites the 
        column names of `dataframe` using a Python trick called 'list comprehension'. It does a bit of code `for` each item `in` the list - and in this case, because we have two 
        column headers, each item is split into two variables, `colname_1`, and `colname_2`.
        
        What we're _doing_ with those two temporary variables is really simple, we're just pasting them together. 
        The `f" TEXT "` part of the line is something called an 'f-string' or 'formatted string', and means we can 
        use code _within_ some text, with code occuring between sets of curly brackets. So we're putting `colname_1` 
        and `colname_2` inside an f-string, separated by a space.

        _But wait, there's more_. Only one thing more. 

        In the FBref table, some columns don't have anything in the first part of the column header. `pd.read_csv` 
        fills this in with some text of its own which includes the word `Unnamed`. We obviously don't want that, so 
        'Unnamed' being *in* the `colname_1` text is an indication that the `colname_1` value is basically junk and 
        we don't need it. 

        If you put that all together the logic of this line of code is something like: "for every value in the 
        dataframe.columns list, combine the names of colname_1 and colname_2 unless colname_1 is junk, else just use 
        the name of colname_2".   
        """
    )

st.write("--------------------------------")

st.subheader("Filtering data")
st.write(
    """
    Cleaning data, like we've just done, is often a step in the process of data analysis. 
    
    But now we get to actually do something with it.
    """
)

new_df = dataframe.copy()
rearranged_df = new_df[
    ["Player", "Squad", "Age", "Born", "Playing Time Min", "Performance G+A"]
].sort_values("Performance G+A", ascending=False)

st.write(
    """
    This tutorial is using data for basic stats from the Premier League 2022/23 season, taken midway through April 
    of that campaign. We'll create a new variable with a copy of our cleaned-up `dataframe` and a subset of the 
    columns in it.
    """
)
st.code(
    """
new_df = dataframe.copy()
rearranged_df = new_df[['Player', 'Squad', 'Age', 'Born', 'Playing Time Min', 'Performance G+A']].sort_values('Performance G+A', ascending=False)
    """
)
st.write(
    """
    Now for you to get involved. 
    
    You can use the input below to choose a number to filter the data on. This number will filter the data to 
    only include players who have scored and assisted equal to or more than the number. You'll see the line of code 
    change, as well as the number of rows and the table itself.
    """
)
number_filter = st.number_input("Input a number: ", value=10)
st.write("Code:")
st.code(
    f"""
    temp_filtered_df = rearranged_df[rearranged_df['Performance G+A'] >= {number_filter}]
    """
)
temp_filtered_df = rearranged_df[rearranged_df["Performance G+A"] >= number_filter]
st.write(f"Number of rows in the filtered dataframe: {len(temp_filtered_df)}")
st.write(temp_filtered_df)

st.write("--------------------------------")

st.subheader("Creating new data & multi-filtering")

young_ballers_df = new_df[
    ["Player", "Squad", "Age", "Born", "Playing Time Min", "Performance G+A"]
].sort_values("Performance G+A", ascending=False)
young_ballers_df["nineties_played"] = young_ballers_df["Playing Time Min"] / 90
young_ballers_df["goal_cont_90"] = (
    young_ballers_df["Performance G+A"] / young_ballers_df["nineties_played"]
)
st.write(
    """
    We're going to create a new dataframe and do something different with it. Players all play different amounts 
    of time, particularly young players with promising futures. We're going to take the goals and assists figures 
    and calculate the values 'per 90 minutes'.  
    
    The original CSV has this data in one of its columns but let's create it ourselves.
    """
)
st.code(
    """
young_ballers_df = new_df[['Player', 'Squad', 'Age', 'Born', 'Playing Time Min', 'Performance G+A']].sort_values('Performance G+A', ascending=False)
young_ballers_df['nineties_played'] = young_ballers_df['Playing Time Min'] / 90
young_ballers_df['goal_cont_90'] = young_ballers_df['Performance G+A'] / young_ballers_df['nineties_played']
    """
)
st.write(
    """
    We're also going to filter on the players' ages. The data that we have has an 'Age' column, but that columns 
    isn't in an immediately helpful format to work with, so let's use the 'Born' column instead. Choose the year 
    that you want your new dataframe to start with, and players born in that year or after will be the ones left in 
    the data.
    """
)

dob_filter = st.number_input("Year of birth filter...", value=2000)

st.write("Code:")
st.code(
    f"""
    young_ballers_df[young_ballers_df['Born'] >= {dob_filter}].sort_values('goal_cont_90', ascending=False)
    """
)
st.write(
    young_ballers_df[young_ballers_df["Born"] >= dob_filter].sort_values(
        "goal_cont_90", ascending=False
    )
)

st.write(
    """
    You'll notice that we've got some players towards the top of the list who haven't even played a full
    match. We didn't save the filtering in the last bit of code, so now we'll filter on both the year of birth
    and the amount of time that they played _at the same time_. 
    """
)

new_dob_filter = st.number_input("Year of birth filter (again)...", value=2000)
nineties_filter = st.number_input(
    "90s filter (1.0 90 = 1 full match)", value=5.0, step=0.01
)

young_ballers_df = young_ballers_df[
    (young_ballers_df["Born"] >= new_dob_filter)
    & (young_ballers_df["nineties_played"] >= nineties_filter)
].sort_values("goal_cont_90", ascending=False)

st.write("Code:")
st.code(
    f"""
    young_ballers_df = young_ballers_df[(young_ballers_df['Born'] >= {new_dob_filter}) & (young_ballers_df['nineties_played'] >= {nineties_filter})].sort_values('goal_cont_90', ascending=False)
    """
)
st.write("The data table itself:")
st.write(young_ballers_df)

st.write(
    """
    There we go! The table that you've ended up with will hopefully be pretty interesting (partly because you've 
    chosen some of the filters of course). The code itself might not have seemed super flashy, but by getting to the 
    end of the tutorial you've seen:
    - How to import a package
    - How to load in a CSV file of data
    - Some ways to clean up data
    - How to add, remove, and filter data to help with data exploration
    
    These are all really fundamental skills for working with data.
    """
)

st.write("----------------------------------------------------------------")

with st.expander("CSV and full code"):
    st.write("Download the CSV used in the tutorial")
    with open("fbref_player_data.csv", "rb") as file:
        st.download_button(
            "CSV file",
            data=file,
            file_name="fbref_player_data.csv",
            mime="text/csv",
        )

    st.write(
        """
        All of the code below was written in the tutorial, but having it all together makes it easier to copy and 
        paste for your own convenience and benefit. 
        
        For parts of the code where you could choose the input in the tutorial, the code below has default values 
        (rather what you might have changed things to in the tutorial).
        """
    )
    st.code(
        """
        import pandas as pd
dataframe = pd.read_csv('fbref_player_data.csv', header=[0,1])
dataframe.columns = [f"{colname_1} {colname_2}" if 'Unnamed' not in colname_1 else colname_2 for colname_1, colname_2 in dataframe.columns]
dataframe = dataframe.drop(['Rk', 'Matches', '#NAME? -9999'], axis=1)

new_df = dataframe.copy()
rearranged_df = new_df[['Player', 'Squad', 'Age', 'Born', 'Playing Time Min', 'Performance G+A']].sort_values('Performance G+A', ascending=False)

temp_filtered_df = rearranged_df[rearranged_df['Performance G+A'] >= 10]

young_ballers_df = new_df[['Player', 'Squad', 'Age', 'Born', 'Playing Time Min', 'Performance G+A']].sort_values('Performance G+A', ascending=False)
young_ballers_df['nineties_played'] = young_ballers_df['Playing Time Min'] / 90
young_ballers_df['goal_cont_90'] = young_ballers_df['Performance G+A'] / young_ballers_df['nineties_played']

young_ballers_df[young_ballers_df['Born'] >= 2000].sort_values('goal_cont_90', ascending=False)

young_ballers_df = young_ballers_df[(young_ballers_df['Born'] >= 2000) & (young_ballers_df['nineties_played'] >= 5.0)].sort_values('goal_cont_90', ascending=False)
        """
    )
