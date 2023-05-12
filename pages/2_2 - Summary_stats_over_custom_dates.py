import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.title("Summary stats over custom dates")
st.subheader("Coding with FBref match results data")
st.write("**est. time, around 10 minutes**")

st.write(
    """
    This is an early-stage Python tutorial where we'll use [FBref](https://fbref.com/en/) competition results data 
    to learn some coding skills. We're going to rearrange and summarise some data and write code in a way that groups
    work together to re-run BLAH BLAH BLAH 
    
    There are a few different ways you could read this tutorial:
    - Read it like you would an article, from start to finish
    - Read it alongside coding, copying and pasting each line as it comes
    - Skip to the end and get the code as an uninterrupted block
    
    Each option is valid. This tutorial will use data from FBref's league fixtures/results pages, taken partway through 
    April of the 2022/23 Premier League season (FBref's pages follow the same structure so you'll be able to re-use 
    this code for other competitions or seasons).
    
    You can download the CSV used in the tutorial here:
    """
)

with open("fbref_fixtures_data.csv", "rb") as file:
    st.download_button(
        "CSV file",
        data=file,
        file_name="fbref_fixtures_data.csv",
        mime="text/csv",
    )

st.write("--------------------------------")

st.subheader("Cleaning the data")
st.write(
    """
    As often happens, there's a bit of cleaning to the data we need to do.
    
    It's a little different to the first tutorial - each column has one header, but two have the same name. Also, to 
    match Python naming conventions (using 'snake case' - `just_like_this` - we'll run through the column names and 
    set them to lower case, replacing spaces with underscores. 
    """
)

df = pd.read_csv("fbref_fixtures_data.csv")
df = df.rename(columns={"xG": "home_xg", "xG.1": "away_xg"})
df.columns = [colname.lower().replace(" ", "_") for colname in df.columns]

st.code(
    """
    df = pd.read_csv("fbref_fixtures_data.csv")
df = df.rename(columns={"xG": "home_xg", "xG.1": "away_xg"})
df.columns = [colname.lower().replace(" ", "_") for colname in df.columns]
    """
)

st.write(
    """
    Because this data was taken partway through the season, there are matches in the CSV that haven't been played yet.
    We can see this by checking out the bottom of the dataframe that we've created, using `df.tail()`. Specifying
    `df.tail(2)` gives us the last two rows of the dataframe.
    """
)
st.code("df.tail(2)")
st.write(df.tail(2))
st.write(
    """
    We can get rid of these rows by using `.dropna()`, specifying that we want to drop rows where the 'score' column 
    is empty. While we're at it, we'll get rid of two junk columns, chaining the two methods together [LINK]. 
    """
)

df = df.drop(columns=["match_report", "notes"]).dropna(subset="score")
st.code(
    """
    df = df.drop(columns=["match_report", "notes"]).dropna(subset="score")
    """
)

st.write(
    """
    Now running `df.tail(2)` gives us something different:
    """
)
st.write(df.tail(2))

st.write(
    """
    Our final bit of data cleaning now. 
    
    The 'score' column isn't too easy to work with, so we're going to split that up. Finally, the format of the 'date' 
    column is actually text rather than a date, which is its own specific datatype. We'll adjust that too.
    
    More details on these lines of code, as well as the cleaning code in full, in the expandable section, because 
    you're probably bored of reading about data cleaning and adjusting techniques by now. 
    """
)

df = df.assign(
    home_score=df["score"].apply(lambda x: int(x[0])),
    away_score=df["score"].apply(lambda x: int(x[-1])),
).drop(columns=["score"])
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.date

st.code(
    """
    df = df.assign(
    home_score=df['score'].apply(lambda x: int(x[0])),
    away_score=df["score"].apply(lambda x: int(x[-1]))
).drop(columns=["score"])
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.date
    """
)
with st.expander("More on these lines, and the cleaning code in full"):
    st.write(
        """
        There are a few more useful tricks here. 
        
        `.assign()` lets you create new columns for your dataframe without having to define them one line at a time.
        `.apply()` runs code over each row in a dataframe, and `lambda` is like a mini-function. There's a [good 
        explanation of Python lambdas here](https://www.w3schools.com/python/python_lambda.asp). 
        
        The things with the `%`s are date and time specifiers; as you might've guessed they tell the function what
        format the current date string is in so that it can rearrange it. I find [this page useful on remembering what
        specifiers are what](https://www.ibm.com/docs/en/cmofm/9.0.0?topic=SSEPCD_9.0.0/com.ibm.ondemand.mp.doc/arsa0257.html)  
        
        Here's the cleaning code in full. It'll be uninterrupted at the bottom of the page as well, but
        just in case you wanted to see it in one piece ahead of then.
        """
    )
    st.code(
        """
        df = pd.read_csv("fbref_fixtures_data.csv")
df = df.rename(columns={"xG": "home_xg", "xG.1": "away_xg"})
df.columns = [colname.lower().replace(" ", "_") for colname in df.columns]

df = df.drop(columns=["match_report", "notes"]).dropna(subset="score")

df = df.assign(
    home_score=df['score'].apply(lambda x: int(x[0])),
    away_score=df["score"].apply(lambda x: int(x[-1]))
).drop(columns=["score"])
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.date
        """
    )

