
    
players_list = ["Dalton", "Colton"]
players_data = {}
#determine what players are playing this round of golf
def get_players():
    current_players_list = players_list
    current_players = []
    player = input(f"Please select player or type add player to register a new player\n {current_players_list}\n")
    #if no player to select from, we need to call the player registration function here
    if len(current_players_list) == 0 or input == "add player":
        player_registration()
    
    
    
     
    
    current_players.append(player)
    #once a player is selected, it needs to be removed from the current rounds list of selectable players.
    current_players_list.remove(player)
    next_player = input(f"Who else is playing with you today? If no one else is playing, please type 'none' to continue.\n {current_players_list}\n")
    current_players.append(next_player)
    current_players_list.remove(next_player)
    if next_player == 'none' or len(current_players_list) == 0:
        print("Good luck on your round today!")
        
    #fix the issue if the selection is 'none'. As of now, we get a ValueError since 'none' is not in the list.
    print(f"The players for the round today are\n {current_players}")
    #when the current players are printed at this point, it needs to be reformatted for cleaner output and readability.
    

        
#function to register and store data of a new player
def player_registration():
    player_name = input("Enter player name\n")
    player_email = input("Enter your email\n")
    players_list.append(player_name)
    players_data["name"] = player_name
    players_data["email"] = player_email
    print(players_data)
    print(players_list)

get_players()
