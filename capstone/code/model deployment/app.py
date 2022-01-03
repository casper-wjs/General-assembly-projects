# referenced from: https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7
# referenced from: https://github.com/xcitech/ml-flask-tutorial, https://xcitech.github.io/tutorials/heroku_tutorial/
import flask
from flask import Flask, request
import pickle
import numpy as np
import pandas as pd

# initializing flask app
app = Flask(__name__, template_folder='templates')

# load in pre-trained model, rb stands for read binary
model = pickle.load(open('model/hdb_model.p', 'rb'))

# load in dummy variables for user input conversion
cat_dict = pickle.load(open('model/cat_dict.p', 'rb'))

# default home route
@app.route('/', methods=['GET', 'POST'])  # @-sign in py is called a decorator
def main():
    if flask.request.method == 'GET':
        # just render the initial form
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        result = request.form

        # prepare categorical feature vector for Prediction
        new_vector = np.zeros(len(cat_dict))

        try:
            new_vector[cat_dict['town_'+str(result['town'])]] = 1
        except:
            pass
        try:
            new_vector[cat_dict['flat_type_'+str(result['flat_type'])]] = 1
        except:
            pass
        try:
            new_vector[cat_dict['flat_model_'+str(result['flat_model'])]] = 1
        except:
            pass

        #new_vector[cat_dict['month_10/1/2021']] = 1

        # extract the input
        age = flask.request.form['age']
        area = flask.request.form['floor_area_sqf']
        mrt = flask.request.form['nearest_mrt_station_dist']
        pri_sch = flask.request.form['nearest_primary_school_dist']
        sec_sch = flask.request.form['nearest_secondary_school_dist']
        mall = flask.request.form['nearest_mall_dist']
        cbd = flask.request.form['dist_cbd']
        storey = flask.request.form['avg_storey']
        year_index = 11

        # make dataframe for the model
        df_cat = pd.DataFrame(new_vector).T
        df_num = pd.DataFrame([[age, area, mrt, pri_sch, sec_sch, mall, cbd, storey, year_index]])

        input_variables = pd.concat([df_num, df_cat], axis=1)

        # get the model's prediction
        prediction = model.predict(input_variables)[0]

        # render the form again but include the predicted hdb price and remind user of their initial inputs
        return flask.render_template('main.html',
                                    original_input = {'Town': str(result['town']),
                                                    'Flat Type': str(result['flat_type']),
                                                    'Flat Model': str(result['flat_model']),
                                                    'Area': area,
                                                    'Age': age,
                                                    'Nearest MRT Distance': mrt,
                                                    'Nearest Primary School Distance': pri_sch,
                                                    'Nearest Secondary School Distance': sec_sch,
                                                    'Nearest Mall Distance': mall,
                                                    'CBD Distance': cbd,
                                                    'Storey': storey},
                                                     result=f'{round(prediction):,}')

if __name__ == '__main__':
    app.run(debug=True)