st.write(
    """
    Now that we've adjusted the date format, we can filter properly on that column. You can choose a date below
    and you'll see that the dataframe gets filtered to only show games played after that date.
    """
)

date_choice = st.date_input(
    "Choose a date",
    value=datetime.date(2023, 1, 1),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)

st.code(
    f"""
    df[df["date"] > {date_choice}].head(2)
    """
)
st.write(df[df["date"] > date_choice].head(2))

st.write("--------------------------------")

st.subheader("Rearranging the data")
st.write(
    """
    Sometimes the data you have is useful, but not in the best format for using it. The data we have here has one row
    per match, but it'll probably be easier if we have one row per _team_. That way you can just group on a 
    column for the team, rather than having to combine home and away columns. 
    
    There are different ways you could do this, but for this tutorial we'll split our original data up into 'home' 
    and 'away' dataframes, rename some columns, and then combine them back together. This'll be a big chunk of code,
    so I've put code comments inside it.
    """
)
new_df = df.copy()

home_df = new_df.rename(
    columns={
        "home": "team_name",
        "home_xg": "xg",
        "away": "opponent_name",
        "away_xg": "opponent_xg",
        "home_score": "score",
        "away_score": "opponent_score",
    }
)
home_df["home_away"] = "home"
away_df = new_df.rename(
    columns={
        "away": "team_name",
        "away_xg": "xg",
        "home": "opponent_name",
        "home_xg": "opponent_xg",
        "away_score": "score",
        "home_score": "opponent_score",
    }
)
away_df["home_away"] = "away"

combined_df = pd.concat([home_df, away_df])
combined_df["points"] = np.where(
    combined_df["score"] > combined_df["opponent_score"],
    3,
    np.where(combined_df["score"] == combined_df["opponent_score"], 1, 0),
)

st.code(
    """
    # Using `.copy()` can help avoid accidentally altering old data when defining new variables
new_df = df.copy()

# Define two new copies, and rename columns accordingly
home_df = new_df.rename(
    columns={
        "home": "team_name",
        "home_xg": "xg",
        "away": "opponent_name",
        "away_xg": "opponent_xg",
        "home_score": "score",
        "away_score": "opponent_score",
    }
)
home_df["home_away"] = "home"
away_df = new_df.rename(
    columns={
        "away": "team_name",
        "away_xg": "xg",
        "home": "opponent_name",
        "home_xg": "opponent_xg",
        "away_score": "score",
        "home_score": "opponent_score",
    }
)
away_df["home_away"] = "away"

# Combine the home and away dataframes and create a points column
combined_df = pd.concat([home_df, away_df])
combined_df["points"] = np.where(
    combined_df["score"] > combined_df["opponent_score"],
    3,
    np.where(combined_df["score"] == combined_df["opponent_score"], 1, 0),
)
    """
)

st.write(
    """
    A simple way to check that this has worked is to look for specific matches and check whether it has two rows - no 
    more and no fewer. Choose a date and a venue from the dropdown (it'll update depending on the date chosen and 
    tell you if there were no matches played that day).
    """
)
new_date_choice = st.date_input(
    "Choose a date",
    value=datetime.date(2022, 8, 5),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)
venue_choices = combined_df[combined_df["date"] == new_date_choice]["venue"].unique()

venue_choice = st.selectbox("Choose a stadium", options=venue_choices)
if venue_choice:
    st.write(
        combined_df[
            (combined_df["date"] == new_date_choice)
            & (combined_df["venue"] == venue_choice)
        ]
    )
else:
    st.write("No matches played that day")

st.write("--------------------------------")

st.subheader("Summarising data for a time period")
st.write(
    """
    Cool. Now we have data in a nice format to work with, we can summarise it. There are some date selectors
    below - you can choose custom dates or leave them as they are for the full date range in the data. We'll
    be filtering on these dates as we summarise.
    """
)

start_date_choice = st.date_input(
    "Start date:",
    value=datetime.date(2022, 8, 5),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)
end_date_choice = st.date_input(
    "End date:",
    value=datetime.date(2023, 4, 21),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)

st.write(
    """
    The bit of code below involves a bunch of the things you'll have seen so far in this tutorial. There's
    some filtering of a dataframe, there's some method chaining, and at the end we create a new column like 
    we've seen before. Click [here for more on the `.agg` function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html) 
    and click [here for more on the `pd.NamedAgg` function](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.NamedAgg.html).
    """
)

