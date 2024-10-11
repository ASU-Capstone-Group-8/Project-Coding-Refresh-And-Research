## Task-41 Model Training and Deployment for NLP Models Research

Date: 11 October 2024

# Model Training:
 - General Overview:
   - Useful article:
     - https://www.datacamp.com/tutorial/fine-tuning-large-language-models
   - This is the point where you are taking the formatted data sets from the previous steps and feeding these into the model to train it.
   - We will be fine-tuning a pretrained model since this would be the most efficient route for our project.
   - Different types of fine-tuning:
     - Supervised fine-tuning:
       - Process of taking a labeled data set, and using it to train the model to a specific task
     - Few-shot learning:
       - Process of passing a few samples of labeled data associated with the task, before the actual task itself, in order to give the model context on what it is intended to do.
       - This is a very fast and dirty method of training
     - Transfer learning:
       - This is essentially just taking a pretrained model trained on a large corpus of data and using it in a more specific context
       - Essentially, this is just attempting to leverage a wider amount of learned language data to see if it can perform a more specific task
     - Domain specific:
       - Training to a very specific domain or industry
       - Medical, Automotive, etc.
     - General steps for fine-tuning:
       - Gather data sets
       - Load the data (annotated data more specifically)
       - Tokenize the data
       - Initialize the (base) model
       - Prepare an evaluator for assessing the model performance
         - This is important, because it will determine if the model is on the right track (progressing positively or negatively)
       - Setup the trainer (the tool that sets up the training configuration) and start training the model
       - Evaluate the newly trained model to determine performance
         - This will use a validation/test set of data
   - General best practices:
     - Quality over quantity of data
       - The quality of data can have a bigger effect on training than quantity
     - Understand hyperparameter adjustments
       - This will be the bulk of the training process, simply adjusting different hyperparameters to adjust the training output
     - Regularly evaluate the model training
     - Avoid over/underfitting
       - Overfitting: Using to small of a data set or an excessive number of epochs.
         - Will be shown by high accuracy on training data but low on real data
       - Underfitting: Insufficient training or low learning rate; Fails to learn its intended task effectively
     - Avoid Forgetting: Fine-tuning can potentially result in the model forgetting data/information it was pretrained with.
     - Ensure training/validation data sets are maintained separate

 - Potential Tools:
   - Pandas 
     - Good for formatting the data into the appropriate structures
   - PyTorch/TensorFlow:
     - Both libraries offer extensive tools for model training
   - KubeFlow
     - Provides a pipeline service that streamlines the entire model development/training/deployment process

# Deployment:
 - Useful article:
   - https://neptune.ai/blog/deploy-nlp-models-in-production
 - There are a few ways to do this, but they all generally involve deploying a model to a hosting service
   - For instance, you can deploy a model to HuggingFace Spaces and use their model inference API
 - Could also consider a different backend framework (Django/Flask)
 - Building an API from scratch could work, but it would generally involve a decent amount of work
 - Containerization is also a big component of efficient, problem free deployment of a model
   - Can use something like docker or kubernetes to containerize the model with all of the necessary tools, programs and dependencies
   - Makes it so that the model can be deployed to pretty much any machine/environment and still work without preconfiguring it

### Current Expectations:
 - Based on the ease of use and streamlined services they provide, we will likely use KubeFlow for setting up the training pipeline
   - They provide specifically tailored components to manage every aspect of the pipeline, and also have service-tailored integrations with AWS, Azure, GCS, etc.
 - For deployment, we haven't determined how we will go about this just yet
   - For the time being, we may make use of Argilla/Label Studio for demonstrating the models functionality since they allow integrating the model into these tools
     - i.e., you can integrate the model into Argilla/Label Studio and use it as an interface for feeding data into the model and generating an output based on its prediction