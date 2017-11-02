[![Build Status](https://travis-ci.org/JoyyToo/Yummy-Recipes.svg?branch=ft-app)](https://travis-ci.org/JoyyToo/Yummy-Recipes) [![Coverage Status](https://coveralls.io/repos/github/JoyyToo/Yummy-Recipes/badge.svg?branch=master)](https://coveralls.io/github/JoyyToo/Yummy-Recipes?branch=master)MIT License

Copyright (c) [year] [fullname]

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

It contains:
 - Designs
 - Wireframes
 - Yummy Recipes application

## Designs

Contains HTML and CSS files for UI.


## Wireframes

Contains designs for the UI folder.

## Yummy Recipes App Description

Contains a Yummy Recipes flask app that provides a platform for users to keep track of their awesome recipes and share with others if they so wish.

## Features

- Users can create accounts
- Users can log in
- Users create, view, update and delete recipe categories 
- Users can create, view, update or delete recipes in existing categories

## Sign Up
![Alt text](https://joyytoo.github.io/Yummy-Recipes/Designs/UI/Screenshots/signup.png?raw=true "Sign Up")

## Log in
![Alt text](https://joyytoo.github.io/Yummy-Recipes/Designs/UI/Screenshots/signin.png?raw=true "Sign In")

## Recipes
![Alt text](https://joyytoo.github.io/Yummy-Recipes/Designs/UI/Screenshots/rec.png?raw=true "Recipes")

## Prerequisites

Python 2.6 or a later version

### Setup

Use the following:

```
$ sudo pip install virtualenv
$ mkdir Yummy-Recipes
$ cd Yummy-Recipes
$ virtualenv venv
```

Activate virtual environment:

```
$ source .venv/bin/activate
```

To set up flask:

Enter the command to install in virtual environment:

```
$ pip install Flask
```

To set up unit testing environment:

```
$ pip install nose
```

To execute a test file:

```
$ source .env
$ nosetests
```

## Running App

- `cd` directory of extracted project
- run using:$ ` source .env`
            $ ` python run.py`



