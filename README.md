# **RPS(Rock, Paper, Scissors)**
## **Site Overview**
A simple 2 round game of rock paper scissors developed with python.

### [Click here to view repository](https://github.com/leebri101/rock-paper-scissors)

## Contents-Page:
1. [**Site Overview**](#site-overview)
1. [**Project-Planning**](#project-planning)
    * [**Target Audiences:**](#target-audiences)
    * [**User Stories**](#user-stories)
    * [**Site Objectives:**](#site-objectives)
    * [**How Is This Will Be Achieved:**](#how-will-this-be-achieved)
1. [**Current Features on all pages**](#current-features-on-all-pages)
    * [**Headers:**](#headers)
        * [*Title*](#Title)
        * [*Call To Action Button*](#call-to-action-button)
        * [*Start Game Section*](#start-game-section)
      * [**Quiz-Section**:](#quiz-section)
          * [*Quiz-Tracker*](#quiz-tracker)
      * [**Questions and Answers**:](#questions-and-answers)
          * [*Q and A*](#q-and-a)
    * [**Point-Tracker**](#point-tracker)
    * [**Results-Section**](#results-section)
    * [**Footer**](#footer)
    * [**Typsetting**](#typesetting)
1. [**Potential-Features**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference:**](#general-reference)
    * [**Content**](#content)
    * [**Media**](#media)

## **Project Planning**
### **Target Audiences:**
* For users who are interesting in a playing short games.
* For users who want to play a simple game of static rock paper scissors

<!-->
### **Site Objectives:**
* 
* Educating the user on using this as a fun way of educating themselves.

### **User Stories:**
* As a user I want to give feedback via the given social media links to further 
improve/enhance the quiz to the owner.
* As a user I want to be able to easily navigate the quiz with ease.
* As a user I want have fun on short quizs without being bored.
* as a user I want the quiz to be as simple easy to understnd.

### **How will this be achieved:**
* The landing page with have a simple CTA (Call To Action) input button at which the user must ineteract with to continue the quiz.
* The page will have the following things:
    * A large coloured CTA play button at which when the user/player hovers over, a small animation will occur and change colours briefly tempting the user to click it which leads to a different pop up to appear.
    * A small text box which the user has to input their name to start the quiz, if nothing has been inputted the quiz cannot start.
    * A series of questions out of ten which displays the question, and four different options at which the user must pick one correct answer to see if it is correct or not.
    * A results page which gives feedback to players as to how many questions they have answered correctly out of 10. 

There was small changes from the planned wireframes to enhance the UX (User Experience). 
Changes include:-
* An interactive CTA play button which is changes color upon hovering.
* A placeholder on the start-game section text box for players to input their names and warning to users if they start the game with no input in the text box.
* An animation on the timer clock which shows a small stop watch shake after each second to indicate the user that time is ticking.
* A hover animation over the 4 different choices of answers within the answers section of the quiz which change color whilst the animation occurs.
* The results page having a box which shows the player's score and a coloured gradient on the border of the box which constantly spins aorund the edge of the box.
* A small Favicon to act as an icon for the webpage.

## **Current Features on all pages**
###  **Header**
* The header has been placed in the top center of the page to allow for a easy transition between desktop and mobile so it doesn't affect the page in huge way. 

 The header itself contains the following features: 

### *Title:*
* The Title is there to show the name of the page.

![Title](doc/screenshots/header.png)

#### *Call To Action Button:*
* The CTA is there with theme of the Earth to match the theme and catch the user's attention the moment that they enter the site. 
    

#### *Start Game Section:*
* The start game section has an autofocus placeholder on the text box which allows for more accessibilty to the user, which is useful on mobile devices as the text cursor is already highlighted in the text box which saves time for the user to manually navigate to it as. 
* Two interactive buttons for the user to input one of which is the Start Game, which upon text input and clicking the button will send the user to commence the geography quiz. The Quit button will send the user back to the main screen where the CTA button is displayed.
* A error handler which diplays a red border in the text box if the user hasn't provided any sort of text or name.
* An event listener where the user can press the ENTER key which has the same response as clicking the Start game button. 

  ![Start Game Section](doc/screenshots/placeholder-input.png)

### **Quiz-Section**:
#### *Quiz-tracker:*
Features used:
* A indicator display to track the current question number the user is on out of the total quiz questions.
* A countdown timer with a animation which moves each time a second is lost within the alloted time length.
* A countdown bar to also track time but visually display the length of time left in the bar.
![Quiz-section](doc/screenshots/tracker-update.png)

### **Questions and Answers**:
#### *Q and A:*
Features used:
* A question with a four choice option answer selector. 
* Users being able to select any answer before clicking next to proceed to the next question.
* Each answer having a hover animation with a color changing function,  the color also changes when the user clicks on answer. 
* The Fisher-Yates method used to shuffle all the questions and answers to any given random order out of ten. So no same question is used twice.

![Quiz-Questions](doc/screenshots/quiz-questions.png)

## **Point-Tracker**
* The point tracker is used to display to the user whether they have; answered the question correctly, gave an incorrect answer, did not give answer and to show which answer they are currently on.
* The point tracker is indicated in four different colors:
    * Green: Meaning the user has answered the question correctly.
    * Red: Meaning the user has answered incorrectly.
    * Gray: Meaning the user has ran out of time or can alternatively skip the question.
    * Yellow: To indicate to the user that they are on the current question.
![Point-Tracker](doc/screenshots/progress-tracker.png)

## **Results-Section**
* The results sections shows the following things:
    * The users score out of 10.
    * A feedback message to the user as to whatever associated score they have recieved.
    * A Play Again button if the users wishes to replay the quiz again.
![Resuts-Section](doc/screenshots/results-page.png)

## **Potential-Features**
* Due to the project deadlines being in a very tight timeframe the project had to be scaled down to a more simpler version of the RPS game but these are the features that I would like to potentially add or implement in the near future:
    * An 8bit animation for the end game displays.
    * potential 
    * A narration voice over for all the questions and answers for users with disablity issues.
    * A mixture of sound, images and text based questions and answers.
    * A shuffler for answer as well.

***
## **Testing-Phase**
Details of the testing phase are be found here: [TESTING.md](TESTING.md)
***

## **Deployment**

### **Heroku**
* Log into Heroku (creating an account if needed).
* Click the "New" button from the dashboard, under the header in the top right corner.
* Choose "Create new app."
* Enter your application name, which has to be unique. Then select your region and click "Create App."
* From your project page, click the "Settings" tab and scroll to "Config Vars."
* Enter "PORT" in the KEY input field, then enter "8000" in the VALUE input field.
* Click the "Add" button to add the Convig Vars.
* On the same page, scroll to the buildpacks section and click "Add Buildpack."
* Add the Python and node.js buildpacks, ensuring that the Python buildpack is listed above the node.js buildpack.
* Go back to the tabs at the top of the page, then select the "Deploy" tab.
* Select the Github deployment method.
* Search for your repository name, then click the "Connect" button to link your repository.
* At the bottom of that page, select deployment type: Automatic Deployment or Manual Deployment. 
* Automatic Deployment will redeploy the project to Heroku every time it is pushed to GitHun. Then wait for your project * to be deployed.

### **Forking the Repository on GitHub**
* Log in to GitHub and locate the GitHub Repository that you want to fork.
* In the upper right of the repository, click the "Fork" button.
* A copy of the repository will now be available within your repositories.
* Forking the GitHub repository makes a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository. 
* This copy of the code can be edited without affecting the original code.

## **Cloning the Repository on GitHub**
* In the upper section of the repository, click the dropdown named "Code."
* In the "Clone with HTTPS" section, copy the URL.
* Open Git Bash in your IDE of choice.
* Change the current working directory to the location you want for the cloned directory.
* Type "git clone" and paste the URL copied from GitHub.
*After pressing Enter, the clone of your repository will be created.
***
-->
 ## **Credits**
### **Honorable mentions**
The third project was very a difficult challenge, which tested my understanding of python . However the more stuff that was being introduced to the project the more simpler and effective the project became due to time restraints of the course, but nonetheless it is a good way to show what i can do, but i must credit the following people:
 * [Can Sucullu](https://github.com/cansucullu) - My Code Institute mentor who is incredible at giving me insight and suggestions on further improving my project and is a huge help to continuously support me for any sort of technical issues within the project.
* The Slack community of Code Institute for helping me with python module as it is somewhat challenging due to the deadline and questions on the module.
* Code Institute Tutors for assisting me with the technical aspects of the project i.e techical issues in regards to the coding. 
* Huge thanks to my girlfriend for the constant support.

### **General reference:**
* The project theme was inspired by the Code Institute's coding project called Love sandwiches. I have tried to change as much as possible 
* I have used W3Schools for a basic understanding and tips for python for generic basic coding references and as general encyclopedia for any code related issues or ideas.

### **Media:**
* Lucid chart for flow chart creation:- https://www.lucidchart.com/pages/ 
* Hello World used as an idea on how to create the game:- https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
* Basic format of flow chart idea and also basis of rock paper scissor game:- https://learn.adafruit.com/rock-paper-scissors-circuitpython/design
* Anscii art generator:- http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=YOU%20WIN