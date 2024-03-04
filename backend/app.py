from flask import Flask, request, jsonify
import sqlite3


def list_videos():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM Videos")
    records = cur.fetchall()
    
    con.close()

    return records


app = Flask(__name__)

@app.route("/api/video")
def video():
    return list_videos()

@app.route("/api/create-video/", methods=["POST"])
def create_video():
    # Extract data from request
    name = request.args.get('name')
    time = request.args.get('time')

    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

    con.close()

    return jsonify({'message': f'Video "{name}" created successfully (time: {time})'}), 201


if __name__ == "__main__":
    app.run(debug=True)