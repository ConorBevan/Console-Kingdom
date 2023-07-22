# Console Kingdom

## Introduction

Console Kingdom is a fictional B2C e-commerce store that is designed and implemented with Python and Django, HTML, CSS and some Javascript. It specialises in selling gaming products to consumers online.

Link to deployed site can be found [Here](https://console-kingdom-1-e73d5794a126.herokuapp.com/)

## Responsive Design
![Home page](media/)

### Strategy
* Console Kingdom is a B2C type of business. In recent times online shopping has becom e the more preffered choice of pursching goods. Console Kingdom aims to offer flexible online shopping to its customers.

# UX
## User stories
## As Admin
* As a admin I can manage users' accounts so that I can make any required changes to them if needed
* As a admin I can manage products so that I can add, update or delete products when necessary
* As a admin I can view created orders so that I can full fill the orders or amend if needed
* As an admin I can manage the newsletter signees

## As a site user
* As a site user I can create or edit my account so that I can update my details accordingly
* As a site user I can login in my account so that I can view my order history
* As a site user I can shop for products
* As a site user I can browse through products so that I can decide what I may be interested in buying
* As a site user I can look at product details so that I can decide if I want to purchase it
* As a site user I can easily add products I want to purchase to a cart so that I can decide whether to purchase or not
* As a site user I can view the contents of my shopping basket so that I can be able to make any adjustments
* As a site user I can update my bag by adding more or remove products so that I can decide on the number of products I intend to buy
* As a site user I can view my order summary so that I can verify it before confirming
* As a site user I can checkout securely so that I can I maintain the level of trust on the site
* As a site user I can use the contact details in the footer to contact the site owners
* As a site user I can sign up to newsletter

## Architecture

## Database

<details>
  <summary>Click here to view Database Schema:</summary>

  ![]()

</details>

## Design
Before I wrote any code for this site, I had to pin point a simple design of what I wanted my site to look like by using wireframes.

<details>
  <summary>Click here to view Wireframes:</summary>

  ![](media/)
  ![](media/)
  ![](media/)
  ![](media/)
 
  </details>

## E-commerce type

Console Kingdom is an online store that sells directly to customers. The functionality on this site for a regular customer is ability to make a purchase swiflty and quickly. For the owners, the goal is to archieve CRUD functionality.

## Marketing
Though there are a lot of marketing techniques for businesses, Console Kingdom decided to first use, facebook to drive out content and engage with customers. Visit our facebook page [here](https://www.facebook.com/Console-Kingdom-115364421628176). 

# Features
## Homepage

To start off, clicking the Console Kingdom url takes you to the home page with a logo on the left, my account and shopping bag to the right, followed by a navigation menu and footer. All these appear on every page on the site. Also found on home page is a hero image accompanied by a modal that describes what the business is about.

### Navbar

![header](media/)

### Home Page

![home](media/)

### Register/Sign up

On the right side of the home page, for the first time user they will need to register their account to enjoy most of the site benefits such as saving their order details. When registering users are asked their username, email and password.

![register](media/)

### Sign In

Registered users would need to sign in when they visit the site again. They will be asked to enter their username and password. The Remember me option is also available making life easier for returning users. Is users need to reset their password, a forgot password is also available.

![login](media/)

### Logout
Users are able to leave their account by logging out of the site.

![logout](media/)

## All Products

The first navigation link from the logo is all products. This is where you can display all products available.

![products](media/)
 
 ### Product Detail and Add to Cart

 Each product on site has a detailed information in form of a name, price,image, description. The user is displayed with a quantity input box to select the quantity they need to add to the shopping bag either increasing or decreasing. They have an option to go back to products by clicking the keep shopping button. Each time a user add a product to the bag they get a notification that alert them of that action.

 ![detail](media/)

 ![add to bag](media/)

 ### The Shopping Bag

 Consists of the price, quantity of each item and sub total. User has an option to update their bag and or remove some items from bag. They can easily go back to products by clicking keep shopping or go to checkout.

![bag](media/)

### Checkout

On the left side of the checkout is where user puts their information, and on the right side is a summary of their order that is the total, the delivery.

![checkout](media/)

### Checkout Success

After completing an order, users receive an order confirmation with their details including order number.

![order confirm](media/)

### Product detail- Super User

If the user is the super user, they have an option to either delete or edit their product

![detail](media/)

### Add Product

Only super users are authorized to add products to products catalogue

![add product](media/)

### Edit Product

Super users only can edit the product by editing either name, description, price and update image. 

![edit](media/)

### Delete product

Super users only can as well delete the products from the site

![delete](media/)

# Footer

The footer appears on all pages of the site, it contains the newsletter sign up, about us, and social links

![footer](media/)

## About Us Modal

About us modal describes in brief what the site is all about to the users.

![about](media/)

# My Profile

The my profile page displays a user's saved contact infomation and their order history

![profile](media/)

# 404 page

A 404 page is also available to handle navigation errors with a home link button to take them back to the home page

![error handling](media/)

### Future features

* Product rating by users

# Web marketing

## Email marketing

Each user that signs up is added to the newsletter list.

## Search engine optimization

SEO keywords

![seo](media/)

## Social media marketing

A facebook page was created to build community from the target market. Facebook is free and it also takes little to no time to set up and also it has so many users whom a business can strive to maintain a certain relationship, create content and connect with a target audience.

![facebook](media/)

## Technologies

### Languages

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

* [Javascript](https://www.javascript.com/)

* [Python](https://www.python.org/)

### Frameworks, programs and libraries used

* [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

* [Bootstrap4](https://getbootstrap.com/) - A css framework

* [Gitpod](https://www.gitpod.io/) - Gitpod was used as an IDE

* [Github](https://github.com/) - I used Github to store all the data of my project after pushing it

* [Heroku](https://www.heroku.com/) - is a cloud platform service  I used to deploy and host the project

* [ElephantSQL](https://www.elephantsql.com/) - used as a database for the project

* [Font Awesome](https://fontawesome.com/) - Was used to add icons for my social media links.

* [PEP8ci](https://pep8ci.herokuapp.com/) - I used it to validate python code

* [Stripe](https://stripe.com/en-ie) - was used for checkout functionality and facilitate online payments

* [AWS](https://aws.amazon.com/s3/) - for  object storage through a web service interface.

# Testing

## Manual Testing

 | Feature | Test  | Expected Result | Actual Result |
| -------------| ----- | ----- | :----: |
| Console Kingdom  | Selecting logo on homepage |  directs user back to homepage |  Pass |
| Navigation Links  | Selecting navigation links |  directs user to relevant pages |  Pass |
| Products Page  | Selecting products |  directs user to products |  Pass |
| Back to Top | Back to top button | Select the button on the products page brings the user back to the top of the page  |  Pass |
| About Us Button | Selecting About Us |  opens the about us modal |  Pass |
| Sign up for our newsletter | selecting Sign up for our newsletter |  notifies user is signed up to newsletter |  Pass |
| Privacy policy | Selecting privacy policy |  directs user to privacy policy|  Pass |
| Facebook icon | Selecting  facebook icon |  directs user to Console Kingdom facebook page |  Pass |
| Contact | Selecting Contact | directs user to contact section in the footer  |  Pass |
| My account | Selecting my account as admin | displays dropdown menu unique to admin apart from account and logout  |  Pass |
| Add product | Adding a new product| successfully add new product to products page  |  Pass |
| Add Product | no image is selected | default image is used |  Pass |
| As Admin edit product | editing product |  successfully edited the product |  Pass |
| As Admin Delete product | Deleting product|  successfully remove product |  Pass |
| Register | Register for an account | selecting Register in my account directs user signup page |  Pass |
| Register | Registering as a new user | Registering as a new user form works |  Pass |
| Login | Login to an account | selecting Login in my account directs user to Login page |  Pass |
| Login | Login to an account | login-in as a new user form works |  Pass |
| Login as admin| Login to as admin gives access to product management functionality | login-in as a new user form works |  Pass |
| Logout | message shown | Logging out message shown |  Pass |

## User story testing
### Admin
* As a admin I can manage users' accounts so that I can make any required changes to them if needed
   > Admin can manage user accounts from admin panels
* As a admin I can manage products so that I can add , update or delete products when necessary
   > Admin can add, delete and update products on the site
* As a admin I can view created orders so that I can full fill the orders or amend if needed
   > Admin can view orders in admin panel
* As a Admin I can delete any of comments so that I can remove them if I nolonger feel they are still necessary or needed
   > Only admin can delete comments 
* As a Admin I can view messages sent via contact form so that I can act upon them
   > Admin can view send messages in the admin panel
* As an admin I can manage the blog content so that I can make amendments if needed
   > Admin can add, edit or delete blogs via blog management. only accessible to admin

## User Story testing

### User
* As a site user I can create or edit my account so that I can update my details accordingly
   > A user can create an account using register and update on my profile
* As a site user I can login in my account so that I can view my order history
   > Logged in user can view order history if they made a purchase before
* As a site user I can search for products so that I can find specific products
   > I made sure users can search for what they want using search bar
* As a site user I can sort products on criteria such as price and category so that I can I have a method of ordering the products
   > I made products to be filtered by price or category for users to choose how they want to view
products as I prefer
* As a site user I can browse through products so that I can decide what I may be interested in buying
   > I made the site such that its easy to browse through all products so they see what to order
* As a site user I can look at product details so that I can decide if I want to purchase it
   > Each product has a  detailed description so users understands more of it
* As a site user I can easily add products I want to purchase to a basket so that I can decide whether to purchase or not
   > Users can easily add products to bag
* As a site user I can view the contents of my shopping basket so that I can be able to make any adjustments
   > User can view bag contents by clicking the bag itself
* As a site user I can update my bag by adding more or remove products so that I can decide on the number of products I intend to buy
   > User can update the bag to a quantity they want or remove everything entirely
* As a site user I can view my order summary so that I can verify it before confirming
   > From secure checkout, users can verify their order summary before buying
* As a site user I can checkout securely so that I can I maintain the level of trust on the site
   > I made sure users have secure checkout when completeing a purchase
* As a site user I can view paginated posts so that I can select which posts to view
   > Blog posts are paginated, clear and easy to see so to select which to view
* As a site user I can view all posts so that I can decide what I may be interested in reading
   > Users can easily choose which one to read
* As a site user I can comment to the blog posts so that I can express my opinion to the post
   > I made the site such that signed in user can comment on blog posts
* As a site user I can use the contact form so that I can contact the site owners
  > By using the contact form, user can send messages to the site owners
* As a site user I can sign up to newsletter so that I can keep updated on the latest news
  > By going to sign up newsletter on the footer, users can easily sign up to receive latest news.

## Functionality testing

Throughout developing this site, I have been using Chrome, and chrome dev tools to help with debugging issues. Testing responsiveness was done using chrome emulated devices.

## Compatibility testing

Chrome emulated devices, and hardware devices iphone 13, samsung A51 and samsung tablet E were used to test compatibility

### Javascript validation
I used JSlint to validate javascript found in some apps

* cart app - 

* blog app - 

* base.html - 

* newsletter - 

* checkout - 

* products - 

* users - 

### Python
[ CI Python linter ](https://pep8ci.herokuapp.com/) was used to test python code

## Bugs

For this project there were so many bugs I encountered from the beginning though some were minor.

### Bug 1
Toasts not showing/displaying - Having all the code set up properly and checking in chrome dev tools I could see they were rendering in my template however not displaying. To fix this,I had to add a cdn which was not working rgianlly and now all toasts work as intended.

### Bug 2
My deployed app on heroku wqs displayed as 404 error. I had added https:// in the allowed host in my settings.py.

### Bug 3
Another noticeable bug was when the aaplication was in mobile the footer was covering the content. I fixed by adding a custom id and having height set as auto so fucntionalyt could resume.

# Deployment

I developed this site on Gitpod, using git for version control. Then deployed to Heroku using the following steps

* Log in to [Heroku](https://id.heroku.com/login) or create an account

* Click New and Create New App

* I selected Europe as region.

* Click Create App button

I then went to create a database to connect to the new created app.

* Login to [ElephantSQL](https://www.elephantsql.com/)

* Create new instance

* Set up your plan - Give the plan a name and select Tiny Turtle free plan

* Select region button

* Select a data center ner your. I selected EU-West-1(Ireland)

* Click Review

* Click Create instance

* Return to elephantsql dashboard, click on database instance name

* In the url section, clicking the copy icon will copy the database url to the clipboard

* Go back to Heroku to your created app, go to Settings

* Add config var DATABASE-URL, and for the value, copy in your databse url from ElephantSQL. do not add quotation marks around your database

* In Gitpod install dj-database_url and psycopg2 to connect to your external database

* Update requirements.txt: pip freeze > requirements

* import dj_database_url in settings and update your database

* migrate your database

* create a new superuser for your database and at this point your database is exposed do not commit it to github

* Install gunicorn and freeze into the requirements file

* Then create Procfile

* DISABLE_COLLECTSTATIC

* Commit and push to github

* On your app in Heroku go to Deploy and connect it to github and search your repository, click connect.

* Choose automatic or manual deploy. I chose manual. Click deploy branch

* When complete click View to open the deployed app

## From Github docs

### Forking 

* Open GitHub page that hosts the repository you wish to fork.
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository

### Cloning

* Open Go to the repository page on Github
* click on the green button that says "Code".
* You can choose to download a zip file of the repository, unpack it on your local machine, and open it in your IDE.
* Copy the URL under the HTTPS tab to clone using https.
* In a new window, and set the current directory to the one you want to contain the clone from.
* Type git clone and paste the URL copied from the GitHub page.
* The repository clone will now be created on your machine. 

## Credits

* Code Institute Botique Ado walk through

* [Stack overflow](https://stackoverflow.com/)

Products description inspiration from

* [Currys](https://www.currys.ie/)

### Acknowledgement and support

* My Mentor Jubril Akolade















                  
