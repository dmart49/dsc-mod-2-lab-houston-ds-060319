import sqlite3
import pandas as pd
import numpy as np

#function to make dataframes from sql database

def make_sql_frame(sql):
    """
    Recieves an SQL command to retrieve
    information from our database
    and places the information in
    a pandas dataFrame
    """
    conn = sqlite3.connect("./database.sqlite")
    c = conn.cursor()
    c.execute(sql)
    df = pd.DataFrame(c.fetchall())
    df.columns = [x[0] for x in c.description]
    return df

#function to add wins, losses, draws to team objects

def get_results(teamDict, dataFrame, result):
    """
    Checks a dataFrame for the desired result
    Iterates through the dataFrame and populates
    the dictionary of Team objects with the
    information in the dataFrame
    """
    
    df_adjusted = dataFrame.loc[dataFrame['Match_Result'] == result]
    for index, row in df_adjusted.iterrows():
        away_name = row['AwayTeam']
        home_name = row['HomeTeam']
        away_goals = row['Away_Goals']
        home_goals = row['Home_Goals']
        for team in teamDict:
            if team == away_name:
                teamDict[team].add_goals(away_goals)
                if(result == 'A'):
                    teamDict[team].add_win()
                elif(result == 'H'):
                    teamDict[team].add_loss()
                else:
                    teamDict[team].add_draw()
            elif team == home_name:
                teamDict[team].add_goals(home_goals)
                if(result == 'A'):
                    teamDict[team].add_loss()
                elif(result == 'H'):
                    teamDict[team].add_win()
                else:
                    teamDict[team].add_draw()