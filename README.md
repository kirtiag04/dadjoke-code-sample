# dadjoke-code-sample
Generates a random dad joke and save user opinions for those jokes

### The dadjoke applicatiion is designed using Flask, Python-based web framework
### On the home page, we have five buttons
Generate joke button - generates random joke from dad-joke generator (https://icanhazdadjoke.com/ API)
Like, Dont Like, Dont Care buttons - save the opinion of the user for a particular joke 
Summary button - displays the summary of opinions for a particular user. Renders a summary page with the list of jokes and user opinions. There is also a link to go back to the home page

Note: For now, all the jokes are generated and all the opinions are saved for one particular user only. We can extend this application for multiple users as the table in the database has a field for username. 


## Requirements and how to run

Install Python2.7 

### Install pip
sudo apt-get install python-pip

### Install virtualenv
sudo pip install virtualenv

### Go into dadjoke directory 
cd dadjoke (on Windows machine, if there is a dadjoke folder within dadjoke folder after unzip, then cd dadjoke/dadjoke)

### Create a virtual env
virtualenv joke

### Activate virtual environment
source joke/bin/activate
source joke/scripts/activate (on Windows machine)

### Install depencies
pip install -r requirements.txt

### Create a database
python db_create.py

### Run flask application (by default it runs on port 5000)
python run.py



## API documentation

### Home page
Render home page of the application
URL - / and /index
Method - GET
Success Response - 200 
Error response - 500

### Generate joke
Generates a random joke from https://icanhazdadjoke.com/ API
URL - /generate
Method - GET
Success Response Code - 200
Success Respone Body - 	{
						  "id": "R7UfaahVfFd",
						  "joke": "My dog used to chase people on a bike a lot. It got so bad I had to take his bike away.",
						  "status": 200
						}

### Save user opinion
Save user opinion to the database
URL - /save-opinion
Method - POST
Success Response - 200
Error response - 500

### Summary 
Renders a summary page of the user opinions
URL - /summary
Method - GET
Success Response - 200
Error response - 500

