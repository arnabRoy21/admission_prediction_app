from flask import Flask, request, redirect, render_template, url_for
import pickle
import os

app = Flask(__name__)
path = os.getcwd()
# print(path)
scaler_model_path = path + '\scaler_model.pickle'
linear_regression_model_path = path + '\linear_regression_model.pickle'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            univ_rating = float(request.form['univ_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            research = float(request.form['research'])

            scaler_model = pickle.load(open(scaler_model_path,'rb'))
            mean = scaler_model.mean_
            std = (scaler_model.var_)**(0.5)
            # print(mean)

            gre_score_norm = (gre_score - mean[0])/std[0]
            toefl_score_norm = (toefl_score - mean[1])/std[1]
            univ_rating_norm = (univ_rating - mean[2])/std[2]
            sop_norm = (sop - mean[3])/std[3]
            lor_norm = (lor - mean[4])/std[4]
            cgpa_norm = (cgpa - mean[5])/std[5]
            research_norm = (research - mean[6])/std[6]
            
            
            reg = pickle.load(open(linear_regression_model_path,'rb'))
            chance_of_admit = reg.predict([[gre_score_norm, toefl_score_norm, univ_rating_norm, sop_norm, lor_norm, cgpa_norm, research_norm]])[0]*100
            chance_of_admit = round(chance_of_admit, 2)
            # print(chance_of_admit)
            return render_template('index.html', chance_of_admit=chance_of_admit) 
        
        except:
            err_message = "Something Went Wrong! Please try again."
            render_template('index.html', err_message=err_message) 
            
    return render_template('index.html', chance_of_admit=None) 

if __name__ == '__main__':
    app.run(debug=True)