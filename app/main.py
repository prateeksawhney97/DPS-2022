from flask import Flask,render_template,request,url_for
import pandas as pd
import numpy as np
from prophet import Prophet

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexhome.html")

@app.route("/home", methods=['POST'])
def home():
    return render_template("indexhome.html")

@app.route('/predictalcohol', methods = ['POST'])  
def predictalcohol():
	return render_template("indexalcohol.html")  

@app.route('/predicttraffic', methods = ['POST'])  
def predicttraffic():
	return render_template("indextraffic.html")  

@app.route('/predictescape', methods = ['POST'])  
def predictescape():
	return render_template("indexescape.html")  


@app.route("/predict", methods=['POST'])
def predict():
    df_meta = pd.read_csv('210619monatszahlenjuni2021monatszahlen2106verkehrsunfaelle.csv')
    df_meta = df_meta[df_meta.MONAT != 'Summe'] # Drop unnecessary rows
    df_meta = df_meta.sort_values(by ='MONAT' , ascending=True) # Sort values by time
    df_meta_1 = df_meta['MONAT'].str.extract('.*(\d{2})', expand = False) 
    df_meta = df_meta.assign(MONAT=df_meta_1[:]) 
    df_meta["MONAT"] = pd.to_numeric(df_meta["MONAT"])
    df_meta[['MONATSZAHL', 'AUSPRAEGUNG']] = df_meta[['MONATSZAHL', 'AUSPRAEGUNG']].astype(pd.StringDtype()) 
    df_meta["Day"] = 11
    dict = {'JAHR': 'Year','MONAT': 'Month'}
    df_meta.rename(columns=dict, inplace=True)
    df_meta['ds']=pd.to_datetime(df_meta[['Year', 'Month', 'Day']])
    df_meta.drop(['VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT', 'ZWOELF_MONATE_MITTELWERT', 'Day'],axis=1 ,inplace=True)
    df_meta = df_meta.rename(columns={'WERT': 'y'}) 
    df_meta = df_meta.rename(columns={'MONATSZAHL': 'Category'})
    df_meta = df_meta.rename(columns={'AUSPRAEGUNG': 'Accident-type'})
    df_meta = df_meta.loc[(df_meta['Accident-type'] == 'insgesamt')]
    df_alk = df_meta.loc[(df_meta['Category'] == 'Alkoholunfälle')]
    m = Prophet()
    m.fit(df_alk) # alcohol accidents
    # Fitting monthly data and making monthly forecasts for the next 12 months
    future = m.make_future_dataframe(periods=12, freq='30d')
    forecast = m.predict(future)
    #print(forecast[['ds','yhat']].tail(12))
    df = forecast[['ds', 'yhat']]
    df['year'] = pd.DatetimeIndex(df['ds']).year
    df['month'] = pd.DatetimeIndex(df['ds']).month
    df=df.query('year == 2021')
    df=df.drop(['ds'], axis = 1)
    df=df.drop(['year'], axis = 1)
    df1=df.query('month==1').values
    df2=df.query('month==2').values
    df3=df.query('month==3').values
    df4=df.query('month==4').values
    df5=df.query('month==5').values
    df6=df.query('month==6').values
    df7=df.query('month==7').values
    df8=df.query('month==8').values
    df9=df.query('month==9').values
    df10=df.query('month==10').values
    df11=df.query('month==11').values
    df12=df.query('month==12').values
    P1=df1[0]
    P2=df2[0]
    P3=df3[0]
    P4=df4[0]
    P5=df5[0]
    P6=df6[0]
    P7=df7[0]
    P8=df8[0]
    P9=df9[0]
    P10=df10[0]
    P11=df11[0]
    P12=df12[0]
    P1=P1[0]
    P2=P2[0]
    P3=P3[0]
    P4=P4[0]
    P5=P5[0]
    P6=P6[0]
    P7=P7[0]
    P8=P8[0]
    P9=P9[0]
    P10=P10[0]
    P11=P11[0]
    P12=P12[0]
    
    print(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12)

    if request.method == 'POST':
        comment = request.form['comment']
        user_month = [comment]
        user_month = int(user_month[0])

        print(user_month)
        result_alcohol = 0
        if user_month==1:
            result_alcohol=P1
        elif user_month==2:
            result_alcohol=P2
        elif user_month==3:
            result_alcohol=P3
        elif user_month==4:
            result_alcohol=P4
        elif user_month==5:
            result_alcohol=P5
        elif user_month==6:
            result_alcohol=P6
        elif user_month==7:
            result_alcohol=P7
        elif user_month==8:
            result_alcohol=P8
        elif user_month==9:
            result_alcohol=P9
        elif user_month==10:
            result_alcohol=P10
        elif user_month==11:
            result_alcohol=P11
        elif user_month==12:
            result_alcohol=P12
        else:
            result_alcohol="Please enter number between 1 (January) and 12 (December)"

        my_prediction = result_alcohol
    return render_template("resultsalcohol.html", prediction=my_prediction, comment=comment)


