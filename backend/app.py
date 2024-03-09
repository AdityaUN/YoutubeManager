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
    created_id = cur.lastrowid
    con.commit()

    con.close()

    data = {
        "message": f'Video "{name}" created successfully time: {time}',
        "createdId": created_id
    }

    return jsonify(data), 201

@app.route("/api/delete-video/", methods=["DELETE"])
def delete_video():
    # Extract data from request
    id = request.args.get('id')

    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()

    cur.execute("DELETE FROM videos WHERE id = ?", (id,))
    con.commit()

    con.close()

    return jsonify({'message': f'Video with "{id}" deleted successfully'}), 201

if __name__ == "__main__":
    app.run(debug=True)