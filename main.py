
from player import get_players
from db import create_db, load_players_from_db

def main():
   create_db()
   players_list = load_players_from_db()
   get_players(players_list)

#run the app
if __name__ == "__main__":
    main()
