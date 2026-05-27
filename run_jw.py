import subprocess
import sys
import os
import webbrowser
import threading
import time


def open_browser():
    time.sleep(2)
    webbrowser.open("http://localhost:8501")


def run():
    threading.Thread(target=open_browser).start()

    app_path = os.path.join(os.path.dirname(__file__), "jw.py")

    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        app_path
    ])


if __name__ == "__main__":
    run()