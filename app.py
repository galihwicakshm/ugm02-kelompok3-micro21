from flask import Flask, render_template, request, send_from_directory
import pickle

app = Flask(__name__)
filename = 'model_prediksi'
loaded_model= pickle.load(open(filename,'rb'))

@app.route('/')
def index():
    return render_template('index.html', prediksi="??")

@app.route('/prediction', methods=['POST'])
def prediction():
    predict= int(request.form['predict'])
    predicted = loaded_model.predict([[predict]])
    return render_template('index.html', prediksi="Rp.{:,.2f}".format(int(predicted)))

if __name__ == '__main__':
    app.run(debug=True)