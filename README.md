# Console Kingdom

## E-Commerce store for gaming consoles

![Webiste on a range of devices]()

### Live site available [here](). 

## Table of Contents

- [Description](#description)
- [Design](#design)
- [UX](#ux)
- [Agile Development](#agile-development)
- [Web Marketing](#web-marketing)
- [Features](#features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Author Info](#author-info)


## Description

Console Kingdom is a fully functional E-Commerce store built in Django using Python, JavaScript, CSS, Bootstrap5, HTML and it incorporates stripe payments. It includes user authentication and Full CRUD functionality for products.

Console Kingdom is a small gaming console supllier based in Co. Wicklow. Specializing in the latest gaming technology. With products ranging from gaming consoles to accessories for the listed consoles

This version has been built for project 5 of the Code Institute Diploma in Software Development and therefore doesn't accept real payments and any orders made won't be fulfilled.

But a fully operational live site will be released soon.

If you would like to test the payment functionality please feel free to do so by entering the card details below when prompted:

`Card number:  Exp: any future date eg. 05/25 CVC: any 3 digits eg 123`

[Back to the Top](#table-of-contents)

## Design

### Wireframe mock-ups
---
Home page: 

The home page provides the user with a clear understanding as to the purpose of the site. 

The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using.

![Home Page Wireframe]()

Shop Page:

Users have the ability to view information on available products and add them to a cart for purchase. 

The emphasis of the design is to provide a clear layout that can adapt to any size device.

![Shop Wireframe]()

About Page:

Users can view a page dedicated to the business, this page includes basic information about the business.

![About Wireframe]()

Cart Page:

Users can view the cart with their chosen items, it includes a total price for items in the cart.

![Cart Wireframe]()

Checkout Page:

The checkout page will include a summary of items in the cart and all relevant information needed for a successful order ie. Contact Details, Delivery Details & Payment Details.

![Checkout Wireframe]()

Site Footer:

The Footer is responsive and universal across the site, it includes contact information and social media links.

![Footer Wireframe]()

Wireframes were also produced for each major page for both mobile and tablet devices. With the intention of the site being fully responsive.

[Back to the Top](#table-of-contents)

## Database Schema

Several custom models were required when building the site. On top of the standard Sculpture/Order models these included a Newsletter signup Model a Message Model and a customer Review model. The database schema was drawn out by hand.

![Database Schema Diagram]()

[Back to the Top](#table-of-contents)

## UX
Console Kingdom was designed to be a friendly and informative site for users to easily browse and find products they would be interested in purchasing. The graphical elements and overall design of the site provide the user with a fun and enjoyable environment.

### The Sites Ideal User
Someone looking to purchase a gaming console or some accessories for their current console.

### Site Goals

* To provide the site owner with a place to sell stock.
* To provide the site owner with a place to expand his digital presence.
* To provide users with an enjoyable and easy to use site for making purchases.

[Back to the Top](#table-of-contents)

## Agile Development

The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using issues on GitHub. Each user story explicitly explains the purpose of the issues.

31 User stories were developed. In practice some of these tasks were completed much quicker than anticipated and others took a little longer but overall the development went smooth.

### User Stories

#### User Stories in GitHub [here]()

These are a few examples of ther main user stories.

- User Sign in or Sign out
	*  User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can avail of the sites full functionality
	*  Receive Welcome Emails - As a user I would like to receive a welcome email upon signing up
    *  Reset password Functionality - As a user I would like to be able to reset my password to keep my account safe
    *  Visibly logged in or out - As a user I would like to know if I am logged in or not

- Landing page
	*  As a User I would like to be brought to the landing page upon first visiting the site so that I can see what options are available to me
    *  As a User from the landing page I should clearly be able to see and navigate the navbar
    *  As a User on the landing page I should be easily able to go straight to the shop and purchase an item

- View Products, Admin CRUD
    *  As a user I should be easily able to see a list of products available.
    *  As a user I should be able to click on any item to see more information about it.
    *  As an Admin I can add products to the database
    *  As an admin I can edit products in the database
    *  As an admin I can delete products from the database

- Shopping Cart
    *  As a user I can easily view the contents of my Cart
    *  As a user I can easily add/edit/delete the contents of my Cart
    *  As a user I can easily identify the total cost of my Cart

- User Feedback/Confirmation
    *  As a user I receive prompt feedback concerning my activity on the site
    *  As a user I can see a order confirmation message
    *  As a user I receive an order confirmation email

- Payment Feature
    *  As a user I can visit a payment screen
    *  As a user I can input my credit/debit card details

- User Profile
    *  As a user I can sign in/create a profile so that I can avail of the sites full functionality

- Contact/Social links
    *  As a user I can fill out a contact form
    *  As a user I can clearly see contact information
    *  As a user I can easily find social media links and when pressed they take me to the correct site

- Customer Reviews
    *  As a user I can clearly see reviews left by past customers
    *  As a user who is logged in I can easily leave a review

[Back to the Top](#table-of-contents)

## Web Marketing

#### **E-Commerce Application Type**
Console Kingdom is a B2C e-commerce application. Selling directly to consumers means that the site is designed to sell quickly, on impulse, and in smaller quantities. A large amount of the functionality is focused on the user experience and the ability to purchase products quickly and effectively. Wholesale is a future goal of the company.

#### **Marketing Strategy**
As Console Kingdom is a start-up business, the budget for marketing is limited. However, there are several ways that Console Kingdom can market itself to help increase sales and brand awareness. Using Facebook to pump out content and drive traffic is the first and most straightforward. The use of paid ads allows the business to target specific demographics and increase brand awareness. The use of social media is also a great way to get feedback from customers and to help with customer service. There is an image of the Facebook page below and a link to the page [here]().

The second is the use of google ads which are a great way to increase brand awareness and help with SEO. The use of google ads can also help with the use of long-tail keywords and help with the ranking of the site.

The final method would then be sending regular news letters to the mailing list obtained via the signup form. The newsletter would contain links to recent articles, the latest products, special offers and promotions. This would help with brand awareness building a community around the brand.

#### **Search Engine Optimization**
SEO research is key to driving traffic from a browser based search i.e. Google to the website. The keyword research has played a crucial role in incorporating words that users typically search for when seeking to purchase consoles online. To help improve the search engine ranking I ensured the site carries meta tags for a description and keywords which encapsulate the general content and focus of this B2C site.

#### **XML Sitemap**
Additionally to help the search engines crawl the website, I've added an XML sitemap file to the main root directory. The file was created using the free service through XML-Sitemaps.com. A sitemap is a way of organizing a website, identifying the URLs and the data under each section. Previously, the sitemaps were primarily geared for the users of the website. However, Google's XML format was designed for the search engines, allowing them to find the data faster and more efficiently.

A robots.txt file has also be included in the build to tell the search engine crawlers which URLs the crawler can access on this site. This is used mainly to avoid overloading the site with requests.

#### **Facebook Page**
![Facebook Page]()

## Main Features

#### Home page
A welcoming homepage was built to welcome the user to the site and clearly convey the sites purpose. The call to action buttons for the user to go straight to the shop or contact the site owner is at the top of the main page.

![Home Page]()

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links.

![Nav Bar]()

#### Footer
A common footer is utilised throughout the site.

![footer]()

#### Other Features
[About Page]()

[Shop]()

[Cart]()

[Checkout]()

[Featured Products]()

[Newsletter Signup]()

[Sign Up]()

[Sign In]()

[Individual Product Page]()

## Future Enhancements
There are several items of functionality that I would like to add in the future. The key areas I would like to add to the site in the future are:

* The ability for users to login via social networks such as google or facebook
* Other payment options ie. Paypal

[Back to the Top](#table-of-contents)

## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site.

#### Validator Testing
All code files were validated using suitable validators for the specific language. HTML & CSS code passed the validation. JavaScript code passed the validation.
All validation screenshots are included below.

## HTML
ll HTML validation returned the same result so I have included only 1 screenshot here.

![HTML Validation]()

## CSS
![CSS Validation]()

## Script JS
![Script JS]()

#### Lighthouse Testing
Below you can see the results of Googles Lighthouse Testing.

![Lighthouse Testing Desktop](./docs/lighthouse-desktop.png)
![Lighthouse Testing Mobile](./docs/Lighthouse-mobile.png)

#### Python/JavaScript Testing
All Custom Python & JavaScript code was manually tested multiple times during and after development.
This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

## Testing User Stories
Need to check with mentor.

## Bugs
Placeholder text

[Back to the Top](#table-of-contents)

## Technologies

* Python
* Django
* Heroku
* PostgreSQL
* JavaScript
* Bootstrap 
* Font Awesome
* CSS
* HTML
* Stripe

#### Packages Used

* VS Code & Gitpod was used to develop the site.
* Git was utilised for version control and transferring files between the code editor and the repository.
* GitHub was utilised for storing the files for this project.

#### Resources Used

* The Django documentation was used extensively during development of this project.
* The Cloudinary documentation was used.
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.

[Back to the Top](#table-of-contents)

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Console Kingdom]()

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered RossAnthonyDesigns and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staticfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: gunicorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
* Log into GitHub or create an account.
* Locate the repository at https://github.com/KSheridan86/project-5-RossAnthonyDesigns .
* At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
* A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/KSheridan86/project-5-RossAnthonyDesigns
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

[Back to the Top](#table-of-contents)

## Credits
- Code Institute course work was used as reference. 

## Acknowledgements

I would like to acknowledge the help and support given by my mentor Jubril Akolade.

[Back to the Top](#table-of-contents)