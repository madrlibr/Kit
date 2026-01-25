import sys
from .main import *

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: kit [gp|gpm|gs|gaa|gc|ru|cb|cd|gs]")
        return

    command = sys.argv[1].lower()
    command2 = sys.argv[2] if len(sys.argv) > 2 else None

    if command == "gp":
        git_pull()
    elif command == "acp":
        add_commit_push(command2)
    elif command == "gm":
        commit(command2)
    elif command == "gaa": 
        git_add_all()
    elif command == "ru":
        remote_url()
    elif command == "cb":
        current_branch()
    elif command == "cd":
        changes_diff()
    elif command == "gs":
        git_status()
    elif command == "iap":
        init_and_push(remote_url=command2)
    else:
        print(f"Error: Perintah '{command}' tidak dikenal.")
        print("Perintah yang tersedia: [gp|gpm|gs|gaa|gc|ru|cb|cd|gs]")