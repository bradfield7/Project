# Project
this repo is my files for my QA 2021 devops first project

## Contents:
* [Project Brief](#Project-Brief)
* [App Design](#App-Design)
* [CI pipeline](#CI-Pipeline)
* [Risk Assessment](#Risk-Assessment)
* [Tests](#Tests)
* [App](#App)
* [Known Issues](#Known-Issues)
* [What i'd add in the future](#What-i'd-add-in-the-future)


## Project Brief:
for this project I was required to produce an app with CRUD functionality (create, read, update, delete) which would use a flask framework and would use at least two tables including a one-to-many relationship.

## App Design:
For my app I decided to keep it simple as I am new to coding, the premise of my app was to create what is basically a questionnaire for football fans. Clubs are inputted manually, then a fan would fill out their information and that will link to the club. Someone could then look at the fans linked to a club to see if there exists any correlations, such as if certain clubs in London have a fanbase with a lower average income than another London club. In this case the club would be the parent and the fan would be the child in this one-to-many relationship. This is my ERD:

![ERD](https://github.com/bradfield7/Project/blob/main/images/chart.png)

## CI Pipeline:
The project also requires good use of a typical CI pipeline, this involves using jira to create a scrumboard and manage sprints, using github to control versions and show good use of pushes and branching.
![Jira](https://github.com/bradfield7/Project/blob/main/images/sprintboard.png)
this is a sample of my tasks in my sprint

![burn](https://github.com/bradfield7/Project/blob/main/images/sprintburndown.png)
this is the burndown chart for my project

We use a virtual environment within a virtual machine as our development environment, the virtual environment (venv) is used so that you can use specific pip installs in that area without it conflicting with other versions that may be on the same machine for other projects.

Lastly we use Jenkins as our server to build and automate testing, this is done following adding scripts and will test every commit made to github with the use of the webhook

## Risk Assessment:
This is a risk assessment I made for the apps development and deployment process, I have taken into account the virtual risks and the real life risks

![RA](https://github.com/bradfield7/Project/blob/main/images/risk.png)

## Tests:
Testing should ideally include high coverage and all passes on any tests included. A high coverage means that the majority of lines of your code have been included in some form of test, so a low coverage is more likely to allow bugs and errors to slip through the cracks. A failed test simply means that either your test has an error or your actual code has a big error, which could be fatal to the app, therefore all tests should be passed.
![test1](https://github.com/bradfield7/Project/blob/main/images/testonvs.png)
the tests within my environment, showing 100% coverage

![test2](https://github.com/bradfield7/Project/blob/main/images/testonjenkins.png)
showing the tests also ran in jenkins automatically

## App:
On my app you are greeted by the title followed by the 4 options. 2 to add details for a fan or a club and another 2 to view fans or clubs.
![home](https://github.com/bradfield7/Project/blob/main/images/homescreen.png)
![fanlist](https://github.com/bradfield7/Project/blob/main/images/fanlist.png)
![club](https://github.com/bradfield7/Project/blob/main/images/addclub.png)

## Known Issues:
One issue I currently encounter is if a fan tries entering a club id that doesn't exist then it throws an error until you submit a correct one, while it is technically doing what it should I would have preferred to have found a way to add an in-page error rather than a website crash.

## What i'd add in the future :
With more knowledge and experience I would add an option list that changes depending on the league selected, so first selecting 'premier league' from my drop down would then only show clubs that have been tagged as being in that league. I would also like to add a way for the parent class to see specifically which fan is supporting, currently it only tags the fan number which isn't as helpful.

the endgame idea for the app would be to find a way to then show the average income for each particular club, as well as seeing a tally of locations to see where popular fanbases are held in the country.
