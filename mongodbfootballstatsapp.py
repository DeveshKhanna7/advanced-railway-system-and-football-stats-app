import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:23217/")
db = client["football_stats"]
players_collection = db["players"]
teams_collection = db["teams"]
matches_collection = db["matches"]
users_collection = db["users"]

def add_player(name, team_id, goals, assists):
    player_data = {
        "name": name,
        "team_id": team_id,
        "goals": goals,
        "assists": assists,
        "created_at": datetime.utcnow()
    }
    players_collection.insert_one(player_data)
    print(f"Player {name} added successfully.")

def add_team(name, country):
    team_data = {
        "name": name,
        "country": country,
        "created_at": datetime.utcnow()
    }
    teams_collection.insert_one(team_data)
    print(f"Team {name} added successfully.")

def add_match(home_team_id, away_team_id, date, result):
    match_data = {
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "date": date,
        "result": result,
        "created_at": datetime.utcnow()
    }
    matches_collection.insert_one(match_data)
    print("Match added successfully.")

def get_players_by_team(team_id):
    players = players_collection.find({"team_id": team_id})
    return list(players)

def get_teams():
    teams = teams_collection.find()
    return list(teams)

def main():

    add_team("Barcelona", "Spain")
    add_team("Juventus", "Italy")
    add_team("Paris Saint-Germain", "France")

    add_player("Lionel Messi", 1, 30, 15)
    add_player("Cristiano Ronaldo", 2, 25, 10)
    add_player("Neymar Jr.", 3, 20, 18)

    add_match(1, 2, datetime(2024, 3, 1), {"home_goals": 2, "away_goals": 1})

    barcelona_players = get_players_by_team(1)
    print("Players in Barcelona:")
    for player in barcelona_players:
        print(player)

    all_teams = get_teams()
    print("All Teams:")
    for team in all_teams:
        print(team)

if __name__ == "__main__":
    main()
