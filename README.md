## mp4rer: Automatic Webm to MP4 Converter

This repository contains `mp4rer.py`, a Python script that automates the conversion of newly added webm files to mp4 format within a specified directory.

### Features

* **Automatic Conversion:** Effortlessly converts webm files to mp4 upon arrival in the monitored directory.
* **Lightweight Script:** Maintains efficiency with a concise Python script.
* **Dependency Management:** Leverages the `watchdog` library for file system monitoring and `ffmpeg` for video conversion.

### Benefits

* **Streamlined Workflow:** Simplifies video format conversion, saving time and effort.
* **Organization:** Ensures consistency in video format within your directory.

### Getting Started

**Prerequisites:**

* Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* `watchdog` library (`pip install watchdog`)
* `ffmpeg` ([https://ffmpeg.org/](https://ffmpeg.org/))

**Instructions:**

1. Clone this repository or download the `mp4rer.py` script.
2. Install the `watchdog` library using your terminal:

   ```bash
   pip install watchdog
   ```

3. Ensure `ffmpeg` is installed on your system. You can usually install it using your system's package manager (e.g., `apt install ffmpeg` on Ubuntu/Debian).

4. Edit the `mp4rer.py` script (optional):

   - Change the `watch_dir` variable to the path of the directory you want to monitor for webm files.

5. Run the script:

   ```bash
   python mp4rer.py
   ```

   This will start monitoring the specified directory and convert any new webm files to mp4 format.

### Usage

The script will continuously monitor the `watch_dir` directory. Whenever a new file with the `.webm` extension is added, it will be automatically converted to an mp4 file with the same name (but `.mp4` extension).

### Contributing

We welcome contributions to this project! Feel free to submit a pull request with any improvements or bug fixes.

### License

This project is licensed under the MIT License (see LICENSE file for details).

### Additional Notes

* This script uses the basic functionalities of `watchdog` and `ffmpeg`. You can explore their documentation for more advanced features.
* Feel free to report any issues or suggest improvements.