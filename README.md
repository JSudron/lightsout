# LIGHTS OUT! - Project Three: Data Centric Development

![Screenshot](https://github.com/JSudron/lightsout/blob/master/images/mockups/Responsive%20Mockup.png?raw=true)

A live demo can be found [here](https://lightsout-joe.herokuapp.com/).

## Introduction - Project Purpose

For this project I was tasked with creating a CRUD application. This application is a database of non-fictional spooky stories with the long-term goal of creating a lot of traffic to the site which would eventually allow
for advertising to boost revenue, an example is the fictional spooky stories on creepypasta.com. This application will allow users to CREATE stories to add to the site, they can also READ through the exisiting stories 
available, UPDATE any of the stories & also DELETE stories if they wish to. All changes are made on the client side which then feeds through to the database on the backend.

## UX
 
### Goals

To allow users to share their spooky experiences & read about other people's experiences.

#### Target Audience

- Users whom speak English as currently this is the only language catered for.
- Users looking to share their spooky experiences with others.
- Users looking to read spooky non-fictional stories.

#### Goals

- Have a fully proficient & intuitive website.
- Have full CRUD functionality.

### User Stories

#### UX Designer

- Provide a website which is attractive, yet can easily be modified if adding further functionality.
- Ensure the CRUD functionality of the website provides the results required by the user.

#### Users

- Have a platform to share their own spooky experinces with other users.
- Be able to edit any stories should changes need to be made.
- Allow for deletetion of stories if users feel the story should be deleted.
- Provide users with a way to read and enjoy other people's spooky stories.
- Navigate the site easily.

### Design

#### Colours

- #1E1E24 Raisin Black
- #92140C Sangria
- #FFF8F0 Floral White

The website [Coolors](https://coolors.co/) was used to find an attractive colour scheme which compliments the horror theme.
The raisin black compliments the hero image used but also contrasts against the sangria & floral white which helps the text to pop out against the
background. The colours are clean & simple but also mimic the colour scheme associated with Dracula, a true icon of horror. 

#### Fonts

- Creepster
- Oswald

Both fonts were found on the site [Google Fonts](https://fonts.google.com/). Oswald was chosen as it's a clean font which allows for easy readability.
The Creepster font was used for headers & in the navbar. It clearly gives off a horror vibe with the oozing blood style used.

### Wireframes

- All Wireframes were created using Balsamiq 3 software.

- [Home](https://github.com/JSudron/lightsout/blob/master/images/mockups/Home.png?raw=true).

- [Stories](https://github.com/JSudron/lightsout/blob/master/images/mockups/Stories.png?raw=true).

- [Selected Stories](https://github.com/JSudron/lightsout/blob/master/images/mockups/Selected%20Story.png?raw=true).

- [Edit/Add Story](https://github.com/JSudron/lightsout/blob/master/images/mockups/Edit-Add%20Story.png?raw=true).

## Features/Functionality

### Elements Present On Each Page

#### Navigation Bar 

- The Navbar-brand is used as a link to the homepage whilst the hamburger menu on the right-hand side of the page opens a pop-up menu with links on the left.
- To keep the page looking minimal & clean the hamburger menu was utilised for all screen sizes.

#### Footer 

- Fixed to the bottom of the page has a copyright declaration.
- Provides links to the relevant social media sites along with my Github page. 
- For now generic social media sites are used.

### Other Elements

#### Add/Edit Story Form 

- A simple contact form was used on this page, with all form fields being required to submit the form.
- When editing a story the form fields are all filled in with the relevant info for the selected story.

#### Stories Section 

- Has the relevant image of the story along with author & category of the story. 
- Each story can be clicked on to reveal the story text along with links to edit or delete the current story.

### Features Left To Implement

#### Login/Register

- Make it a requirement to have a username & password to be able to add, edit or delete a story.
- This would allow a further feature which would allow stories to only be edited or deleted by the user who created it.

#### FAQ Section

- Give further info about how the site works & provide contact details to get in touch with the site admin.

#### Story Reviews

- Allow users to leave comments & upvote & downvote stories.

#### Search Bar

- Allow users to search by category, author or keyword.
- Further functionality would be to filter results by popularity, most commented etc.

#### Further Languages

- Add a language choice option to cater to users from various countries.

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python
- Flask

### Libraries

- Bootstrap
- JQuery & Popper
- FontAwesome
- Google Fonts

### Tools

- Github/Gitpod - Used to create & deploy website.
- MongoDB - Stored the database.
- Heroku - Used to deploy the application.
- Balsamiq 3 Mockups
- Google Chrome Dev Tools 

## Database

- The MongoDB database was utilised with a fairly simple many-to-many database.
- The Database has two collections: Stories & Categories.
- The category field in stories links to a key id field for the relevant category in categories.
- [Stories](https://github.com/JSudron/lightsout/blob/master/images/database/database%20-%20stories.png?raw=true).
- [Categories](https://github.com/JSudron/lightsout/blob/master/images/database/database%20-%20categories.png?raw=true).

## Testing

- [Click Here For Testing File](https://github.com/JSudron/lightsout/blob/master/testing/testing.md)

## Deployment

### Cloning from GitHub

- Go to [Lights Out!](https://github.com/JSudron/lightsout) repository page.
- On the repository page click Clone or Download.
- In the Clone with HTTPs section, copy the clone URL for the repository.
- In your local IDE open Git Bash.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 3 - `git clone https://github.com/JSudron/lightsout`.
- Press enter and your local clone will be created.

### Heroku Deployment

- Type `heroku ps:scale web=1` into bash terminal
- Create requirements.txt `sudo pip3 freeze --local > requirements.txt`.
- Create a Procfile `python app.py > Procfile`.
- Type `heroku login -i` & enter login details.
- Go to Deploy on Heroku and under Create New Repository copy the command: `heroku git:remote -a lightsout`, paste into bash terminal.
- In the bash terminal type `git push heroku master`.
- In the Heroku app dashboard, click Settings.
- Click on reveal Config Vars.
- Enter "IP" in first key box. Enter "0.0.0.0" into corressponding value box.
- Enter "PORT" into 2nd key box, enter "5000" into corresponding value box.
- Enter "MONGO_URI" in key box, enter mongodb details in value box.
- Enter "SECRET_KEY" in key box, enter secret key from env.py.
- Site now deployed at [Lights Out!](https://lightsout-joe.herokuapp.com/).

## Credits

### Content

- Most stories were taken from 'It Happened To Me! Vol 3' a small book published by Fortean Times & published in 2010. 
- The stories were often shortened.
- UFO story came from [VICE](https://www.vice.com/en_uk/article/9k8nx5/we-asked-people-at-a-ufo-conference-about-their-alien-encounters).
- Ghost stories also taken from [Huffington Post](https://www.huffingtonpost.co.uk/entry/work-spooky-horror-stories_l_5db0a7fbe4b01ca2a856e337?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAABTn5LEt-5AbPs9DbrSSncnXNISiqRtH8aLQTdXoFy0iJq7Teczkume6oW1YWPXOrE42HeIUokBd3z6OonjnIAhgcMUIH-JyeJnYpyVhgc9RC613Cgr-qaXv68_V6e90cXMhoE__jt6iIUYOPka_5sZBXS2jrQREf_uyIhCH4k5X)


### Media

#### Images

- All images taken from [Pexels](https://www.pexels.com/).

#### Fonts

- Fonts from [Google Fonts](https://fonts.google.com/).

### Acknowledgements

#### Inspiration

- Parts of code were learnt from various sites, which was then amended by myself to obtain the look & feel I was after.
- [Awwwards](https://www.awwwards.com/) was used to look at a variety of sites for design inspiration.
- Colour scheme from [Coolors](https://coolors.co/).
- Slack & [Stack Overflow](https://www.stackoverflow.com/) were used to troubleshoot issues I had.
- Tutor Support was also invaluable, not only the support but their patience.

#### Navbar

- Code learnt from Code Institute tutorials.   
- The slide menu pop-up overlay javascript was learnt from [W3schools](https://www.w3schools.com/howto/howto_js_fullscreen_overlay.asp).

#### Home Page

- Code learnt from Code Institute tutorials. 
- Hero image learnt from [W3schools](https://www.w3schools.com/howto/howto_css_hero_image.asp).

#### Other Pages & Footer

- Code learnt from Code Institute tutorials.

#### Javascript, Python, Flask, CSS

- Code learnt from Code Institute tutorials.

## Disclaimer

### This is for educational use only
