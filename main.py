"""
Bodged together code to process Inkstorm 8 Signups for production data

By Vincent Lee @vlee888 / Discord: vlee489#5801
"""

import csv
from design import Team, Player
from typing import Optional

inputFile = "attendeeList_inkstorm-8.csv"
output = "outputV2.csv"

teamObjects = []

# Remember computers start from 0
team_name_column = 26  # column that contains the team name
player_name_column = 5  # column that contains player name
player_county_column = 13  # column with the player's country info


def find_team(teamList, teamName) -> Optional[Team]:
    """
    Used to find if a team object with a certain name exists in the provided list
    :param teamList: list
        list of Team objects
    :param teamName: str
        team name to look for
    :return: Team
        The Team Object if found, if not fround, returns None
    """
    for teamItem in teamList:
        if teamItem.teamName == teamName:
            return teamItem
    return None


# Opens the input file
with open(inputFile, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file)
    # For each row in the CSV file
    for row in reader:
        if row[team_name_column]:  # if the team name isn't blank (Hence not pending team)
            team = find_team(teamObjects, row[team_name_column])  # Find Team Object
            if team:
                # Add Player to team
                team.add_member(Player(row[player_name_column], row[player_county_column]))
            else:
                # Create new team, add player, add to list of teams
                team_create = Team(row[team_name_column])
                team_create.add_member(Player(row[player_name_column], row[player_county_column]))
                teamObjects.append(team_create)


# Create an output csv file with the utf-8 encoding
with open(output, "w", encoding='utf-8', newline='', ) as csv_out_file:
    writer = csv.writer(csv_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Write initial row
    writer.writerow(["ID", "teamName", "seed", "playerCount", "teamPrefix", "player1name", "player1flag", "player2name",
                     "player2flag", "player3name", "player3flag", "player4name", "player4flag", "player5name",
                     "player5flag", "player6name", "player6flag", "player7name", "player7flag"])
    for teams in teamObjects:
        # get list to add to file for each time
        teamRow = [teams.ID, teams.teamName, "", teams.play_count(), ""]
        for players in teams.players:
            teamRow.append(players.name)
            teamRow.append(players.country)

        writer.writerow(teamRow)  # write row to file
