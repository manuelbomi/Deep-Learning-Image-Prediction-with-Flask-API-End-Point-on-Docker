from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model('fashionMnist.h5')
target_img = os.path.join(os.getcwd() , 'static/images')

@app.route('/')
def index_view():
    return render_template('index.html')

#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
           
# Function to load and prepare the image in right shape
def read_image(filename):

    img = load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=model.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            if classes_x == 0:
              mnist1 = "Tshirt/top"
            elif classes_x == 1:
              mnist1 = "Trouser"
            elif classes_x == 2:
              mnist1 = "Pullover"
            elif classes_x == 3:
              mnist1 = "Dress"
            elif classes_x == 4:
              mnist1 = "Coat"
            elif classes_x == 5:
              mnist1 = "Sandal"
            elif classes_x == 6:
              mnist1 = "Shirt"
            elif classes_x == 7:
              mnist1 = "Sneaker"
            elif classes_x == 8:
              mnist1 = "Bag"
            else:
              mnist1 = "Ankle Boot"
            
            return render_template('predict.html', mnist1 = mnist1, user_image = file_path)
        else:
            return "Unable to read the file. Please check file extension"

if __name__ == '__main__':
    app.run(host='0.0.0.0')