# Django_vscode_basic

# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 
# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
# Virtualenv

## Linux

    $ sudo apt-get install python3-venv    # If needed
    $ python3 -m venv .venv
    $ source .venv/bin/activate

## macOS

    $ python3 -m venv .venv
    $ source .venv/bin/activate

## Windows

    $ py -3 -m venv .venv
    $ .venv\scripts\activate
    or
    $ source c:/path_to_the_project or d:/path_to_the_project .venv/Scripts/activate
    or 
    /**
        Select interpreter from ( vscode / pycharm ) to run 
    */
    
## Install project dependencies:

    $ python.exe -m pip install --upgrade pip
    $ pip install -r requirements.txt
    
    
## Then simply apply the migrations:

    $ python manage.py migrate
    

## You can now run the development server:

    $ python manage.py runserver
    $ python manage.py runserver 8007 # Port if needed
    or
    /**
        vscode - create launch.json file for run and debug
        pycharm - set configuration to run and debug
    */

## Administration:

### Create a superuser and enable the administrative interface

    $ python manage.py createsuperuser --username=<username> --email=<email>

    /**
        After creating check with admin url
        http://127.0.0.1:<port>/admin
    */