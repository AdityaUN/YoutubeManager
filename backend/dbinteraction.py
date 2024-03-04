import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    

def main():
    while True:
        pass
    con.close()


if __name__ == "__main__":
    main()