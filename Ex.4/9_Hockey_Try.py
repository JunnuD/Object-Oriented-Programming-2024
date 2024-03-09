import json

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def search_for_player(data, name):
    for player in data:
        if player['name'].lower() == name.lower():
            print(f"{player['name']} {player['team']} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")
            break
    else:
        print("Player not found.")


def list_teams(data):
    teams = sorted({player['team'] for player in data})
    for team in teams:
        print(team)

def list_countries(data):
    countries = sorted({player['nationality'] for player in data})
    for country in countries:
        print(country)


def interactive_shell(data):
    while True:
        print("commands:\n0 quit\n1 search for player\n2 teams\n3 countries")
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            name = input("name: ")
            search_for_player(data, name)
        elif command == "2":
            list_teams(data)
        elif command == "3":
            list_countries(data)
            
def list_players_in_team(data, team):
    players = [player for player in data if player["team"] == team.upper()]
    sorted_players = sorted(players, key=lambda x: (x["goals"] + x["assists"], x["goals"]), reverse=True)
    for player in sorted_players:
        print(f'{player["name"]} {player["team"]} {player["goals"]} + {player["assists"]} = {player["goals"] + player["assists"]}')


def main():
    filename = input("file name: ")
    data = load_data(filename)
    if data:
        print(f"read the data of {len(data)} players")
        interactive_shell(data)

if __name__ == "__main__":
    main()

