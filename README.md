# Note-Taking Website on AWS EC2

## 1. Project Overview

This project is a simple Note-Taking Website deployed on an AWS EC2 instance.

The application allows users to:
- Write and save notes.
- Display saved notes with their timestamps.
- Edit existing notes.
- Delete notes.

The notes are stored in a MariaDB database running on the same EC2 instance.

A separate Amazon EBS volume is attached to the EC2 instance and mounted at `/backup` to store database backup files.

---

## 2. Technologies Used

- AWS EC2
- Red Hat Enterprise Linux (RHEL) 10
- Python 3
- Flask
- MariaDB
- MySQL Connector for Python
- Amazon EBS
- systemd
- Bash
- Vim
- MobaXterm

---

## 3. AWS EC2 Configuration

The application was deployed on an AWS EC2 instance running RHEL 10.

The Security Group allows:
- SSH (TCP 22)
- HTTP (TCP 80)

The Flask application listens on port 80.

---

## 4. Project Structure

```text
note-app/
├── app.py
├── backup.sh
├── README.md
└── templates/
    └── index.html



Files Description
app.py: Main Flask application and database operations.
templates/index.html: Web interface for creating, editing, deleting, and displaying notes.
backup.sh: Bash script used to create MariaDB database backups.
README.md: Project documentation.





5.MariaDB Database

MariaDB was installed and configured on the EC2 instance.

A database named notesdb was created.

The application uses a table named notes with the following columns:

Column	Type	Description
id	INT	Unique note ID
note	TEXT	Note content
created_at	TIMESTAMP	Note creation time

A dedicated MariaDB user named noteuser was created for the application.








6.Flask Web Application

The application was developed using Python and Flask.

The main routes are:

/ - Displays all notes.
/add - Adds a new note.
/edit/<note_id> - Edits an existing note.
/delete/<note_id> - Deletes a note.

Notes are displayed with the newest notes first.




7.EBS Backup Volume

A separate 1 GiB Amazon EBS volume was created and attached to the EC2 instance.

The volume was formatted using XFS and mounted at:

/backup

The mount was also configured in /etc/fstab using the volume UUID so that the volume can be mounted automatically after reboot.




8.Database Backup

The MariaDB database is backed up using mysqldump.

The backup files are stored inside:

/backup

Example backup file:

/backup/notesdb_2026-09-23_03-45-51.sql

The backup was verified by checking the generated SQL file and confirming that it contains the notesdb database and its table structure.




9.Backup Script

The backup process is automated using the Bash script:

backup.sh

The script creates a timestamped SQL backup file inside /backup.

Example:

notesdb_YYYY-MM-DD_HH-MM-SS.sql

The script also checks whether the backup operation completed successfully.




10.systemd Service

The Flask application was configured as a systemd service.

Service file:

/etc/systemd/system/note-app.service

The service starts the Flask application automatically and is configured to restart if the application stops unexpectedly.

The service was enabled and started using systemd.




11.Testing

The application was tested through the EC2 public IP address.

The following operations were tested successfully:

Creating a note.
Displaying saved notes.
Editing a note.
Deleting a note.
Storing notes in MariaDB.
Creating a database backup.
Storing backup files in /backup.
Running the application as a systemd service.





12.Screenshots

The project includes screenshots showing:

Running Note-Taking Website.
MariaDB database and table.
EBS volume mounted at /backup.
Database backup files stored in /backup.
systemd service status.





13.Conclusion

The Note-Taking Website was successfully deployed on AWS EC2 using Flask and MariaDB.

The project also includes a separate EBS volume for storing database backups, providing a simple backup strategy for the application's database.
