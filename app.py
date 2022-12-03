from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder


app = Flask(__name__)

# load he model
model = pickle.load(
    open('C:/Users/MSI GF63/Desktop/MLCLOUD/housepricemodel.pkl', 'rb'))

# routes

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        data1 = float(request.form['category'])
        data2 = float(request.form['Room_count'])
        data3 = float(request.form['bathroom_count'])
        data4 = float(request.form['Size'])
        data5 = float(request.form['Type'])
        data6 = float(request.form['city'])
        arr = np.array([[data1, data2, data3, data4, data5, data6]])
        pred = model.predict(arr)
        print(type(pred))
        pred = str(pred[0])
        return render_template('index.html', prediction=pred)
        # return render_template('index.html', data="aaa")

        # init_feature = [float(x) for x in request.form.values()]
        # final_features = [np.array(init_feature)]
        # prediction = model.predict(final_features)
        # return render_template('index.html', prediction="aaaa")

    #     p = model.predict(data)
    #     print('data: ', data)
    # echo = 'hello'
    # return render_template("index.html")


if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)
