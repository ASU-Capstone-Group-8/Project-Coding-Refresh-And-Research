# Data Annotation Tool Notes:

Date: 
 - 09 October 2024 JST: Argilla
 - 11 October 2024 JST: Label Studio, Snorkel, and final notes

## Potential Tools To Be Used:
 - Argilla
    - https://argilla.io/
    - Used for producing good data-sets used in AI
    - Open-source
    - They specifically take an approach of making the process of data prep and training more manageable through a visual interface, which improves general control over the data and model
    - Provides functionality that organizes workflow associated with training models
        - https://docs.argilla.io/latest/
        - More specifically, they provide tools for a variety of purposes including:
            - A general UI for performing data annotation
            - Capabilities for integrating the process of training into the UI, such that continuous training (through supervised reinforcement) can be accomplished
                - This is a major benefit for Argilla from what I have seen
            - Capabilities for splitting work between several members of a work space
                - This is useful because this is a central problem associated with data labeling and the magnitude of data that must be annotated (splitting the workload improves efficiency)
    - In depth documentation detailing the use of all tools within the library: https://docs.argilla.io/latest/how_to_guides/
    - They provide resources on how to get started for text classification: https://docs.argilla.io/latest/tutorials/text_classification/
        - General steps:
            - Deploy Argilla server via HF Spaces
                - Can also deploy via Docker
            - Login to using the Argilla sign in (should pop up immediately)
            - Then setup a script to build the application and add records to be evaluated
                - Seen here: https://github.com/ASU-Capstone-Group-8/Project-Coding-Refresh-And-Research/blob/main/dlsmallw/PythonPractice/TestingOfPotentialTools/ArgillaTesting/argillaSandbox.py

 - Label Studio
   - https://labelstud.io/
   - Very similar to Argilla
   - Open-source
   - VERY easy setup:
     - Can do a simple pip install, "pip install label-studio"
     - Then you just run it, "label-studio start"
       - This initializes the application and database in a server environment on port 8080
     - Then you just have to login (or create a new account) and you can setup a labeling project there
       - It has a very similar UI to Argilla, but honestly seems more user friendly, since it doesn't require really any code to be written to initialize

 - Snorkel
   - https://www.snorkel.org/
   - Uses a purely programmatic approach to data labeling
   - Open-source
   - This requires code to be written to use it
     - Essentially serves as a library, and you can build a program to take the raw data as input, and it will output a labeled set
   - Probably the most difficult to work with, since it is handled entirely through a program without user input (outside of the code itself)

## General Thoughts
Of these tools, Argilla and Label Studio are probably the best contenders since they both offer hands on interaction during the annotation process
 - Either through manual labeling, reinforcement training or just general monitoring of model predictions

I personally think that Label Studio may actually be more ideal and easier to configure for the following reasons:
 - Very simple setup (2 commands to pretty much run)
   - Although, we may need to configure server hosting for it, in order to make it available to everyone for use
 - Offers all of the features that can be found in Argilla, but simplifies the process of setting up data labeling itself
   - Allows for projects to be setup directly in the GUI
   - data can be directly imported without needing to programmatically import it (can be done in GUI)
   - Has a login system already in place, so this would not need to be implemented (Argilla does not necessarily have a built in login system, it use HF spaces login system)
 - Ultimately, Label Studio is likely the better choice