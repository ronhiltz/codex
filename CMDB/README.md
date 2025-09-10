# CMDB

A lightweight configuration management database (CMDB) for storing database
instances and their associated accounts.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python CMDB/app.py
   ```
3. Open `http://127.0.0.1:5000` in a browser to access the UI.

The application uses SQLite for storage and creates a local `cmdb.db` file in
the repository.
