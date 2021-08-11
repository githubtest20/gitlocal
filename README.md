Background
==========
This application will help you reserve tickets and the seats
are auto assigned based on the request/input from the user and
update the seats in JSON file to 'RESERVED' and save it for future feed.

Install
=======
Install the JSON package if not already available in the system-package

'pip install json'

If you're on Windows, make sure you installed the `pip.exe` component when you
installed Python, a package management to install additional packages as required
by the application.

Run the Code
============
Launch the powershell in Windows or Shell as required

1.Run the respective client.
2.Run the command 'python -m Reservation '<file_path>'' to launch the application.
3.The code will user_input i.e nos of tickets to be booked.
4.System assign the tickets and update the respective seats to 'RESERVED' in the file.
5.Finally application will printout the seats confirmation.

Run Script Manually
===================
1.create script.sh file with python script to run.
2.run './script.sh '<filepath>''
NOTE : makesure to run the script from respective path, as in python module.
