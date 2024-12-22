# The Travelling Wooden Spoon - Food Blog

## Table of Content

- [About the project](#about-the-project)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features left to implement](#features-left-to-implement)
- [Testing](#testing)
  - [Initial Checks](#initial-checks)
  - [Bugs](#bugs)
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



## Quiz structure

        The quiz consists of three sections:

- Vocabulary Section (15 questions)
    - The questions test synonyms, antonyms, and general vocabulary knowledge.
    - Example: "What is the synonym of 'happy'?" sad -  joyful - angry - tired

- Grammar Section (15 questions)
    - The questions test the understanding of tenses, word order, modal verbs, adjectives vs. adverbs, comparatives, and pronouns.
    - Example: "Which sentence uses the modal verb correctly?" He ran quick. - He ran quickly. - He ran more quick. - He ran the most quick.

- Text Comprehension Section (1 passage with 5 questions)
    - The question test comprehension of a text about global warming from National Geographic Education
    - Example: "What is global warming, and what has caused its significant increase in the past hundred years?"



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


## Code Quality and Version Control

- PEP8 Compliance: The code has been checked against PEP8 standards using PEP8 online to ensure consistency and readability. No PEP8 errors were found during the validation process.

- Linting: `Pylint` was used to check for style violations, including line length. I corrected detected violations by installing and running `Black`.

- Comments: Functions and classes include docstrings to describe their purpose, inputs, and outputs.

- Version control is managed using Git and GitHub, with a focus on maintaining a clean and organized history. Regular commits follow a consistent format and describe the features implemented and/or reasons for changes made to existing features.


## Testing


### Initial Checks

To catch and fix potential bugs early I tested the functionality of the code thoroughly after I implmeneted a new function using print statements in the relevant places and checked the output matched the results I expected before moving on.

I confirmed that all errors caused by user action are handeled the expected way and the corresponding feedback messages are given to the user by entering invalid inputs:

- strings where numbers were expected
- out of bounds inputs
- inputs not matching the expected format

I tested both, my local terminal and the Code Institute Heroku terminal.

I reviewed my Google Sheets to ensure the input is free of typos and checked that the value for `Correct Answer` matches the corresponding index in the Python code.

I used the raise keyword to provoke errors to check that system related errors such as data not getting pushed to the results sheet and data not getting send to the ZAP are caught and handled correctly.

| Feature Tested                | Expected Outcome                                           | Actual Outcome                                             |
|-------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| User data input (name)        | User is presented with promt to enter their name           | Prompt displayed correctly                                 |
| Error Handling (Invalid Input)| Input > 20 characters not accepted, error message displayed| Message displayed correctly: Name should not exceed 20     |
|                               |                                                            | characters. Please try again.                              |
| User data input (email)       | User is presented with promt to enter their name           | Prompt displayed correctly                                 |
| Error Handling (Invalid Input)| Incorrect email format not acceppted, error message        | Message displayed correctly: Invalid email format. The     |
|                               | displayed.                                                 | format should be name@email.com                            |
| Sample Question Display       | User is presented with a sample question after             | Sample question displayed correctly                        |
| Error Handling (Invalid Input)| User receives error message when entering any other        | Error message displayed as expected: Invalid input. Please |
|                               | character than a number                                    | enter a number between 1 and 4                             |
| Import Questions from Sheets  | Questions loaded successfully without errors               | Questions displayed correctly                              |
| Error Handling (Invalid Input)| User receives error message when entering any other        | Error message displayed as expected: Invalid input. Please |
| when asnwering questions      | character than a number                                    | enter a number between 1 and 4                             |
| Scoring System                | Points are correctly calculated and displayed              | Scoring system worked accurately and displayed correct     |
|                               |                                                            | points                                                     |
| CEFR Level Determination      | User is assigned the correct CEFR level based on score     | CEFR level was accurately determined and matched expected  |
|                               |                                                            | results                                                    |
| Result Recording              | User results are saved to Google Sheets and JSON file      | Results recorded successfully in both Sheets and JSON file |
|                               |                                                            | Success message corretly displayed                         |
| Email Dispatch via Zapier     | User receives email with quiz results                      | Email sent successfully, user received results in their    |
|                               |                                                            | inbox                                                      |
| Error Handling (dispatch)     | Appropriate error message displayed                        | Correct error message displayed:                           |
| to Zapier failed              |                                                            | Failed to send results. Status code:                       |
|                               |                                                            | Error sending data to Z.:                                  |


### Bugs

- When rewriting the code after deciding to use Google Sheets instead of a JSON file for a better future maintainability I ran into the issue that the score did not update although the question was answered correctly. With combination of using the raise keyword and debugging statements I was able to narrow down the problem to a value mismatch between Google Sheets and the Python code. The fucntions ask_question() and comprehension_quiz() were expecting an integer matching the user input while I had saved 'A', 'B', 'C', 'D' as value for 'Correct answer'. I fixed this by updating the value for 'Correct answer' to integers for the vocabulary and grammar sheet and implmeneting the ord() method into comprehension_quiz due to the different structure of the sheet (non-unique headings).

- When fixing the error of the scores not updating I briefly forgot that lists are zero-indexed while the sheets in Google Sheets start with '1' which resulted in the enumeration being off for the vocab_sheet and the grammar_sheet, starting with '1.' for the question instead of '1.' for the first answer option. I fixed this by reviewing the structure of my sheets and adjusting the indices accordingly.

- When testing the app after implementing send_to_zapier_webhook() I noticed that within the mock terminal the error message "Error sending data to Z.: No such file or directory: 'zapier_webhook_url.txt'" was printed to the terminal although the results_sheet was updated correctly and I received the results email from Zapier. After confirming the code itself to be correct using debugging statements I checked the relevant part of the code in PEP8online and located an incorrect indentation plus a trailing whitespace. Correcting these resolved the error.


### Remaining Bugs:

There are no bugs remaining.


### Validator Testing:


### Automated Testing

- PEP8
    - installed and ran .flake8 to get a list of linter violations
    - installed an ran autopep8
  => all issues but one issue (too many characters in line) fixed => fixing that error led to function stopping to work 

- Automated Testing in Django:
  -> created a test folder for each app and a test- file for each .py-file

  blog app:
  


## Technology Stack
   
  - Backend: Python, Django
  - Frontend: HTML, CSS, Bootstrap, Javascript
  - Database: PostgreSQL (Cloud-hosted on Heroku)
  - Media Management: Cloudinary
  - Rich Text Editor: Django Summernote
  - Authentication: Django AllAuth


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
