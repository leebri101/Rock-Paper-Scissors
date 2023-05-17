# **Testing**
## **Table of Contents:**
* [**Testing**](#testing)
  * [**Table of Contents:**](#table-of-contents)
  * [**Manual Testing:**](#manual-testing)
    * [***Inputs:***](#inputs)
    * [***Game-Play:***](#game-play)
  * [**Bugs and Fixes**](#bugs-and-fixes)
    * [**Remaining Bugs**](#remaining-bugs)
  * [**Post Development Testing**](#post-development-testing)
    * [**Validators**](#validators)
      * [***HTML*** - https://validator.w3.org/nu/](#html---httpsvalidatorw3orgnu)
      * [***CSS*** - https://jigsaw.w3.org/css-validator/](#css---httpsjigsaww3orgcss-validator)
      * [***Python:*** - https://pep8ci.herokuapp.com/#](#python---httppep8onlinecom)

## **Manual Testing:** 
During the testing phase of the game I have used the following things through out the time.

### ***Inputs:***
I have tested all sorts of inputs with strings upon gameplay to see if there are any issues or breaks.
I have also asked my girlfriend to help with the experiment by letting her freely play the game as it is and if any misinput was in place all of them would print out a
Lastly, i have asked several people to break the app itself but it was not possible.

### ***Game Play:***
Throughout development, I was testing the game in the terminal of VScode as well as several playing multiple rounds in the Code Institute terminal template for each deployment to Heroku.
Throughout the development phase, I was manually testing the game through different IDE's like Code Institutes terminal and code anywhere.
The results where a fully functional game with minor cosmetic issues of the layout.

## **Bugs and Fixes**
1. **Intended Outcome:**
    * ***Issue Found:***
        * Loop of display of rule after each game 
    * ***Causes:*** 
        * Coding and placements to try and hide the rules after the first or second game.
    * ***Solution Found:***  
        * Instead of using inheritance, to allow for cross-functionality I opted for giving all objects a relationship with each other through belonging/possession, this was achieved by:   
            * Creating the board object as part of the Player init method. This meant that the Player possessed the board object.   
            * The Ship objects are created in the build_fleet method of the board, making a list of ships belonging to a particular player's board.
     

### **Remaining Bugs**


## **Post Development Testing**
### **Validators**

#### ***HTML*** - https://validator.w3.org/nu/

* ***Issue Found:***
    * The SVG file contained attributes written in non English language and hence the validator returned the below error: 
![HTML Validator Error](docs/screenshots/html-validator-error.jpg)

* ***Solution Used:***
    * Placing the attribute, 'lang="ca"' in the div containing the background image fixed this.

#### ***CSS*** - https://jigsaw.w3.org/css-validator/

* No issues were found as no CSS coding was used in the project
![CSS Validator](https://jigsaw.w3.org/css-validator/images/vcss)  

#### ***Python:*** - https://pep8ci.herokuapp.com/#
* Due to the downfall of PEP8 online all testing for PEP8 was done by Code institutes hand crafted version of PEP8 whichreturned no errors.
![PEP8 CI](docs/screenshots/pep8-ci.png)

[return to README.md](README.md)
