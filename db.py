import sqlite3


#set up database to store player data
def create_db():
    con = sqlite3.connect("players_data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS player(name TEXT, email TEXT)")
    con.commit()
    con.close()
#finish function

def load_players_from_db():
    con = sqlite3.connect("players_data.db")
    cur = con.cursor()
    cur.execute("SELECT name FROM player")
    rows = cur.fetchall()
    con.close()
    #print(row[0] for row in rows)
    return [row[0] for row in rows]

def add_player_to_db(player_name, player_email):
    con = sqlite3.connect("players_data.db")
    cur = con.cursor()
    cur.execute("INSERT INTO player (name, email) VALUES (?, ?)", (player_name, player_email))
    con.commit()
    con.close()

#def delete_player_from_db():
