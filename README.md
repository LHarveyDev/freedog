# Freedog
Freedog is my submission for Milestone Project 4.

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [add your pages](#)
   

3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgment](#acknowledgment)

## Design & Planning:

### User Stories
- #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn how to navigate to the areas I want to use.
    2. As a First Time Visitor, I want to be able to view the facilities on offer.
    3. As a First Time Visitor, I want to find out the opening times and pricing structure.
    4. As a First Time Visitor, I want to register.
    5. As a First Time Visitor, I want to book a session and pay.
    6. As a First Time Visitor, I want to locate their social media links to see their followings on social media to determine how trusted and known they are.

- #### Returning Visitor Goals

    1. As a Returning Visitor, I want to log in and view my profile.
    2. As a Returning Visitor, I want to book a new session.
    3. As a Returning Visitor, I want to amend/cancel a previously booked session.
    4. As a Returning Visitor, I want to check if there are any social media updates.

- #### Frequent User Goals

    1. As a Frequent User, I want to log in and view my profile.
    2. As a Frequent User, I want to book a new session.
    3. As a Frequent User, I want to amend/cancel a previously booked session.
    4. As a Frequent User, I want to check if there are any social media updates.

### Wireframes
Attach wireframes in this section
### Typography
Explain font you've used for your project
### Colour Scheme
Screenshoot of the colour scheme for your project
### DataBase Diagram
Image of the database diagram for your project

## Features:
Explain your features on the website,(navigation, pages, links, forms, input fields, CRUD....)
## Technologies Used
1. [Lucidchart:](https://lucidchart.com/)
   - Lucidchart was used to create the [flowcharts](#wireframes) during the design process
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](#wireframes) during the design process
1. [dbdiagram:](https://dbdiagram.io)
   - dbdiagram was used to create the [database schema](/documentation/database_schema.png) during the design process
1. [Django:](https://www.djangoproject.com/)
   - Django was used to create the Python web framework.
1. [Djecrety:](https://djecrety.ir/)
   - Djecrety was used to create the Secret Key.
1. [Bootstrap:](https://getbootstrap.com/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [JQuery:](https://releases.jquery.com/)
   - jQuery was used in conjunction with Bootstrap to add interactivity.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
   - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Pacifico' font into the style.css file which is used for my header text.
1. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Favicon.io:](https://favicon.io/)
   - Favicon.io was used to create the icon on the web page tab.
1. [I Love IMG:](https://www.iloveimg.com/resize-image)
   - I Love IMG was used to crop and resize all images to enhance performance and increase Lighthouse scores during testing.
1. [Gitpod](https://gitpod.io)
   - Gitpod was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub was used to store the projects code after being pushed from Git.
1. [Heroku:](https://heroku.com/)
   - Heroku was used to deploy my project.
## Testing
Important part of your README!!!
### Google's Lighthouse Performance
Screenshots of certain pages and scores (mobile and desktop)
### Browser Compatibility
Check compatability with different browsers (Firefox, Edge, Chrome)
### Responsiveness
Screenshots of the responsivness, pick few devices
### Code Validation
Validate your code HTML, CSS, JS & Python - display screenshots
### Manual Testing user stories
Test all your user stories, you an create table 
User Story |  Test | Pass
--- | --- | :---:
paste here you user story | what is visible to the user and what action they should perform | &check;
- attach screenshot
### Manual Testing features
Test all your features, you can use the same approach 
| Status | feature
|:-------:|:--------|
| &check; | description
- attach screenshot
## Bugs
List of bugs and how did you fix them, you can create simple table
| Bug | Fix
|:-------:|:--------|
|   |    |
## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.
  
#### Making a Local Clone
- write steps

#### Forking the Github Repository 
- write steps

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Deploying to Heroku.
- In GitPod CLI, the root directory of the project, run: pip3 freeze --local > requirements.txt to create a requirements.txt file containing project dependencies.
- In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'. Open the Procfile. - Inside the file, check that web: python3 app.py has been added when creating the file Save the file.
- Push the 2 new files to the GitHub repository
- Login to Heroku, select Create new app, add the name for your app and choose your closest region.
- Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
- Navigate to the settings tab, click reveal config vars and input the following:


| Key | Value
|:-------:|:--------|
| DATABASE_URL  |    |
| IP  |    |
|  PORT |    |
|  SECRET_KEY   |     |

Actual Enviroment variables not disclosed for security
## Credits
List of used resources for your website (text, images, snippets of code, projects....), add links and description
## Acknowledgment
Mention people who helped you with your project(mentor, colleagues...)