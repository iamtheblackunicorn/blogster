# BLOGSTER :pill: :fire:

***An open source content management system written in Python and Django.*** :pill: :fire:

## ABOUT :books:

I've been writing a lot lately and wanted to make an open source content management system in Django just for fun! This is that CMS. :) You can write your blog here once you have deployed this web app to a server. A list of features is below.

## FEATURES :test_tube:

- Write your blog easily and simply.
- A JSON API for app developers.
- Fully customizable.

## SETTING UP :hammer:

### Requirements :school_satchel:

To run this Django Web App, you will need the following tools installed and available from the command-line:

- Python 3.x
- Django for Python 3.x
- CMake
- Git

### Running :racing_car:

To run this project, follow these steps:

- 1.) Get the source code:

```bash
$ git clone https://$YOUR_GITHUB_TOKEN@github.com/iamtheblackunicorn/blogster.git
```

- 2.) Change directory:

```bash
$ cd blogster
```

- 3.) Sync the database:

```bash
$ make mig
```

- 4.) Create a superuser to create blog posts:

```bash
$ make su
```

- 4.) Serve the Web App locally:

```bash
$ make serve
```

- 5.) Enjoy. :heart:

## USAGE :hammer:

Login with your superuser credentials using the url of your app with the adage of `god`. Click on `posts` and make a new one.
Save it, logout, and go back to the home page.

## DEPLOYING :rocket:

To deploy this Web App, check the instructions for setting up Django Web Apps on your hosting provider's website.

## NOTE :scroll:

- *Blogster :pill: :fire:* by Alexander Abraham :black_heart: a.k.a. *"The Black Unicorn" :unicorn:*
- Licensed under the MIT license.
