import os, shutil
from datetime import datetime

def backup_db():
    # copy quotes.db to quotes_<date>.db
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    shutil.copy("quotes.db", f"quotes_{now}.db")