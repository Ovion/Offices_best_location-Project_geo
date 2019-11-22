# Project-MongoDB

## You recently created a new company in the `GAMING industry`, and you want the best location for your office.


The company will have the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President

As a data engineer I will ask for your preferences on where to place the new office.

You have to found a place that more or less covers all the following requirements.
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.

- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far. (Coming soon)

## main.py
----------
This is the main file, must be run on the terminal.

1. First of all the programm will ask about if you want to load the content in mongo compass. You should answer with a 'y' for yes or 'n' for no.

2. Then it will ask for your preferences about the three requirements previuos mentioned. Please the input must be a number.

3. Later it will show you a list of the three top cities where to place your new office.

4. Then the programm do they magic and a webbrowser will be pop with the best location.
 
### Functions and filters
-------------------------

In the folder called `functions` the are several files that I used to put there all the functions that I use in main, filters to clean and geolocalize the best position and a specific file to representate the map.

### MongoDB collections
-----------------------
In the folder called `collections_mdb` there are mongo db collections in order to representate the final map.




