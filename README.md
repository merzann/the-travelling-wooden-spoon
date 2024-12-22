# The Travelling Wooden Spoon - Food Blog

## Table of Content

- [About the project](#about-the-project)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features left to implement](#features-left-to-implement)
- [Testing](#testing)
  - [Initial Checks](#initial-checks)
  - [Page performance](#page-performance)
  - [Bugs and Resolutions](#bugs-and-resolutions)
  - [Validator Testing](#validator-testing)
  - [Automated Testing](#automated-testing)
-  [Technology Stack](#technology-stack)
-  [Deployment](#deployment)
-  [Usage](#usage)
-  [Contribution](#contribution)
- [Acknowledgement](#acknowledgement)
  - [Content](#content)
  - [Media](#media)
- [Author](#author)
- [License](#license)


## Overview
The Travelling Wooden Spoon is a dynamic blog application focused on recipes, weekly cooking tips, and engaging user interactions. Users can browse recipes, view blog posts, create an account in order doe rate recipes orleave comments, read weekly tips,und sign up for a weekly newsletter to stay up to date. 

The application supports a rich feature set, including user authentication, newsletter subscriptions, and automated blog updates when new recipes are published.

Admins can manage the content through the Django Admin Panel, utilizing tools like Summernote for styling their posts making them truly individual. They will love the history panel, that allows them to keep track of their post history, the scheduling section for creating and queueing posts in advance, then schedule them for future release and the option to export an up-to-date list of subscribern in csv-format for mailings.

The Travelling Wooden Spoon is a feature-rich platform for recipe enthusiasts. Its robust backend ensures seamless content management, while the frontend delivers a user-friendly experience. With the bugs resolved and planned enhancements, the project is well-positioned for growth and engagement.

The live link can be found here - https://the-travelling-wooden-spoon-499c1c443de1.herokuapp.com/

![Responsive Mockup](readme_media/mockup.png)



## 

Hero Section on Mobile
![Hero Section page on Mobile](readme_media/Homepage_mobilde_hero.png)

Hero Section on Desktop
![Hero Section on Desktop](readme_media/Homepage_Desktop_hero.png)

- 

## Scoring

- Vocabulary Section: 
    - Each correct answer scores 1 point (maximum 15 points).
- Grammar Section: 
    - Each correct answer scores 1 point (maximum 15 points).
- Text Comprehension Section: 
    - Each correct answer scores 4 points (maximum 20 points).



## CEFR Levels

The total score determines the user's CEFR level:

- A1 - Beginner: 0-10 points
- A2 - Elementary: 11-20 points
- B1 - Lower Intermediate: 21-30 points
- B2 - Upper Intermediate: 31-40 points
- C1 - Advanced: 41-45 points
- C2 - Proficient: 46-50 points



## How the English Level Assessment Quiz works

1. The user starts the quiz by clicking "RUN PROGRAM"

2. The command interface greets the user with a welcome message and a short information about the assessment quiz, how to answer the questions and an information that they will receive an email with the results after completing the quiz.

3. Then the user is prompted to enter their name and email address. 

4. The next step is to answer a sample question which demonstrates to the user that they need to input the number (1-4) corresponding to the answer option chosen. 

5. The test loads and the user is presented the first question. There are 4 options given to answer the question with one option being correct.
    A new question is displyed after the user has answered the previous one.
    'Current score' displays the score achieved up to this point to the user.

6. When the user has completed the quiz they receive a message "Quiz complete!", their scores, sorted by category, and their overall CEFR.

7. Again the user is informed that they will also receive their results via email. The email will be sent automatically after a few minutes through a ZAP.


## Features

### Existing Features

## Home page

Hero Section on Mobile
![Hero Section page on Mobile](readme_media/Homepage_mobilde_hero.png)

Hero Section on Desktop
![Hero Section on Desktop](readme_media/Homepage_Desktop_hero.png)

### Import questions from Google Sheets

        The application requires 4 worksheets:

#### Vocabulary sheet/Grammar sheet
- The vocabulary sheet is structured is follows:
    - column 1: questions
    - column 2-4: answer options A-D
    - column 5: correct answer

![Vocabulary Sheet](./readme_media/vocab_sheet.png)
![Grammar Sheet](./readme_media/grammar_sheet.png)

#### Comprehension Sheet
- The comprehension sheet is structured as follows:
    - column 1: reading text
    - column 2: questions
    - cloumn 3-6: answer options A-D
    - column 7: correct answer

![Comprehension Sheet](./readme_media/comprehension_sheet.png)

#### Results sheet
- The results sheet is structured as follows:
    - column 1: Name
    - column 2: Email
    - cloumn 3: Vocabulary score
    - column 4: Grammar score
    - column 5: Comprehension score
    - column 6: CEFR level

![Results Sheet](./readme_media/results_sheet.png)


### Sample Question

The user has to answer a sample question after entering their details. The sample question demomstrates to the user how the quiz works and the way how they have to enter their answer. The user receives immediate feedback when they enter any character other then a number.

![Sample Question](./readme_media/error_handling_sample_question.png)


### Administer quiz via command-line interface

The assessment quiz runs in the Code-Institute mockup terminal in Heroku.

![Administer Quiz](readme_media/initial_view.png)

The questions are staged when the assessment quiz has finished loading. 
The questions are displayed one question after the other, the new question only after the user has answered the previous one and hit enter.

![Questions Vocabulary](./readme_media/sample_question_quiz.png)
![Questions Grammar](./readme_media/grammar_questions.png)
![Text Comprehension](./readme_media/text_comprehension.png)
    

### Calculate and determine CEFR level

While the user completes the quiz the score is updated for each question answered correctly: +1 in the vocabulary and grammar section, +4 in the section for text comprehension. 

- `Current score` displays the points achieved up to this point to the user. A final interim score is calcualted and displayed to the user when a section is completed.
- Upon completing the quiz the user is presented with their final score, their score for each section and their current CEFR level.

![Final Score/CEFR Level](./readme_media/final_score.png)


### Record and export results

The result gets recorded in the results_sheet and results.json

![Final Score/CEFR Level Sheet](./readme_media/resultsSheet.png)
![Final Score/CEFR Level JSON](./readme_media/result_json.png)

The app then sends the results to the ZAP and the user receives an email with their results for their records and a course recommendation.

![Email Zap](./readme_media/email_zap.png)
![Email Zap](./readme_media/email_zap(2).png)


### Robust and user-friendly error handling

The error handling is robust and user-friendly, accounting for common errors caused by user action such as out of the bound or incorrect character input as well as for system issues, e.g. 
- data not correctly pulled or pushed from and to external sheets
- data not transmitted correctly to trigger the automated email the user receives after completing the test.


#### When the user inputs their name and email address:
- The system allows a maximum of 20 characters for the name. Should the user enter more characters they will receive a message informing them that the max. length allowed is 20 characters.

- A feedback message is provided should the email entered not be in the correct format xxx@gmail.com

![Error Handling user input: details](./readme_media/error_handling_user_input.png)


#### When the user enters any other character than a number as input to answer a question:
- Immediate feedback is provided when the user types in a letter or any other character which is not a number.

![Error Handling user input: quiz answer](./readme_media/error_handling_sample_question.png)


#### When a system push or pull request succeeds/fails:

![Error Handling user input: system](./readme_media/system_error.png)


### Features left to implement

- a freestyle section to test the students writing skills and get a better inside on their actual ability to use the language
- randomizing of the questions within the sections to prevent cheating by restarting the test mutiple times or for the purpose of using the test for learning new language items



# Testing

### Initial Checks

To catch and be able to reverse an action before being forced to wipe the database I made sure to strictly following the concept of model first and test the functionality with print statements to the terminal before creating the template accordingling.

I confirmed that all errors caused by user action are handeled the expected way and the corresponding feedback messages are given to the user by entering invalid inputs:

- Submit button hit in forms before filling out all fields
- inputs not matching the expected format
- attempting to submit a comment twice, either by error or intentionally
- signing up for the newsletter twice, either by error or intentionally
- trying to submit more than one rating
- attempting to submit a rating or commment when not signed in

I had content reviewed by test users so I catch and fix typos and/or grammar errors.

I thoroughly tested all buttons, carousel and scroll-down-icon on both mobile devices, tablets and desktop.

Together with my test users I reviewed the content on different devices to ensure all of the content is displayed as expected.


## Page Performance

  ### Mobile

Home Pagew
![Home page](readme_media/p_mobile_home.png)

Category Page
![Category page](readme_media/p_mobile_category.png)

Recipe Detail Page
![Recipe detail page](readme_media/p_mobile_recipe_detail.png)

About Page
![About page](readme_media/p_mobile_about.png)

Weekly Tip
![Weekly tip page](readme_media/p_mobile_weekly_tip.png)

Page for Login
Logout / Sign-Up
![Login_Logout_SignUp](readme_media/p_mobile_login_logout_signup.png)



  ### Desktop

Home Page
![Home page](readme_media/p_desktop_home.png)

Category Page
![Category page](readme_media/p_desktop_category.png)

Recipe Detail Page
![Recipe detail page](readme_media/p_desktop_recipe_detail.png)

About Page
![About page](readme_media/p_desktop_about.png)

Weekly Tip
![Weekly tip page](readme_media/p_desktop_weekly_tip.png)

Page for Login
Logout / Sign-Up
![Login_Logout_SignUp](readme_media/p_desktop_login_logout_signup.png)



                                                                           
| Feature Tested                   | Expected Outcome                                                  | Error Fall-safes or Expected Error Handling      |
|----------------------------------|-------------------------------------------------------------------|--------------------------------------------------|
| Navbar Home Button               | Navigates to the homepage                                         | Page loads with no errors                        |
| Navbar Recipes Dropdown          | Displays a dropdown menu of recipe categories                     |                                                  |
|                                  | when hovered over                                                 | Dropdown menu correctly lists categories; no     |
|                                  |                                                                   | errors are displayed                             |
| Navbar Recipes Dropdown Selection| Navigates to the selected category page                           | Redirects to category page or shows "No recipes  |
|                                  |                                                                   | found" message                                   |
| Navbar About Button              | Navigates to the About page                                       | Page loads with the correct About content; no    |
|                                  |                                                                   | errors displayed                                 |
| Navbar Weekly Tip Button         | Navigates to the Weekly Tip page                                  | Weekly Tip page loads correctly with tip content |  
|                                  |                                                                   | or fallback tip                                  |
| Navbar Login Button              | Navigates to the Login page for unauthenticated users             | Login form loads correctly, error message for    |
|                                  |                                                                   | invalid credentials                              |
| Navbar Register Button           | Navigates to the Signup page                                      | Signup page loads correctly, shows validation    |
|                                  |                                                                   | errors if invalid                                |
| Navbar Logout Button             | Logs out authenticated user                                       | User is redirected to the homepage               |
|                                  |                                                                   |                                                  |
| Scroll down button               | Navigates to next section, bumbs up and down periodically to let  | button is displyed at all time even if click     |
|                                  | the user know there is content below the hero image               | functionality should fail                        |
|                                  |                                                                   |                                                  |  
| Social Media Links               | Opens respective social media page in a new tab                   | Includes`target="_blank"' element; ensures lin   |
|                                  |                                                                   | opens in a new tab                               |
| Read More button                 | Navigates to the recipe detail page with full recipe content      | If recipe not found, 404 error is displayed      |
|                                  |                                                                   |                                                  |
| Hover over Navbar Dropdown       | Dropdown menu expands with categories                             | Handles hover functionality without JavaScript   |
|                                  |                                                                   | errors                                           |
| Static Asset Loading             | Loads all CSS, JS, and fonts correctly                            | Error message or console log if assets fail to   |
|                                  |                                                                   | load                                             |
|                                  |                                                                   |                                                  |
| SEO and Accessibility Tags       | Provides meaningful aria labels and meta tags                     | Validates no missing or invalid aria-label or    |
|                                  |                                                                   | meta-tag warnings                                |



### Bugs and Resolutions


1. **TemplateDoesNotExist Error**
    - **Issue:** Template paths were not correctly defined, causing Django to throw errors.
    - **Solution:** Adjusted the app's TEMPLATES setting and ensured proper folder structures.


2. **BlogPost and Recipe Description Compatibility**
    - **Issue:** Recipes created before fixing integration issue of Summernote didn't display descriptions properly afterwards
    - **Solution:** Backfilled missing excerpt and description data using Django Shell.


3. **Comment Deletion by Users**
    - **Issue:** When reviewing the User Stories created I noticed that I had forgotten to add a Delete-button resulting in Users being unable to delete their own comments.
    - **Solution:** Added delete_comment view and corresponding button in the recipe_detail.html.

    
4. **Truncated Text in Templates**
    - **Issue:** Long descriptions cluttered the index.html and category.html due to same field being used in recipe_detail.html
    - **Solution:** Tried to add methods (truncated_description, truncated_snippet) to models and updated templates. When that kept causing cascading errors I added a new field named "excerpt" to the recipe model which now gives the user the option to additionally add an attention-catching hook for displaying the recipe on home page and category page.


5. **Missing Admin Filters**
    - **Issue:** Dynamic Summernote integration removed admin filters.
    - **Solution:** Reinstated filters in admin.py for key models.


6. **Weekly Tip Page Newsletter**
    - **Issue:** Newsletter functionality was missing.
    - **Solution:** Implemented a newsletter form, added validation, and integrated backend management.


7. **Blog Detail View**
    - **Issue:** blog_detail needed to reuse recipe_detail.html toavoid having to create another template after amending the Blogpost model to fix the problem of new posts added not automatically being displayed in Latest-Blogpost-Section on Homepage
    - **Solution:** Updated the blog_detail view to pass relevant data dynamically.



### Remaining Bugs:

-> no known bugs remaining; all parts of the application worked as expected during manual testing


### Validator Testing:

W3C CSS: no errors detected (no option to create URL link to paste here)
W3C HTML: multiple errros returned across all files caused by Django templating language
JSHint: no errors detected

### Automated Testing

- PEP8
    - installed and ran .flake8 to get a list of linter violations
    - installed an ran autopep8
  => all issues but one issue (too many characters in line) fixed => fixing that error led to function stopping to work 

- Automated Testing in Django:
  -> created a test folder for each app and a test- file for each .py-file

  blog app:
  -> 1 import error (redirect missing) fixed
  -> one error in calculating average rating fixed -> float() added for a more precise result
  -> repeated error in test_signal.py due to test environmentv not able to reproduce signal

  froms.py
  -> no errors detected

  about.py:
  -> repeated error caused by link to cloudinary due to sample picture stored locally -> test function in test_about_page_context refactored _. error remains

  weekly_tips.py: 
  -> repeated error that file could not be detected

  troubleshooting; debugging with 
  -> python manage.py test weekly_tip --verbosity 
  -> python -m unittest discover weekly_tip/tests
  -> python manage.py test weekly_tip.tests.test_models
  -> ran python manage.py test --verbosity 3 --failfast -> grabbed all files and returned only the errors known and described above


## Technology Stack
   
  - Backend: Python, Django
  - Frontend: HTML, CSS, Bootstrap, Javascript
  - Database: PostgreSQL (Cloud-hosted on Heroku)
  - Media Management: Cloudinary
  - Rich Text Editor: Django Summernote
  - Authentication: Django AllAuth



## Code Quality and Version Control

- PEP8 Compliance: The code has been checked against PEP8 standards using .Flake and autopep8

- Comments: Functions and classes include docstrings to describe their purpose, inputs, and outputs.

- Version control is managed using Git and GitHub, with a focus on maintaining a clean and organized history. Regular commits follow a consistent format and describe the features implemented and/or reasons for changes made to existing features.



## Deployment
    
This project was deployed through Heroku

Steps for deployement
- **Fork or Clone the repository:**

   git clone https://github.com/merzann/the-travelling-wooden-spoon
   cd the-travelling-wooden-spoon

- Install dependencies - 'pip install -r requirements.txt'
    - `pip3 install django~=4.2.1`
    - `pip3 install gunicorn~=20.1`
    - `pip3 install dj-database-url~=0.5 psycopg2~=2.9`
    - `pip3 install whitenoise~=6.5.0`
    - `pip3 install django-summernote~=0.8.20.0` 
    - `pip3 install django-allauth~=0.57.0` 
    - `pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7`
    - `pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15`

- Set up environment variables: create a .env - file
  DATABASE_URL=<your-database-url>
  CLOUDINARY_URL=<your-cloudinary-url>
  SECRET_KEY=<your-secret-key>

- Run migrations after adding or updating models
  python3 manage.py makemigrations
  python3 manage.py migrate

- Run the collectstatic command in the terminal to collect the static files into a staticfiles
  directory:
  python3 manage.py collectstatic
- Check the Python Version you have installed in your Workspace: python3 -V
- Create a runtime.txt file and add the Python Version you have installed
  - a list of supported Python Versions can be found here: 
    https://devcenter.heroku.com/articles/python-support

- create a PPROCFILE: echo web: python manage.py > Procfile
- set DEBUG to "False"

- Create an account with Heroku or sign up for an account
- Create a new Heroku App
- Enter Config Vars in settings
  DATABASE_URL: <your-database-url>
  SECRET_KEY : <your-secret-key>
- Link the Heroku App to the repository
- Click on DEPLOY

The live link can be found here - https://the-travelling-wooden-spoon-499c1c443de1.herokuapp.com/


## Usage

- Ensure you have Python installed. This application requires `Python 3.6` or later.
- clone the repository as explained above
- Install the dependencies: `pip install -r requirements.txt`
- create an env. - file and set up the envirnoment variables (see above)
- run migrations
- order to access the Admin Panel you need to create a superuser: 
  python3 manage.py createsuperuser

  Gitpod will show a login requets:
  Email: enter your Gitpod/Github email
  Password: enter your password

- Start the develoment server: python manage.py runserver



## Contributing

- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -am 'Add new feature`)
- Push to the branch (`git push origin feature-branch`)
- Create a new Pull Request



## Acknowledgement

### Content
- The template used for building this project was provided by Code Institute on Github for student projects [p3-template](https://github.com/Code-Institute-Org/p3-template)
- A big thank you to the Code Institute Tutor team for continuous support and endless patience with a coding Newby missing the forest for the trees.
- I also would like to thank the Stack Overflow community for pointing me in the right direction whenever I was stuck and turning in circles in the middle of the night
- As with all my projects I would like to extend a special thanks to my team of critical test users who helped me pinpoint and fix bugs and typos I had missed

### Media
- images:  Freepik https://www.freepik.com/free-photos-vectors
- recipes: "Das große Pasta Buch", Parragon Books ltd., 
  "Die schoensten Liebesrezepte" Ruth Johnson
- most of the pictures belong to me


## Author

- [merzann](https://github.com/merzann)


## License
[![MIT License](https://img.shields.io/badge/License%20-%20MIT-olivgreen)](LICENSE.md)
