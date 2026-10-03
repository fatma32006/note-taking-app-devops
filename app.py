from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "noteuser",
    "password": "NotePass123!",
    "database": "notesdb"
}


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/", methods=["GET"])
def home():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, note, created_at FROM notes ORDER BY created_at DESC"
    )

    notes = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    note = request.form["note"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO notes (note) VALUES (%s)",
        (note,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


@app.route("/edit/<int:note_id>", methods=["POST"])
def edit_note(note_id):
    note = request.form["note"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE notes SET note = %s WHERE id = %s",
        (note, note_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM notes WHERE id = %s",
        (note_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
