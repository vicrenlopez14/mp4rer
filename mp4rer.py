import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys

def convert_webm_to_mp4(filepath):
    """Converts a webm file to mp4 using ffmpeg"""
    filename, _ = os.path.splitext(filepath)
    output_path = f"{filename}.mp4"
    command = ["ffmpeg", "-i", filepath, "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", output_path]
    subprocess.run(command)

class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        """
        Esecutes convert_webm_to_mp4 function when a new file is created
        """
        if not event.is_directory and event.src_path.endswith(".webm"):
            filepath = event.src_path
            convert_webm_to_mp4(filepath)

if __name__ == "__main__":
    # Take the path of the directory to watch from command line arguments
    watch_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    observer = Observer()
    observer.schedule(Watcher(), watch_dir, recursive=False)
    observer.start()
    try:
        print(f"Watching {watch_dir} for new webm files")
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Stopping...")

    

    