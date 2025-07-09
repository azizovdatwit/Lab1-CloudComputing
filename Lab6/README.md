This project demonstrates containerization of the Lab 5 for my_guitar_shop database.

Project uses docker compose to connect docker to the my_guitar_shop database. - it uses this file to containerize SQL queries that was done for LAB 5

 how to run your project:
 To create an image of this project in docker:
Clone the repository in source code then cd into Lab 6 folder
Enter the command: "docker-compose -f DockerCompose.yaml up" in the terminal. make sure you are in the right dir.
Create an instance on either dbeaver or mysql workbench where port number is 3307 and enter your password to check connection is successful. If you see error about public key retrival, 
under driver properties change public key retrival from false to true. Then check again, it should work. Then upload my_guitar_shop here and execute queries.

Another way to verify :

Open Docker go to containers and under actions, run the container
After this, open the terminal in Docker and  enter the command: docker exec -it sqlScripts mysql -uroot -p
It should ask for a password which is MYSQL_ROOT_PASSWORD var on docker compose file then you'll be able run your mysql queries.
Once in mysql, use sql commands to view the data such as show tables or show databases, etc. 

