# Admission Prediction App
An admission prediction app made using sklearn's linear regression model, and based on the **UCLA Graduate Dataset**

##### App Link - https://admission-predict-python-app.herokuapp.com/


### Ways to set it up:

1. Clone this project to your local project directory.
   - git clone https://github.com/arnabRoy21/admission_prediction_app.git
2. Make any chages or enhancements to code as per your need and commit the changes.
   - git add .
   - git commit -m *message*

### Heroku Deployment Steps:

1. Install heroku CLI and create a heroku web app - **admission-predict-python-app**
2. In heroku CLI, cd to project folder and run - heroku login
3. Add a heroku git remote for the already created heroku web app
   - heroku git:remote -a **admission-predict-python-app**
4. Deploy the app
   - git push heroku main
