import pandas as pd

def get_games():
    """Gets a gamerpower api which contains a lot free and legal games 
    for pc and converts the data into a .csv file so you can browse it 
    whenever you want. Check the end date of a title and get it before 
    it ends!"""
    
    data = pd.read_json("https://www.gamerpower.com/api/giveaways?platform=pc")
    games = data[["title", "description", "instructions", "open_giveaway", "worth", "end_date",]]
    games.to_csv("games.csv")
    
get_games()
