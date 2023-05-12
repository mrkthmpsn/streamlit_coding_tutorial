import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.title("Coding with FBref match results data")
st.subheader("est. time, WHO KNOWS MATEY")

st.write(
    """
    This is an early-stage Python tutorial where we'll use [FBref](https://fbref.com/en/) competition results data 
    to learn some coding skills. We're going to rearrange and summarise some data and write code in a way that groups
    work together to re-run BLAH BLAH BLAH 
    
    You can read through the tutorial as you'd read through an article (there are some interactive sections to keep 
    things from getting too boring) or you can skip to the end to get the code and the CSV that the tutorial is 
    based on. (All the code at the end will be shown throughout the tutorial as well).
    
    This tutorial will use data from FBref's league fixtures/results pages, taken partway through April of the 2022/23
    Premier League season (FBref's pages follow the same structure so you'll be able to re-use this code for other 
    competitions or seasons).
    """
)

st.write("--------------------------------")

st.subheader("Cleaning the data")
st.write(
    """
    Like always (or at least, like often) there's a bit of cleaning to the data we need to do.
    
    Fortunately, unlike the first tutorial [link], the table only has one header for each column. However, it has 
    two columns named the same thing, so we'll want to rename them. Then, to match Python naming conventions (using
    'snake case' - `just_like_this` - we'll run through the column names and set them to lower case, replacing 
    spaces with underscores. 
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
    column is actually text rather than date, which is its own specific datatype. We'll adjust that too.
    
    More details on these lines of code in the expandable section, because you're probably bored of reading about data 
    cleaning and adjusting techniques by now. 
    """
)

df["home_score"] = df["score"].apply(lambda x: int(x[0]))
df["away_score"] = df["score"].apply(lambda x: int(x[-1]))
df = df.drop(columns=["score"])

df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.date

st.code(
    """
    df["home_score"] = df["score"].apply(lambda x: int(x[0]))
df["away_score"] = df["score"].apply(lambda x: int(x[-1]))
df = df.drop(columns=["score"])

df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.date
    """
)
with st.expander("More on apply and lambda"):
    st.write(
        """
        Write about the use of `apply` and `lambda` here (maybe use assign instead of apply lambda?)
        
        Write a bit about date formats and what those %s are called because i can never find what they
        are when I try and google for them
        """
    )

st.write(df.head(2))

st.write("bit of text here")

date_choice = st.date_input(
    "Choose a date",
    value=datetime.date(2023, 1, 1),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)

st.write(df[df["date"] > date_choice].head(2))

st.write("--------------------------------")

st.subheader("Rearranging the data")
st.write("bit of text here")
new_df = df.copy()

st.write("bit of text here")
home_df = new_df.copy().rename(
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
away_df = new_df.copy().rename(
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

st.write(combined_df.head())

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
st.write("bit of text here")

start_date_choice = st.date_input(
    "Start date:",
    value=datetime.date(2022, 12, 25),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)
end_date_choice = st.date_input(
    "End date:",
    value=datetime.date(2023, 4, 11),
    min_value=datetime.date(2022, 8, 5),
    max_value=datetime.date(2023, 4, 21),
)
st.write("will show the code here")

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

st.write(summarised_df.sort_values("xg_difference", ascending=False))