@app.route("/predicttraffic2", methods=['POST'])
def predicttraffic2():
    df_meta = pd.read_csv('210619monatszahlenjuni2021monatszahlen2106verkehrsunfaelle.csv')
    df_meta = df_meta[df_meta.MONAT != 'Summe'] # Drop unnecessary rows
    df_meta = df_meta.sort_values(by ='MONAT' , ascending=True) # Sort values by time
    df_meta_1 = df_meta['MONAT'].str.extract('.*(\d{2})', expand = False) 
    df_meta = df_meta.assign(MONAT=df_meta_1[:]) 
    df_meta["MONAT"] = pd.to_numeric(df_meta["MONAT"])
    df_meta[['MONATSZAHL', 'AUSPRAEGUNG']] = df_meta[['MONATSZAHL', 'AUSPRAEGUNG']].astype(pd.StringDtype()) 
    df_meta["Day"] = 11
    dict = {'JAHR': 'Year','MONAT': 'Month'}
    df_meta.rename(columns=dict, inplace=True)
    df_meta['ds']=pd.to_datetime(df_meta[['Year', 'Month', 'Day']])
    df_meta.drop(['VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT', 'ZWOELF_MONATE_MITTELWERT', 'Day'],axis=1 ,inplace=True)
    df_meta = df_meta.rename(columns={'WERT': 'y'}) 
    df_meta = df_meta.rename(columns={'MONATSZAHL': 'Category'})
    df_meta = df_meta.rename(columns={'AUSPRAEGUNG': 'Accident-type'})
    df_meta = df_meta.loc[(df_meta['Accident-type'] == 'insgesamt')]
    df_verkehr = df_meta.loc[(df_meta['Category'] == 'Verkehrsunfälle')]
    m = Prophet()
    m.fit(df_verkehr) # traffic accidents
    # Fitting monthly data and making monthly forecasts for the next 12 months
    future = m.make_future_dataframe(periods=12, freq='30d')
    forecast = m.predict(future)
    #print(forecast[['ds','yhat']].tail(12))
    df = forecast[['ds', 'yhat']]
    df['year'] = pd.DatetimeIndex(df['ds']).year
    df['month'] = pd.DatetimeIndex(df['ds']).month
    df=df.query('year == 2021')
    df=df.drop(['ds'], axis = 1)
    df=df.drop(['year'], axis = 1)
    df1=df.query('month==1').values
    df2=df.query('month==2').values
    df3=df.query('month==3').values
    df4=df.query('month==4').values
    df5=df.query('month==5').values
    df6=df.query('month==6').values
    df7=df.query('month==7').values
    df8=df.query('month==8').values
    df9=df.query('month==9').values
    df10=df.query('month==10').values
    df11=df.query('month==11').values
    df12=df.query('month==12').values
    P1=df1[0]
    P2=df2[0]
    P3=df3[0]
    P4=df4[0]
    P5=df5[0]
    P6=df6[0]
    P7=df7[0]
    P8=df8[0]
    P9=df9[0]
    P10=df10[0]
    P11=df11[0]
    P12=df12[0]
    P1=P1[0]
    P2=P2[0]
    P3=P3[0]
    P4=P4[0]
    P5=P5[0]
    P6=P6[0]
    P7=P7[0]
    P8=P8[0]
    P9=P9[0]
    P10=P10[0]
    P11=P11[0]
    P12=P12[0]
    
    print(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12)

    if request.method == 'POST':
        comment = request.form['comment']
        user_month = [comment]
        user_month = int(user_month[0])

        print(user_month)
        result_traffic = 0
        if user_month==1:
            result_traffic=P1
        elif user_month==2:
            result_traffic=P2
        elif user_month==3:
            result_traffic=P3
        elif user_month==4:
            result_traffic=P4
        elif user_month==5:
            result_traffic=P5
        elif user_month==6:
            result_traffic=P6
        elif user_month==7:
            result_traffic=P7
        elif user_month==8:
            result_traffic=P8
        elif user_month==9:
            result_traffic=P9
        elif user_month==10:
            result_traffic=P10
        elif user_month==11:
            result_traffic=P11
        elif user_month==12:
            result_traffic=P12
        else:
            result_traffic="Please enter number between 1 (January) and 12 (December)"

        my_prediction = result_traffic
    return render_template("resultstraffic.html", prediction=my_prediction, comment=comment)

