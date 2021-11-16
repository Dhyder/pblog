# Red Blog
## Author
* [Dhyder](https://github.com/Dhyder)

## Description
A personal blogging website where you can create and share your opinions and other users can read and comment on them.

## Screenshots
![RedBlog](https://user-images.githubusercontent.com/86789832/141859271-f0fb0362-fdd5-4c0c-9d45-dc924815ec6e.png)
![RedBlog](https://user-images.githubusercontent.com/86789832/141933180-34e28487-ef94-41c3-8577-ac2279a64b61.png)
![RedBlog](https://user-images.githubusercontent.com/86789832/141935143-66e019fa-b5c8-4cdd-864f-74964932e0ec.png)

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
| User comments on the Blog post plus a nickname | Write your feedback and post it | Your feedback is displayed under the blog post   |
| Writer deletes a blog post       | Deleting the blog post from the database    | The blog post will be deleted and not appear on the page                  |
| Writer updates a blog post       | Updating the blog post in database    | The blog post will be updated                |
| Writer deletes a comment         | Deleting the blog post in database    | The comment will no longer appear under the post                   |

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
Copyright (c) 2021 **Shaggy**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
