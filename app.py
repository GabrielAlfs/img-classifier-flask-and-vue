import os
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
from werkzeug.utils import secure_filename
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

MODEL_PATH = 'models/your_model.h5'

model = ResNet50(weights='imagenet')

def model_predict(img_path, model):
  img = image.load_img(img_path, target_size=(224, 224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x, mode='caffe')
  preds = model.predict(x)
  return preds


@app.route('/predict', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    f = request.files['image_file']
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
      basepath,
      'uploads',
      secure_filename(f.filename))
    f.save(file_path)
    preds = model_predict(file_path, model)
    pred_class = decode_predictions(preds)
    result = [
      [
        str(pred_class[0][0][1]), 
        float(pred_class[0][0][2])
      ],
      [
        str(pred_class[0][1][1]), 
        float(pred_class[0][1][2])
      ],
      [
        str(pred_class[0][2][1]), 
        float(pred_class[0][2][2])
      ],
    ]
    return jsonify(result)
  return None

if __name__ == '__main__':
  app.run(debug = False, threaded = False)