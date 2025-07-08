import sqlite3

#set up database to store player data
def create_db():
    con = sqlite3.connect("players_data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS player(name, email)")

#learn how to make the players list populate from the db   
players_list = ["Dalton", "Colton", "Emily"]###need to update this variable to pull from db, not just have a static list.
players_data = {}
#determine what players are playing this round of golf.
def get_players():
    #store a list of current players for the round
    current_players = []
    while True:
        current_players_list = [p for p in players_list if p not in current_players]
        if not current_players_list:
            break
        player = input(f"Please select player or type 'add player' to register a new player\n {current_players_list}\n")
        ###Need to make sure the newly added player gets stored in db to be selectable next time the program runs, added to the current player variable, and player also does not
        ###need to show up in the current players list.
        if player == "add player":
            player_registration(current_players)#if no player to select from, we need to call the player registration function here
            continue
        if player in current_players_list:
            current_players.append(player)
            current_players_list.remove(player)#once a player is selected, it needs to be removed from the current rounds list of selectable players.
            break     
    if not current_players_list:
        print("Good luck on your round today!")
        print(f"The players for the round today are\n")
        print(*current_players, sep=", ")
    else:
        while current_players_list: 
            next_player = input(f"Who else is playing with you today? If no one else is playing, please type 'none' to continue.\n {current_players_list}\n")
            if next_player == 'none':
                break
    #update current players and remove them from list of selectable players
            if next_player in current_players_list:
                current_players.append(next_player)
                current_players_list.remove(next_player)
    #all players have been selected or no one else is playing
    print("Good luck on your round today!")
    print(f"The players for the round today are\n")
    print(*current_players, sep=", ")
    

        
#function to register and store data of a new player
def player_registration(current_players):
    player_name = input("Enter player name\n")
    player_email = input("Enter your email\n")
    players_list.append(player_name)
    players_data["name"] = player_name
    players_data["email"] = player_email
    print(players_data)
    print(players_list)
    ###need to make this function also update sqlite db


get_players()

