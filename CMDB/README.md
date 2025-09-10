# CMDB

A lightweight configuration management database (CMDB) for storing database

instances and their associated accounts. Databases and account entries can be
browsed via a small web UI that also exposes a per-account view to see which
databases use a given credential. Entries can be edited or removed directly
from the interface.


## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python CMDB/app.py
   ```

3. Open `http://127.0.0.1:5000` in a browser to access the UI. Use the navigation
   links to add databases, manage accounts, or view where a specific account
   exists across databases.

The application uses SQLite for storage and creates a local `cmdb.db` file in the
repository.

