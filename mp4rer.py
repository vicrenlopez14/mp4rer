import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import time

incomplete_files = {} # Dictionary to store incomplete file paths and timestamps

def convert_webm_to_mp4(filepath):
    """Converts a webm file to mp4 using ffmpeg"""
    filename, _ = os.path.splitext(filepath)
    output_path = f"{filename}.mp4"
    command = ["ffmpeg", "-i", filepath, "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", output_path]
    subprocess.run(command)

class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        """
        Executes convert_webm_to_mp4 function when a new file is created
        """
        if not event.is_directory and event.src_path.endswith(".webm"):
            filepath = event.src_path
            if os.path.getsize(filepath) == 0:
                print(f"File {filepath} is empty. Skipping...")
                incomplete_files[filepath] = time.time()
            else:
                convert_webm_to_mp4(filepath)
                
    def on_modified(self, event):
        """
        Executes convert_webm_to_mp4 function when a file is modified
        """
        if not event.is_directory and event.src_path.endswith(".webm"):
            filepath = event.src_path
            # Get file modification time
            stat = os.stat(filepath)
            last_modified = stat.st_mtime

            # Check if last modified time is greater than 5 seconds
            if (time.time() - last_modified) > 5:
                convert_webm_to_mp4(filepath)

if __name__ == "__main__":
    # Take the path of the directory to watch from command line arguments
    watch_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    observer = Observer()
    observer.schedule(Watcher(), watch_dir, recursive=False)

    # Start the observer in a separate thread
    observer.start()

    try:
        print(f"Watching {watch_dir} for new webm files")

        # Loop to monitor incomplete files in the main thread
        while True:
            # Create a copy of the dictionary to avoid modification during iteration
            for filepath, updated_at in incomplete_files.copy().items():
                # Check if file size is now greater than 0 and time difference is sufficient
                if os.path.getsize(filepath) > 0 and time.time() - updated_at > 2:
                    convert_webm_to_mp4(filepath)
                    del incomplete_files[filepath]  # Remove from incomplete list after success
                # You can add additional logic here to handle timeouts or retries for failed conversions
            time.sleep(1)  # Adjust sleep time as needed

    except KeyboardInterrupt:
        observer.stop()

    observer.join()  # Wait for the observer thread to finish before exiting
    print("Stopping...")