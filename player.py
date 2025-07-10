#function to register and store data of a new player
from db import add_player_to_db, load_players_from_db



def player_registration(players_list, current_players):
    player_name = input("Enter player name\n")
    player_email = input("Enter your email\n")
    if player_name not in players_list:
        #players_list.append(player_name)
        add_player_to_db(player_name, player_email)
        current_players.append(player_name)
        players_list = load_players_from_db()
    else:
        print("Player is already registered")
    return players_list
    ###need to make this function also update sqlite db

def get_players(players_list):
    #store a list of current players for the round
    current_players = []

    if not players_list:
        player_registration(players_list, current_players)
    while True:
        current_players_list = [p for p in players_list if p not in current_players]
        if not current_players_list:
            break
        player = input(f"Please select player or type 'add player' to register a new player\n {current_players_list}\n")
        ###Need to make sure the newly added player gets stored in db to be selectable next time the program runs, added to the current player variable.
        if player == "add player":
            player_registration(players_list, current_players)#if no player to select from, we need to call the player registration function here
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