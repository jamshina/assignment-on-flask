from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('iris.pkl','rb'))



@app.rout('/')
def home():
    result=''
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    sepal_lenght=float(request.form['SL'])
    sepal_width=float(request.form['SW'])
    petal_lenght=float(request.form['PL'])
    petal_width=float(request.form['PW'])
    result = model.predict([[sepal_lenght,sepal_width,petal_lenght,petal_width]])
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)         