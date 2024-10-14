# BRIEF OVERVIEW
One of the major goals of training machine learning models is to solve real world problems, and this goal can only be accomplished when a trained model is deployed in productions and being actively used by consumers. 

This projects shows how a deep learning model that has been trained and saved in a desired format (e.g. .keras, .h5, .hdf5 etc) can be deployed as an API endpoint, using the lightweight Flask API on Docker. 

In the project, emphasis has been placed on deployment of the model as an API end point on Docker. Hence, the model can still be retrianed (increase epoch number, increase the size of the MINST Fashion dataset, hyperparameter tunning, etc) in future iterations to improve its prediction accuracies. 

The popular MINST Fashion dataset has been used to train a deep learning model that has few layers. 

The trained model was saved in .h5 format and Flask is used to provide an API end point that will enable users to utilize the model for prediction. 

To use the model, users should clone (or download) the code repository onto their own computer system that has Docker running. The project should be decompressed (unzipped). The project directory after decompressing will look as shown below:


![image](https://github.com/user-attachments/assets/f18c09a9-92de-468f-8d6e-206aa3697d1f)

Users can use popular IDEs such as Visual Studio Code, Windows Command prompt (CMD), PyCharm, Jupyter Notebook, etc to navigate to the project directory. For example, users may obtain result similar to the figure below when Visual Studio Code (on Windows OS) is used to navigate to the project directory:


![image](https://github.com/user-attachments/assets/5a5d6af9-5129-415b-a78a-0156706f6de1)

Docker should be running on the users computer. 

The user can then use the Docker command below to build the project.

                                   docker build -t flaskapi . 


After build the project, users can then use any of the commands below to have access to the project's API end point via Flask.

                                  docker run 5000:5000 flaskapi
                                  
                                  docker run -p 5000:5000 flaskapi

                                  docker run flaskapi

The commands options above are provided just in case some other processes may be listening at the port 5000 on the users computer. 

Users can then navigate to http://127.0.0.1:5000 access point on any browser available on their computer to interract with the MINST Fashion prediction model. 

The Flask based API front end will render the front end shown below:


![image](https://github.com/user-attachments/assets/97fdfb5f-c8c1-41f1-99b5-60b1617a5d72)

Users can click on the "Choose File" button and then click on "static", "images" and select any of the provided sample MINST Fashion images to test the API end point. 

An example is shown below:


![image](https://github.com/user-attachments/assets/dadd85ee-c6ce-429f-94cd-b5c65170288d)

Users can then click on the "Predict" button to obtain a prediction as shown below:

![image](https://github.com/user-attachments/assets/f5184dda-65a4-4c4e-8448-1cb5d3a478db)

As stated earlier, the prediction accuracies will be significantly improved in the post beta version of the project. Also, the prediction accuracies will be included. 

The front end will also be included to provide for numerous other details that can provide more useful information about the MINST Fashion data. 













