# LSWA-Project
NY Restaurant Sanitation Lookup

## Things that need to be done in the backend:

1. Output a table of restaurants underneath where the user hits the search button
2. Each restaurant should have a button next to it that says "This restaurant made me sick"
3. If the user is logged in, they should be able to hit that button and add that restaurant to their table
4. Otherwise, the button should redirect them to the login page
5. Each restaurant should have a border color that corresponds with its sickness count. Red = high, Yellow = medium, Green = low
6. If a logged in user clicks on "Dashboard", he or she should be able to access the restaurants that made him/her sick
7. Otherwise, the dashboard should lead the user to the login page
8. When the user logs in, the service should check if the email exists in the database and that the password matches.
9. When the user registers, the service should check if the email is already in the database and then output and error message. 
10. Otherwise, the service should add the information to the users database and redirect the user to the login page. (Or output a message that tells them to go to the login page).


## Running the containers
docker-compose up nginx