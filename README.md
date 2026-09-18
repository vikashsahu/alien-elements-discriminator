### Background
The [Alien Elements Lab](https://www.learningundefeated.org/curriculum/alien-elements/) is a high school chemistry/data science activity involving two main tools. While the [CODAP](https://codap.concord.org/) data analysis platform runs in the browser, the Alien Elements Lab involves a python script called the "discriminator", a [tkinter](https://docs.python.org/3/library/tkinter.html)-based GUI application that requires a standalone device to run.

For a classroom that has no such available devices (desktop, non-chromebook laptop, or tablet as the activity suggests), a web-app solution is needed. This project is a simple hosted version of the tkinter app.

### Live Link
Currently available at https://sahwho.pythonanywhere.com/, however this URL will likely change to something like https://sahwho.pythonanywhere.com/discriminator in the future. Docs will be updated when that happens.

### This Project
A [Flask](https://flask.palletsprojects.com/en/stable/) application hosted on [pythonanywhere](https://www.pythonanywhere.com/)'s free tier. Because of how basic the [original script](https://www.learningundefeated.org/wp-content/uploads/2025/07/Octet_Rule_GUI-2.0.txt) is, there's no real "backend" to speak of, no database, etc. Just 2 main functions (check_octet_rule and get_valence_electrons) as well as a function that converts numbers to their Unicode subscript equivalents. 

### Local Development
1. Clone the project from this github repo (once)
2. run ```pip install -r requirements.txt``` to install the dependencies.
3. ```flask --app main run``` in your command line
4. visit 127.0.0.1:8080 in your browser
Live reloading isn't a thing (I'm pretty sure), so you'll likely need to stop and restart the app each time local changes are made. This could be a potential future improvement.

### Sample Valid Input: I₂T
First Element: I
First Element Count: 2
Second Element: T
Second Element Count: 1