summarised_df = (
    combined_df[
        (combined_df["date"] >= start_date_choice)
        & (combined_df["date"] <= end_date_choice)
    ]
    .groupby("team_name")
    .agg(
        games_played=pd.NamedAgg(column="wk", aggfunc="count"),
        xg_for=pd.NamedAgg(column="xg", aggfunc="mean"),
        xg_against=pd.NamedAgg(column="opponent_xg", aggfunc="mean"),
        goals_for=pd.NamedAgg(column="score", aggfunc="mean"),
        goals_against=pd.NamedAgg(column="opponent_score", aggfunc="mean"),
        points_per_game=pd.NamedAgg(column="points", aggfunc="mean"),
    )
)
summarised_df["xg_difference"] = summarised_df["xg_for"] - summarised_df["xg_against"]

st.code(
    f"""
    summarised_df = (
    combined_df[
        (combined_df["date"] >= {start_date_choice})
        & (combined_df["date"] <= {end_date_choice})
    ]
    .groupby("team_name")
    .agg(
        games_played=pd.NamedAgg(column="wk", aggfunc="count"),
        xg_for=pd.NamedAgg(column="xg", aggfunc="mean"),
        xg_against=pd.NamedAgg(column="opponent_xg", aggfunc="mean"),
        goals_for=pd.NamedAgg(column="score", aggfunc="mean"),
        goals_against=pd.NamedAgg(column="opponent_score", aggfunc="mean"),
        points_per_game=pd.NamedAgg(column="points", aggfunc="mean"),
    )
)
summarised_df["xg_difference"] = summarised_df["xg_for"] - summarised_df["xg_against"]

summarised_df.sort_values("xg_difference", ascending=False)
    """
)
st.write(summarised_df.sort_values("xg_difference", ascending=False))

st.write(
    """
    Summarising by whatever dates you want is interesting enough, and you've got plenty other bits of data
    you could summarise as well. Home and away is an obvious one, or if you filtered to certain teams in the
    opponent column you could see how they did against the Big Six or in London derbies. This code will also 
    work for other similar pages on FBref, which look at other stats over time.
    
    With this tutorial, you've learnt about cleaning and reformatting data, about datatypes, and about summarising
    data in a dataframe. And you've ended up with code that can summarise stats over any timeframe. 
    """
)

with st.expander("CSV and full code here:"):
    st.write("Download the CSV used in the tutorial")
    with open("fbref_fixtures_data.csv", "rb") as file:
        st.download_button(
            "CSV file",
            data=file,
            file_name="fbref_fixtures_data.csv",
            mime="text/csv",
        )

    st.write("And here's the full uninterrupted code")

    st.code(
        """
        df = pd.read_csv("fbref_fixtures_data.csv")
df = df.rename(columns={"xG": "home_xg", "xG.1": "away_xg"})
df.columns = [colname.lower().replace(" ", "_") for colname in df.columns]

df = df.drop(columns=["match_report", "notes"]).dropna(subset="score")

df = df.assign(
    home_score=df['score'].apply(lambda x: int(x[0])),
    away_score=df["score"].apply(lambda x: int(x[-1]))
).drop(columns=["score"])
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.date

# Using `.copy()` can help avoid accidentally altering old data when defining new variables
new_df = df.copy()

# Define two new copies, and rename columns accordingly
home_df = new_df.rename(
    columns={
        "home": "team_name",
        "home_xg": "xg",
        "away": "opponent_name",
        "away_xg": "opponent_xg",
        "home_score": "score",
        "away_score": "opponent_score",
    }
)
home_df["home_away"] = "home"
away_df = new_df.rename(
    columns={
        "away": "team_name",
        "away_xg": "xg",
        "home": "opponent_name",
        "home_xg": "opponent_xg",
        "away_score": "score",
        "home_score": "opponent_score",
    }
)
away_df["home_away"] = "away"

# Combine the home and away dataframes and create a points column
combined_df = pd.concat([home_df, away_df])
combined_df["points"] = np.where(
    combined_df["score"] > combined_df["opponent_score"],
    3,
    np.where(combined_df["score"] == combined_df["opponent_score"], 1, 0),
)

summarised_df = (
    combined_df[
        (combined_df["date"] >= {start_date_choice})
        & (combined_df["date"] <= {end_date_choice})
    ]
    .groupby("team_name")
    .agg(
        games_played=pd.NamedAgg(column="wk", aggfunc="count"),
        xg_for=pd.NamedAgg(column="xg", aggfunc="mean"),
        xg_against=pd.NamedAgg(column="opponent_xg", aggfunc="mean"),
        goals_for=pd.NamedAgg(column="score", aggfunc="mean"),
        goals_against=pd.NamedAgg(column="opponent_score", aggfunc="mean"),
        points_per_game=pd.NamedAgg(column="points", aggfunc="mean"),
    )
)
summarised_df["xg_difference"] = summarised_df["xg_for"] - summarised_df["xg_against"]

summarised_df.sort_values("xg_difference", ascending=False)
        """
    )
