# File Monitoring and SQLite Database Sync Script

This Python script continuously monitors a specified directory (default: `media`) and updates an SQLite database (`db.sqlite3`) with the names of new files found in that directory. It is useful for keeping track of new files added to a folder, ensuring no duplicates in the database, and recording file creation timestamps.

## Features

- **Database Initialization**: The script will automatically create an SQLite database if it doesn't exist. The database will store file names along with their creation timestamps.
- **Continuous Monitoring**: The script periodically checks a specified directory for any new files and updates the database.
- **Duplicate Prevention**: The database ensures that no duplicate file names are entered by enforcing a unique constraint on the file names.
- **File Metadata**: Each file entry includes the file's name and the timestamp when it was added to the database.
- **Flexible Configuration**: The script can be easily configured to monitor a different folder or adjust the polling interval.

## Requirements

- **Python 3.x**: The script is written in Python 3.
- **SQLite3**: SQLite is a self-contained database engine and comes pre-installed with Python, so there is no need for additional setup.

## Installation

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/file-monitoring-script.git
cd file-monitoring-script
