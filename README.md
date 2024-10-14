# BRIEF OVERVIEW
One of the major goals of training machine learning models is to solve real world problems, and this goal can only be accomplished when a trained model is deployed in productions and being actively used by consumers. 

This projects shows how a deep learning model that has been trained and saved in a desired format (e.g. .keras, .h5, .hdf5 etc) can be deployed as an API endpoint, using the lightweight Flask API on Docker. 

In the project, emphasis has been placed on deployment of the model as an API end point on Docker. Hence, the model can still be retrianed (increase epoch number, increase the size of the MINST Fashion dataset, hyperparameter tunning, etc) in future iterations to improve its prediction accuracies. 

The popular MINST Fashion dataset has been used to train a deep learning model that has few layers. 

The trained model was saved in .h5 format and Flask is used to provide an API end point that will enable users to utilize the model for prediction. 
