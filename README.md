# BlueStackProject



please install these package:
pip install -U selenium
pip install -U pathlib
or pip install -r requirements.txt
RUN instructions -------
step 1 - clone the project from hithub.com
for cloning - git clone "https://github.com/viveksh991/BlueStackProject.git"

step 2 - open file in any editor - like pycharm, sublime or Note++
for problem_1.py - no need to any changes
for problem_2.py - please change the assignment_folder path

step 3 - open cmd or terminal and type these commands

        - use cd for going the project location like - cd PycharmProjects\BlueStackProject
        - then type python problem_1.py - for running the problem_1
        - then type python problem_2.py - for running the problem_2

        Or you can do manually from pycharm run button

=======================================  Problem_Statement and his Steps ===============================================================
Problem - 1:
Write a script to get all the “Game Control” instructions as shown in the left Panel and print them as a Dictionary after Playing a Game from Now.gg Website.

1. hit this url - "https://now.gg/apps/perfect-world/7724/perfect-world-mobile.html"

2. Click on Play in Browser:

3. When you start playing the game, Game Control Window will appear

4. Get all data related to the Game Control Window and Dump it to the file.


Problem - 2:
You are required to write a function which will scrape some logs and return the data from the log file. Data will be scraped according to the following steps.

1. Unzip the file present on the drive. (This step can be done manually)

2. Read the file start_assignment.log and search for the string "beginning of assignment".

3. Now search for the pattern "required_pattern_.*" after "beginning of assignment" had already occurred and grabbed the first occurrence of it.

4. Search the file at location "Logs\" with name as the pattern found in start assignment.log

5. Finally in the file present at location "Logs\" search for the string "assignment_completed" and return its next line
