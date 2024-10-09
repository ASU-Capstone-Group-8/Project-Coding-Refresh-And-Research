# Data Annotation Tool Notes:

Date: 09 October 2024

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
    - They provide resources on how to get started for text classfication: https://docs.argilla.io/latest/tutorials/text_classification/
        - General steps:
            - Deploy Argilla server via HF Spaces
                - Can also deploy via Docker
            - Login to using the Argilla sign in (should pop up immediately)
            - Then setup a script to build the application and add records to be evaluated
                - Seen here: https://github.com/ASU-Capstone-Group-8/Project-Coding-Refresh-And-Research/blob/main/dlsmallw/PythonPractice/TestingOfPotentialTools/ArgillaTesting/argillaSandbox.py
