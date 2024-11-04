## Task-120: Label Studio Setup Research and Notes

### Getting it set up for use
 - Can be installed through a few different methods (https://labelstud.io/guide/install.html#Install-with-Docker-on-nix):
    - Installed using pip/pipenv
    - Installed and ran within a Docker image
    - Installed by cloning and running the github repository locally
 - We will likely need to use Docker, since this method can then be conveniently served to a hosting service for making the Label Studio project accessible via the internet.
 - Label Studio will require a hosting service for running and making the app available to the sponsors team:
    - Docker is an option for containerizing the app and then serving it to one of many hosting sites:
        - AWS
        - GCS
        - Azure
        - Hugging Face Spaces (good option to get started with, at least before settling on an official host)
    - HumanSignal (Label Studio creators), also offer an Enterprise-level product, where they host and provide additional support and services
        - This may be unnecessary for our applications though
 
#### Personal Testing Notes:
 - General Info:
    - When running the application, it will automatically configure and initialize a SQLite database for managing the data that is imported into the app.
    - It also comes with a built in authentication system (login) for users, so we won't need to worry about this
    - Provides an API for interacting with a running instance of the service programatically, so we could potentially use this in some way
    - The application also has source and destination storage linking, so we can automatically set it up to pull from a storage source containing non-labeled data, and then push any labeled data to another location automatically
        - This is immensely convenient

 - Installing and running locally through the use of pip:
    - Relatively simple, but this method wouldn't be super ideal when setting up the service on a hosting service:
        - Label Studio isn't secure by default, and actual hosting service would need some additional security mechanisms to prevent any web-based security issues
 - Installing and running within a docker container:
    - Simple like with using pip and setting up a venv, but takes less (command-based) steps
    - Would be fairly simple to serve a docker container with the app to a hosting service and then just run it
    - There are however some security warnings associated with the official label-studio image that we would use (discovered when using Docker Desktop and running the scout analyzer)
        - These warnings consisted of several High and Medium level vulnerabilities that would need to be considered and any potential protections implemented

 - Served using Hugging Face Spaces:
    - This is probably the easiest of any of the methods, since Hugging Face Spaces already has a docker image ready to be configured and launched
    - For the purposes of our project, this could very well meet all of our (and the sponsors) needs for labeling and organizing training/assessment data
    - Only major concern with this route, would be the fact that we would need to figure out a method for maintaining data (login information) such that an issue causing the server to go down would not wipe out all user credentials
        - Might be able to set up the application to regularly backup user credentials to an external database, so that we have that available if/when the server goes down
        - The data being labeled is no concern, since we would be importing and directly exporting already labeled data

### Current Expected Strategy
 - We will move forward with using HF Spaces for now since it is simple, quick and relatively reliable
 - Once we have source and destination storage locations set up, we can then link these databases
 - For the web scraping application:
    - Current plan is to have a new page, that uses either a WebContextView or a Webview element for effectively openning the label studio app in the application
    - We will also set up a setting or some option to specify the URL to the Label Studio app we will be using
    - Users will be able to interact with the label studio application within the web scraping app just as if they were in a browser (thanks to electron being a framework that uses chromium)
