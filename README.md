# Red Blog
## Author
* [Dhyder](https://github.com/Dhyder)

## Description
A personal blogging website where you can create and share your opinions and other users can read and comment on them.

## Screenshot
![RedBlog](https://user-images.githubusercontent.com/86789832/141854431-1d713d13-fcc4-459c-8618-8c5b49907af6.png)

## Live Link
You can view the site at: [Red Blog](https://redblogger.herokuapp.com/)

####  User view
* User can view the blog posts on the site
* User sees random quotes on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts

####  Writer view
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading
* update or delete blogs I have created.

## User Story
- A user can view the most recent posts.
- View and comment the blog posts on the site.
- A user should an email alert when a new post is made by joining a subscription.
- Register to be allowed to log in to the application
- A user sees random quotes on the site
- A writer can create a blog from the application and update or delete blogs I have created.

## Specifications
| Input                    | Behaviour                       | Output                                       |
| -------------------------| ------------------------------  | -------------------------------------------- |
| Subscribe to mail list              | Input the email               | Redirect you to the index page               |
| Writer login                    | Take you to home page           | Redirect you to the Homepage                 |
| Create a blog post by filling blog form          | Write your blog and post it to blogs    | Your blog is displayed  in index page                     | 
| User comment on the Blog post plus a nickname | Write your feedback and post it | Your feedback is displayed under the blog post   |
| Writer delete a blog post       | Deleting the blog post from the database    | The blog post will be deleted and not appear on the page                  |
| Writer update a blog post       | Updating the blog post in database    | The blog post will be updated                |
| Writer delete a comment         | Deleting the blog post in database    | The comment will no longer appear under the post                   |

## SetUp / Installation Requirements
### Prerequisites
* python3.8.12
* pip
* virtualenv
* Flask
* pgAdmin4
* SQLAlchemy
* HTML5  
* CSS3
* Javascript 
* Font Awesome
* jQuery

### Cloning
* In your terminal:

        $ git clone https://github.com/Dhyder/pblog.git
        $ cd pblog

## Running the Application
* Creating the virtual environment

        $ virtualvenv
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-bootstrap
        $ python3.8 -m pip install Flask-Script

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests

## Technologies Used
* Python3.8.12
* Flask

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

### MIT License:
Copyright (c) 2021 **Dhyder**