@app.route("/predictescape2", methods=['POST'])
def predictescape2():
    df_meta = pd.read_csv('210619monatszahlenjuni2021monatszahlen2106verkehrsunfaelle.csv')
    df_meta = df_meta[df_meta.MONAT != 'Summe'] # Drop unnecessary rows
    df_meta = df_meta.sort_values(by ='MONAT' , ascending=True) # Sort values by time
    df_meta_1 = df_meta['MONAT'].str.extract('.*(\d{2})', expand = False) 
    df_meta = df_meta.assign(MONAT=df_meta_1[:]) 
    df_meta["MONAT"] = pd.to_numeric(df_meta["MONAT"])
    df_meta[['MONATSZAHL', 'AUSPRAEGUNG']] = df_meta[['MONATSZAHL', 'AUSPRAEGUNG']].astype(pd.StringDtype()) 
    df_meta["Day"] = 11
    dict = {'JAHR': 'Year','MONAT': 'Month'}
    df_meta.rename(columns=dict, inplace=True)
    df_meta['ds']=pd.to_datetime(df_meta[['Year', 'Month', 'Day']])
    df_meta.drop(['VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT', 'ZWOELF_MONATE_MITTELWERT', 'Day'],axis=1 ,inplace=True)
    df_meta = df_meta.rename(columns={'WERT': 'y'}) 
    df_meta = df_meta.rename(columns={'MONATSZAHL': 'Category'})
    df_meta = df_meta.rename(columns={'AUSPRAEGUNG': 'Accident-type'})
    df_meta = df_meta.loc[(df_meta['Accident-type'] == 'insgesamt')]
    df_flucht = df_meta.loc[(df_meta['Category'] == 'Fluchtunfälle')]
    m = Prophet()
    m.fit(df_flucht) # ESCAPE accidents
    # Fitting monthly data and making monthly forecasts for the next 12 months
    future = m.make_future_dataframe(periods=12, freq='30d')
    forecast = m.predict(future)
    #print(forecast[['ds','yhat']].tail(12))
    df = forecast[['ds', 'yhat']]
    df['year'] = pd.DatetimeIndex(df['ds']).year
    df['month'] = pd.DatetimeIndex(df['ds']).month
    df=df.query('year == 2021')
    df=df.drop(['ds'], axis = 1)
    df=df.drop(['year'], axis = 1)
    df1=df.query('month==1').values
    df2=df.query('month==2').values
    df3=df.query('month==3').values
    df4=df.query('month==4').values
    df5=df.query('month==5').values
    df6=df.query('month==6').values
    df7=df.query('month==7').values
    df8=df.query('month==8').values
    df9=df.query('month==9').values
    df10=df.query('month==10').values
    df11=df.query('month==11').values
    df12=df.query('month==12').values
    P1=df1[0]
    P2=df2[0]
    P3=df3[0]
    P4=df4[0]
    P5=df5[0]
    P6=df6[0]
    P7=df7[0]
    P8=df8[0]
    P9=df9[0]
    P10=df10[0]
    P11=df11[0]
    P12=df12[0]
    P1=P1[0]
    P2=P2[0]
    P3=P3[0]
    P4=P4[0]
    P5=P5[0]
    P6=P6[0]
    P7=P7[0]
    P8=P8[0]
    P9=P9[0]
    P10=P10[0]
    P11=P11[0]
    P12=P12[0]
    
    print(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12)

    if request.method == 'POST':
        comment = request.form['comment']
        user_month = [comment]
        user_month = int(user_month[0])

        print(user_month)
        result_escape = 0
        if user_month==1:
            result_escape=P1
        elif user_month==2:
            result_escape=P2
        elif user_month==3:
            result_escape=P3
        elif user_month==4:
            result_escape=P4
        elif user_month==5:
            result_escape=P5
        elif user_month==6:
            result_escape=P6
        elif user_month==7:
            result_escape=P7
        elif user_month==8:
            result_escape=P8
        elif user_month==9:
            result_escape=P9
        elif user_month==10:
            result_escape=P10
        elif user_month==11:
            result_escape=P11
        elif user_month==12:
            result_escape=P12
        else:
            result_escape="Please enter number between 1 (January) and 12 (December)"

        my_prediction = result_escape
    return render_template("resultsescape.html", prediction=my_prediction, comment=comment)

#if __name__ == '__main__':
#    app.run(host="127.0.0.1",port=8080,debug=True)
