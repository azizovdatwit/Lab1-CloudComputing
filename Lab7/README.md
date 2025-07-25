This project executes sql queries from LAB 5 using python command line driver. 

Main file here is driver.py. That's where cld is implemented, also it is where I made the connection 
between python and mysql using cursor object. Note: I added port 3307 to execute the queries on the instance from LAB 6.
Also, all the sql queries are stored in a variable called sqlQueris as dictionary. 

Since this is built off of Lab 6, you should already have the instance and container that is connected, if not here how to do that: 
To create an image of this project in docker:
Clone the repository in source code then cd into Lab 6 folder
Enter the command: "docker-compose -f DockerCompose.yaml up" in the terminal. make sure you are in the right dir.
Create an instance on either dbeaver or mysql workbench where port number is 3307 and enter your password to check connection is successful. If you see error about public key retrival, 
under driver properties change public key retrival from false to true. Then check again, it should work. Then upload my_guitar_shop here and execute queries.


After that, go to driver.py file and run it. It'll expect a number between 0-10 to execute queries. After testing, you can enter 0 to exit out.

If you want to check testQueries.py file that contains unittests, you can right click on the file and select run from the menu. You need to be in the correct directory which is Lab1/Lab7

