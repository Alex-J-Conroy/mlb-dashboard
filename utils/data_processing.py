## Roster Data Import
roster_file = open('2019combinedroster.txt', 'r')
roster_string = roster_file.read()
roster_df = pd.DataFrame([x.split(',') for x in roster_string.split('\n')])
roster_df['firstinitial'] = roster_df[2].astype(str).str[0]
roster_df["Player"] = roster_df[1] +" "+ roster_df["firstinitial"]
del roster_df[0]
del roster_df[1]
del roster_df[2]
del roster_df[3]
del roster_df[4]
del roster_df[6]
del roster_df['firstinitial']
roster_df = roster_df[["Player",5]]
roster_df.columns = ['Player', 'Team']
roster_df.head()


team_name_file = open('TEAM2019.txt', 'r')
team_name_string = team_name_file.read()
team_name_df = pd.DataFrame([x.split(',') for x in team_name_string.split('\n')])
del team_name_df[1]
team_name_df["teamName"] = team_name_df[2] +" "+ team_name_df[3]
del team_name_df[2]
del team_name_df[3]
team_name_df.columns = ['Team', 'teamName']
team_name_df.head()

#merging datasets
playerTeam = pd.merge(roster_df,  team_name_df,  on ='Team',  how ='left')
dataset = pd.merge(dataset,  playerTeam,  on ='Player',  how ='left')
del dataset["Team"]
dataset['teamName'].astype(str)
dataset

#metric calcs
dataset["AVG"] = dataset["H"]/dataset["AB"]
dataset