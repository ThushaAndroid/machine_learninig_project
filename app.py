from flask import Flask, render_template, request, redirect
from helper import preprocessing, vectrorizer , get_prediction
from logger import logging

app = Flask(__name__)

print('Start server started')
logging.info('Start server started')

data = dict()
reviews = []
positive =0
negative = 0

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    print('========= Open home page =======')
    logging.info('========= Open home page =======')

    return render_template('index.html', data = data)



@app.route("/", methods=['post'])
def my_post():
    text = request.form['text']
   
    print(f'Text : {text}')
    print(f'Text : {text}')

    preprocessed_text = preprocessing(text)
    print(f'Preprocessed Text : {preprocessed_text}')
    logging.info(f'Preprocessed Text : {preprocessed_text}')

    vectrorized_text = vectrorizer(preprocessed_text)
    print(f'Vectrorized Text : {vectrorized_text}')
    logging.info(f'Vectrorized Text : {vectrorized_text}')

    prediction = get_prediction(vectrorized_text)
    print(f'Prediction : {prediction}')
    logging.info(f'Prediction : {prediction}')

    if prediction == "negative":
        global negative
        negative +=1

    else:
        global positive
        positive +=1

    reviews.insert(0, text)

    return redirect(request.url)
    
if __name__ == "__main__":
    app.run()
