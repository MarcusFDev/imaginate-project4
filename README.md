# Imaginate.

[Imaginate](https://imaginate-project4-marcusf-ce5676c7b6a0.herokuapp.com). Stories for readers, fueled by the power of imagination.  With a modern user-driven design, Imaginate aims to be the new core place to write, store and share a individuals imagination online.

![Site on All Devices](static/images/site-all-devices.webp)
---

# Table of Contents

1. [UX](#ux)

   - [Goals](#goals)
     - [Visitor Goals](#visitor-goals)
     - [Business Goals](#business-goals)
     - [User Stories](#user-stories)
   - [Visual Design](#visual-design)

2. [Features](#features)

    - 

3. [Project Notes](#project-notes)

    - 

4. [Technology Used](#technology-used)

   - [Languages](#languages)
   - [Libraries](#libraries)
   - [Platforms](#platforms)
   - [Other Tools](#other-tools)

5. [Testing](#testing)

   - [Methods](#methods)
     - [Validation](#validation)
     - [General Testing](#general-testing)
   - [Bugs](#bugs)
     - [Known Bugs](#known-bugs)
     - [Fixed Bugs](#fixed-bugs)

6. [Deployment](#deployment)

    - [Github Deployment](#github-deployment)
        - [Github Preperation](#github-preparation)
        - [Github Instructions](#github-instructions)


7. [Credits and Contact](#credits-and-contact)

    - [Credits](#credits)
    - [Contact](#contact)

---

# UX

## Goals

### Visitor Goals

The target audience for Imaginate are:

- Users who like to write stories.
- Users that want a easy to navigate, modern and user friendly story site. 
- Users that want a place to share their stories online.
- Users who want to read stories and give feedback.
- Users that want to be part of a community.

The user goals are:

- To register an account with the site.
- To login to their account on the site. 
- To post their stories online.
- To have the ability to private their stories.
- To have the ability to visit other's profile page.
- To build a portfolio of their stories on their profile page.
- To have the power to delete their story.
- To have the ability to access other public stories.
- To react to the story with a up vote.
- To comment on a users story.
- To edit and delete their comments.

Imaginate fills these goals by:

- Providing a way to Create & Login to a site account.
- Providing a story creation page to write a story.
- Providing a story private button to toggle public/private on owned stories.
- Providing a User Profile page for every user. With the ability to delete all stories, all comments and account.
- Providing a link to users profile page via author names on stories & comments.
- Providing a Library page containing a list of public stories that can be filtered & searched.
- Providing a Comment section under every story to comment.
- Providing buttons to delete and edit comments belonging to the logged in user.
- Providing upvote button on story page to upvote a story.
- Providing a My Stories page to show a list of logged in user's stories.

### Business Goals

The Business Goals for Imaginate are:

- Obtain a userbase of individuals who like to read & write stories.
- Maintain a free and limitless platform for all users.
- Become a community recognised name in the online writer & reader society.

### User Stories

1. As a returning reader I want to be able to create an account on the site so I can always view new stories.
2. As a writer I want to be easily able to locate all my stories all in one place.
3. As a clumsey writer I really need to be able to edit and even delete my stories in case I make a mistake.
4. As a community driven person I would love there to be a way I can comment on & upvote stories so I can be part of the community.
5. As a writer I would feel safe if I could private my work.

More user Stories can be found [here](https://github.com/users/MarcusFDev/projects/4/views/1).

## Visual Design


---
# Features

## Fixtures

Imaginate is a story focussed on writing & reading stories. It was important to ensure that the full showcase of the sites features could be visualized so story data was required to fill the `Story(models.Model):` database table. For the sake of showcasing functionality & maintaining time management for the project scope; a story fixture was used to append data to the database. [ChatGPT](https://chatgpt.com) was utilized with my fixture structure to generate story data quickly so that the database could be filled faster than manual story creation, for the sake of not wasting development time manually & individually adding every story entry.

Fixture file used can be found here: [Story Fixture](https://mystb.in/bc5539c9ffa90a5d99).


## Feature Ideas

Due to time constraints and the adapting scope of the project's first iteration deadline, the following feature ideas were not realized in this version. They are intended to released in the future during a new project development cycle.

### Project Content

- Edit Stories. provide a button to edit stories on the site and change story specific settings.
- Story List visiting. Ability to access other User's story list.
- Profile Avatar changing. Ability for users to change Avatars. (Given both premade selectable Avatars & the availability to upload their own.)
- News Feed that site Admins/Moderators can post update blogs.
- Homepage story showcase. Weekly changing highlight reel of most recent upvoted stories to encourage continuous strive for improvement in their works and appreciation for using the site. Alongside giving light to must-reads!
- Story tags. Allow writers to use predefined tags to help categorize their stories and readers the ability to filter tags to find story genres.
- Policy Page. A list of site policies informing users to follow so enforcement action can be handled.
- Story Drafts. Allow stories to be saved as drafts before publishing.
- Follow User Accounts. Ability to follow other user accounts & recieve notications.

And so much more before site can reach a Public Release date.

### Project Design

- More Dynamic page scroll animations. Such as a open book underneath the Home Page titles.
- Story/Library lists designed as a bookcase with each story being deisgned to represent a book.
- Story pages themselves styled with the content looking like a open book.

---

# Project Notes


---

# Technology Used

## Languages

- [Python](https://docs.python.org/3/)
    - Complete Project Functionality.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Adds interactivity and make dynamic web content.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Structure and layout of web pages.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - Styling for web pages.

## Frameworks

- [Django](https://www.djangoproject.com/)
    - A high-level Python web framework that encourages rapid development and clean, pragmatic design. It was crucial for building the web application's backend, handling routing, database interactions, and user authentication.

## Databases

- [PostgreSQL](https://www.postgresql.org/)
    - An advanced, open-source relational database system known for its reliability, feature robustness, and performance. Used as the database for storing application data.

## Libraries

- [Bootstrap V5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
    - Widely used CSS library. Used throughout project to aid in page styling and limit the requirement of a lot of custom css & script code. 
- [JQuery V3.6](https://jquery.com)
    - Commonly used as a alternative and often more efficent than vanilla JavaScript functionality.
- [Re](https://docs.python.org/3/library/re.html)
    - Used with `clean()` in the `accounts/forms.py` file to handle special characters within account Registration & Login functionalities.
- [Summernote](https://summernote.org/)
    - A simple WYSIWYG editor that enables users to easily format text within the project, used for the profile description & story creation.
- [Gunicorn](https://gunicorn.org/)
    - A Python WSGI HTTP server for UNIX that serves the Django application in production, ensuring efficient handling of incoming requests.
- [WhiteNoise](http://whitenoise.evans.io/en/stable/)
    - A package that allows Django application to serve its own static files eliminating the need for a separate static file server.
- [Pillow](https://python-pillow.org/)
    - A Python Imaging Library that adds image processing capabilities to the application, allowing for tasks such as saving image files.

## Platforms

- [Github](https://github.com/MarcusFDev/imaginate-project4)
    - Storing code remotely.
- [Gitpod](https://www.gitpod.io)
    - IDE for project creation and development.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used for project deployment and examination purposes.

## Other Tools

- [CI Python Linter](https://pep8ci.herokuapp.com)
    - Code Institute Python linter was used to validate the Python code.
- [Coolers](https://coolors.co)
    - Tool to create palette image of color schema.
- [Am I Responsive?](https://ui.dev/amiresponsive)
    - Tool used to create multiple device image.
- [FreeConvert](https://www.freeconvert.com)
    - Tool used to change images to .webp file types.
- [W3C HTML5 Validator](https://validator.w3.org/nu/#textarea)
    - Tool to validate HTML5 files meet website standards.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Tool to validate CSS files to meet website standards.
- [ChatGPT](https://chatgpt.com)
    - AI Text Generator to automatically create unique fixture story entries.

# Testing

## Methods

### Validation

- HTML pages all have been validated with the [W3C HTML5 Validator](https://validator.w3.org/nu/#textarea) tool. Errors that do appear from the validator have been caused by Django templating. 

![HTML Validator image](static/images/homepagehtmlvalid.webp)

- All CSS code has been validated with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) tool.

![CSS Validator image](static/images/css-validated.webp)

- All Python code has been validated with the [CI Python Linter](https://pep8ci.herokuapp.com) tool. Below are the core functionality Python files validated. All others have been validated and resulted in zero errors.

`accounts/view.py` Validation:

![Accounts View Validator image](static/images/accounts-views.webp)

`accounts/forms.py` Validation:

![Accounts Forms Validator image](static/images/accounts-forms.webp)

`stories/view.py` Validation:

![Stories View Validator image](static/images/stories-views.webp)

`stories/forms.py` Validation:

![Stories Forms Validator image](static/images/stories-forms.webp)

- Accessibility has been tested using developer tools utilizing lighthouse.

Mobile Lighthouse Result using Google Chrome (Average Result)

![Lighthouse Result Mobile](static/images/site-lighthouse-mobile.webp)

Desktop Lighthouse Result Google Chrome (Average Result)

![Lighthouse Result Desktop](static/images/site-all-devices-desktop.webp)

### General Testing

- After every iteration of code, everything was promptly manually tested to check for unexpected errors.
- Account Register & Login error handling works. (Bootstrap Modals close on page refresh however.)
- Newsletter signup correctly stores data to the database model for use.
- All links correctly work on all devices.
- Data correctly updates to all database model tables.
- Alerts implemented work correctly.
- Pages dynamically update with changes using JQuery and Ajax as intended.
- Story upvoting, deleting & creating work as intended.
- Comment upvoting, editing, deleting and creating work as intended.

## Bugs

### Known Bugs

- Story Upvote `<div>` not updating style upon AJAX button click. Page Refresh still required for styles to take effect.
- Account Login & Register modals close & page refresh upon failed form submission.
- If error in form is detected from either Login or Register, error styling is applied to other Modal, Register or Login respectively.
- Edited to empty About description does not append default empty message on profile page.
- Pages occasionally load slower than normal on higher latency due to amount of event listeners on each page load.
- Error messages handled poorly & inconsistently from form errors causing some to not correctly appear.


### Fixed Bugs

- (TEMPORARY FIX): Logout modal not correctly working in seperate modal.html file. Moved directly into `base.html` for functionality.
- Fix: Multiple formatting errors regarding `<div>` elements inside other elements incorrectly such as `<h1>, <span> & <ul>` elements.
- Fix: A error occured over a model change in the UserProfile model. Entire database was wiped clean with renewed model structure.
- Fix: LoginForm not working as intended, required large changes structurally. Commit message located [here](https://github.com/MarcusFDev/imaginate-project4/commit/0aab44fdc87818fc155355e9a36254e891a4d008)
 

# Deployment

[Imaginate](https://imaginate-project4-marcusf-ce5676c7b6a0.herokuapp.com) is a both frontend & backend project utilizing the Django framework to build a expandable and modern user-driven website. 

To experience the project [Heroku](https://dashboard.heroku.com/apps) was used to host Imaginate via their website platform. 

A Code Institute [template](https://github.com/Code-Institute-Org/ci-full-template) was used as the building block to bring Imaginate to life.

To view my Heroku deployment of Imaginate please follow this [link](https://imaginate-project4-marcusf-ce5676c7b6a0.herokuapp.com).

## Github Deployment

### Github Preparation

Requirements:

- You need a GitHub account.
- You need a IDE such as [GitPod](https://gitpod.io).
- You need a Google account.

### Github Instructions

1. 

## Credits and Contact

### Credits

IDE Template:

- This Code Institute [template](https://github.com/Code-Institute-Org/ci-full-template) was used to set up the IDE environment for the Imaginate project.

### Contact

Please feel free to reach out if you have any questions. Contact me via my email at marcusf.dev@gmail.com