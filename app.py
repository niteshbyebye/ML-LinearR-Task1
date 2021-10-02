from flask import Flask, render_template, request
from joblib import load
model = load('car_pred.joblib')

app = Flask(__name__)

def convert(L):
    K = model.predict(L)
    return int(K[0])

@app.route('/')
def func():
    return render_template('index.html', act = False)

@app.route('/sol', methods =['GET', 'POST'])
def fun2():
    if(request.method == 'POST'):
        model = int(request.form['model'])
        color = int(request.form['color'])
        body_type = int(request.form['body_type'])
        gear = int(request.form['gear'])
        km = int(request.form['km'])
        
        Alloy_wheels = 1 if request.form.get('Alloy_wheels') != None else 0
        CC = 1 if request.form.get('CC') != None else 0
        VC = 1 if request.form.get('VC') != None else 0
        SS = 1 if request.form.get('SS') != None else 0
        SP = 1 if request.form.get('SP') != None else 0
        SPP = 1 if request.form.get('SPP') != None else 0
        SPL = 1 if request.form.get('SPL') != None else 0
        WT = 1 if request.form.get('WT') != None else 0
        TS = 1 if request.form.get('TS') != None else 0
        HP = 1 if request.form.get('HP') != None else 0
        TH = 1 if request.form.get('TH') != None else 0
        RC = 1 if request.form.get('RC') != None else 0
        CRC = 1 if request.form.get('CRC') != None else 0
        TNC = 1 if request.form.get('TNC') != None else 0
        SKB = 1 if request.form.get('SKB') != None else 0
        RHD = 1 if request.form.get('RHD') != None else 0
        
        l=[[model, body_type, color, km, gear, Alloy_wheels, CC, VC, SS, SP, SPP, SPL, WT,TS, HP,TH,
          RC,CRC,TNC,SKB,RHD]]
        
        ans = convert(l)
        act = True  
    return render_template('index.html', act= act, ans=ans)


if __name__ == '__main__':
	app.run()
