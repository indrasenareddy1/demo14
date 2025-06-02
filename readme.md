copilot_test.py
Overview
copilot_test.py is a Python script that displays the system's uptime.

On Windows, it uses the net stats srv command to show how long the system has been running.
On Unix/Linux, it reads from /proc/uptime to calculate and display the uptime in hours and minutes.
How to Run
Make sure you have Python installed (version 3.x).
Open a terminal or command prompt.
Navigate to the directory containing copilot_test.py.
Run the script using:
bash
python copilot_test.py
On Windows, the script will print the system's uptime (since last boot).
On Unix/Linux, it will display the uptime in hours and minutes.
