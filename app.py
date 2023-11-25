from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('iris.pkl','rb'))



@app.route('/')
def home():
    result=''
    return render_template('index.html',**locals())


@app.route('/predict',methods=['GET','POST'])
def predict():
    SL=float(request.form['SL'])
    SW=float(request.form['SW'])
    PL=float(request.form['PL'])
    PW=float(request.form['PW'])
    result = model.predict([[SL,SW,PL,PW]])
    return render_template('index.html',**locals())

if __name__=='__main__':
    app.run(debug=True)         