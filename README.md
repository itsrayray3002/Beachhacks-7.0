# Beachhacks-7.0
# StackCollab

## Inspiration
For inspiration, we wanted to tackle one of the most prevalent issues for a breakthrough into the industry for computer scientists, which is networking with other similar minds. Outside of school and hackathons, finding people to explore and grow professionally with is difficult. A brilliant back-end may never see the light of day if it's lacking a front-end.

## What it does
StackCollab is a mobile application that connects users with each other based on their skills and experiences as computer scientists. These skills are displayed in the form of tags, which each user (when creating their profile) will select up to five of. What makes SC unique, however, is that it resembles the "swipe" based style of all the popular dating apps (Tinder, Hinge, Bumble, etc.). The user is given another user's profile, and using data from LinkedIn and the tags provided by both parties, you are given the opportunity to either swipe right (implying you are interested in the other user's background and want to pursue contact) or swipe left (implying you would prefer to explore other users).

## How we built it
Our team built StackCollab by using Flask, MySQL, Python, HTML, and CSS. We used Flask to create the backend of our mobile application. This incredible framework allowed us to flexibly build a server that handled the backend and frontend at once. For the user data, we used MySQL as our database. MySQL allowed us to store all the users' data in the form of emails, names, and profile pictures from the LinkedIn OAuth 2.0 API, which is how we managed account creation. We also utilized MySQL to operate multiple tables for personal biography information. For the backend, we used the Python-based Flask framework for its raw elasticity. Python was used primarily to manage and set up our MySQL database. It also handled user authentication. For the UI, we used HTML and CSS, taking advantage of Figma to prototype and design.

## Challenges we ran into
Given that it was our first time using MySQL, Flask, and the LinkedIn API, we ran into some tedious obstacles. Some of the challenges we faced were: trying to get OAuth 2.0 to work in order to authenticate LinkedIn accounts, trying to master the MySQL database so that we can access and manage our data effectively, and trying to support SSL on a development server to run the OAuth API.

## Accomplishments that we're proud of
We are proud of how we learned to incorporate new software in MySQL and Flask, which we had never used once before. A good bulk of our time spent in the beginning of the competition was studying up on the syntax and functionalities of these applications. We were massively impressed with our team's problem-solving abilities, as we faced many problems yet persevered through them all with patience.

## What we learned
As mentioned previously, we learned how to use MySQL for databasing in order to capture and store data needed for our mobile application. We also discovered and learned Flask, which proved to be a huge benefit for us as Python is one of our strongest languages. It was our team's first time creating a project that incorporated a database, as well as our first time creating a project that incorporated both a frontend and a backend simultaneously.

## What's next for StackCollab
Our future goal is to expand on our idea and fully enhance StackCollab's potential capabilities that we are confident we can implement. There were still a few aspects of our project we didn't get to implement due to time constraints, and we aim to finish implementing them in the near future. These include GitHub and LeetCode integration, further customizability for profiles, and a matching algorithm to bring more likely partners closer together.

## Built With
- CSS
- Figma
- Flask
- HTML
- MySQL
- Python
- SQLAlchemy
- Visual Studio
