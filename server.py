from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import seaborn as sb
import plotly
import plotly.graph_objs as go
# Data dari flask di kirim ke browser dalam bentuk json
import json
import joblib

app = Flask(__name__)

# Sumber data
SBA = pd.read_csv('SBAnational.csv')
SBA = SBA.head(100)

# # # # # # # # # #
# HISTOGRAM & BOX #
# # # # # # # # # #

def category_plot(cat_plot = 'histoplot', cat_x = 'NewExist', cat_y = 'Term', estimator ='count', hue='MIS_Status'):
    
    if cat_plot == 'histoplot':
        data = []

        for val in SBA[hue].unique(): # [No, Yes]
            hist = go.Histogram(
                        x = SBA[SBA[hue] == val ][cat_x],
                        y = SBA[SBA[hue] == val ][cat_y],
                        histfunc=estimator,
                        name= val
                    )
            
            data.append(hist)

        title = 'Histogram'
    else :
        data = []

        for val in SBA[hue].unique(): # [No, Yes]
            hist = go.Box(
                        x = SBA[SBA[hue] == val ][cat_x],
                        y = SBA[SBA[hue] == val ][cat_y],
                        name= val
                    )
            
            data.append(hist)

        title = 'Box'

    layout = go.Layout(
        title=title,
        title_x=0.5,
        xaxis={"title" : cat_x},
        yaxis=dict(title=cat_y),
        boxmode='group'
    )

    final = {"data" : data, "layout" : layout}

    graphJSON = json.dumps(final, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/')
def index():
    plot = category_plot()

    # list dropdown
    list_plot = [('histoplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('NewExist', 'NewExist'), ('RevLineCr', 'RevLineCr'), ('LowDoc', 'LowDoc'), ('MIS_Status', 'MIS_Status')]
    list_y = [('Term', 'Term'), ('GrAppv', 'GrAppv'), ('SBA_Appv', 'SBA_Appv')]
    list_estimator = [('count', 'Count'), ('sum', 'Sum'),('avg','Average'), ('min', 'Minimum'), ('max', 'Maximum')]

    return render_template(
        'category.html', 
        plot=plot, 
        focus_plot='histoplot', 
        focus_x='NewExist', 
        focus_y='Term', 
        focus_estimator='count',
        drop_plot = list_plot,
        drop_x = list_x,
        drop_y = list_y,
        drop_estimator = list_estimator,
        drop_hue = list_x
    )

@app.route('/cat_fn')
def cat_fn():
    cat_plot = request.args.get('cat_plot') # histoplot
    cat_x = request.args.get('cat_x') # NewExist
    cat_y = request.args.get('cat_y') # Term
    estimator = request.args.get('estimator') # avg
    hue = request.args.get('hue') # MIS_Status

    # Ketika kita klik menu 'Histogram & Box' di Navigasi
    if cat_plot == None and cat_x == None and cat_y == None and estimator == None and hue == None:
        cat_plot = 'histoplot'
        cat_x = 'NewExist'
        cat_y = 'Term'
        estimator = 'count'
        hue = 'MIS_Status'

    # Ketika kita pindah dari boxplot (disabled) ke histogram
    if estimator == None:
        estimator = 'count'

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)

    # list dropdown
    list_plot = [('histoplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('NewExist', 'NewExist'), ('RevLineCr', 'RevLineCr'), ('LowDoc', 'LowDoc'), ('MIS_Status', 'MIS_Status')]
    list_y = [('Term', 'Term'), ('GrAppv', 'GrAppv'), ('SBA_Appv', 'SBA_Appv')]
    list_estimator = [('count', 'Count'), ('sum', 'Sum'),('avg','Average'), ('min', 'Minimum'), ('max', 'Maximum')]
                                                                                            
    return render_template(
        'category.html', 
        plot=plot, 
        focus_plot=cat_plot, 
        focus_x=cat_x, 
        focus_y=cat_y, 
        focus_estimator=estimator,
        focus_hue = hue,
        drop_plot = list_plot,
        drop_x = list_x,
        drop_y = list_y,
        drop_estimator = list_estimator,
        drop_hue = list_x
    )


# # # # # #
# SCATTER # 
# # # # # #

def scatter_plot(cat_x, cat_y):

    # membuat plot, nama variable tidak harus 'data'
    data_source = [
        go.Scatter(
            x = SBA[cat_x],
            y = SBA[cat_y],
            mode = 'markers'
        )
    ]

    # membuat layout, nama variable tidak harus 'layout'
    layout_source = go.Layout(
        title='Scatter',
        title_x= 0.5,
        xaxis = {"title" : cat_x},
        yaxis = {"title" : cat_y}
    )

    # Gabungkan antara plot dengan layout
    # variable yang menyimpan dictionary tidak harus final
    # dict harus memiliki key 'data' dan 'layout
    final = {"data" : data_source, "layout" : layout_source}

    # hasil json yang akan dikirim tidak harus menggunakan 'graphJSON'
    graphJSON = json.dumps(final, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/scatt_fn')
def scatt_fn():
    # Memilih dari menu dropdown
    # Keduanya akan bernilai None hanya ketika kita mengunjungi via 'Scatter' menu di navbar
    cat_x = request.args.get('cat_x')
    cat_y = request.args.get('cat_y')

    # Jika kita klick menu 'Scatter' pada navbar, keduanya akan bernilai None
    if cat_x == None and cat_y == None:
        cat_x = 'Term'
        cat_y = 'GrAppv'

    plot = scatter_plot(cat_x, cat_y)
    
    # Kirim ke browser
    return render_template('scatter.html', plot=plot, focus_x=cat_x, focus_y=cat_y)


# # # #
# PIE #
# # # #

def pie_plot(hue):

    # result : list of tupple dari penghitungan banyak data secara unique 
    result = SBA[hue].value_counts()

    labels_source = []
    values_source = []

    for item in result.iteritems():
        labels_source.append(item[0])
        values_source.append(item[1])

    data_source = [
        go.Pie(
            labels=labels_source,
            values=values_source
        )
    ]

    layout_source = go.Layout(
        title='Pie',
        title_x=0.5
    )

    final = {"data" : data_source, "layout" : layout_source}

    # hasil json yang akan dikirim tidak harus menggunakan 'graphJSON'
    graphJSON = json.dumps(final, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/pie_fn')
def pie_fn():
    hue_source = request.args.get('hue')

    # Saat diakses melalui link, hue_sorce akan bernilai None
    if hue_source == None:
        hue_source = 'NewExist'

    plot_source = pie_plot(hue_source)

    return render_template('pie.html', plot=plot_source, focus_hue=hue_source)

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/SBA_Loan_Result', methods=["POST", "GET"])
def SBA_Loan_predict():
    if request.method == "POST":
        input = request.form
        Term = float(input['Term'])
        NewExist = float(input['NewExist'])
        if NewExist == 1:
            NewExistRes = 'Existing Business'
        else:
            NewExistRes = 'New Business'
        GrAppv = float(input['GrAppv'])
        SBA_Appv = float(input['SBA_Appv'])
        RevLineCr = float(input['RevLineCr'])
        if RevLineCr == 1:
            RevLineCrRes = 'Yes'
        else:
            RevLineCrRes = 'No'
        LowDoc = float(input['LowDoc'])
        if LowDoc == 1:
            LowDocRes = 'Yes'
        else:
            LowDocRes = 'No'
        NAICS = input['NAICS']
        NAICS_11 = 0
        NAICS_21 = 0
        NAICS_22 = 0
        NAICS_23 = 0
        NAICS_31_33 = 0
        NAICS_42 = 0
        NAICS_44_45 = 0
        NAICS_48_49 = 0
        NAICS_51 = 0
        NAICS_52 = 0
        NAICS_53 = 0
        NAICS_54 = 0
        NAICS_55 = 0
        NAICS_55 = 0
        NAICS_56 = 0
        NAICS_61 = 0
        NAICS_62 = 0
        NAICS_71 = 0
        NAICS_72 = 0
        NAICS_81 = 0
        NAICS_92 = 0
        if NAICS == '11':
            NAICS_11 += 1
            NAICSRes = 'Agriculture, forestry, fishing and hunting'
        elif NAICS == '21':
            NAICS_21 += 1
            NAICSRes = 'Mining, quarrying, and oil and gas extraction'
        elif NAICS == '22':
            NAICS_22 += 1
            NAICSRes = 'Utilities'
        elif NAICS == '23':
            NAICS_23 += 1
            NAICSRes = 'Construction'
        elif NAICS == '31-33':
            NAICS_31_33 += 1
            NAICSRes = 'Manufacturing'
        elif NAICS == '42':
            NAICS_42 += 1
            NAICSRes = 'Wholesale trade'
        elif NAICS == '44-45':
            NAICS_44_45 += 1
            NAICSRes = 'Retail trade'
        elif NAICS == '48-49':
            NAICS_48_49 += 1
            NAICSRes = 'Transportation and warehousing'
        elif NAICS == '51':
            NAICS_51 += 1
            NAICSRes = 'Information'
        elif NAICS == '52':
            NAICS_52 += 1
            NAICSRes = 'Finance and insurance'
        elif NAICS == '53':
            NAICS_53 += 1
            NAICSRes = 'Real estate and rental and leasing'
        elif NAICS == '54':
            NAICS_54 += 1
            NAICSRes = 'Professional, scientific, and technical services'
        elif NAICS == '55':
            NAICS_55 += 1
            NAICSRes = 'Management of companies and enterprises'
        elif NAICS == '56':
            NAICS_56 += 1
            NAICSRes = 'Administrative/support & waste management/remediation Service'
        elif NAICS == '61':
            NAICS_61 += 1
            NAICSRes = 'Educational services'
        elif NAICS == '62':
            NAICS_62 += 1
            NAICSRes = 'Health care and social assistance'
        elif NAICS == '71':
            NAICS_71 += 1
            NAICSRes = 'Arts, entertainment, and recreation'
        elif NAICS == '72':
            NAICS_72 += 1
            NAICSRes = 'Accommodation and food services'
        elif NAICS == '81':
            NAICS_81 += 1
            NAICSRes = 'Other services (except public administration)'
        elif NAICS == '92':
            NAICS_92 += 1
            NAICSRes = 'Public administration'

# Term, NewExist, GrAppv, SBA_Appv, RevLineCr, Lowdoc, NAICS_11
        pred = gbc.predict([[Term, NewExist, GrAppv, SBA_Appv, RevLineCr, LowDoc, NAICS_11, NAICS_21, NAICS_22,
        NAICS_23, NAICS_31_33, NAICS_42, NAICS_44_45, NAICS_48_49, NAICS_51, NAICS_52, NAICS_53, NAICS_54, NAICS_55,
        NAICS_56, NAICS_61, NAICS_62, NAICS_71, NAICS_72, NAICS_81, NAICS_92]])[0]
        
        pred_proba = gbc.predict_proba([[Term, NewExist, GrAppv, SBA_Appv, RevLineCr, LowDoc, NAICS_11, NAICS_21, NAICS_22,
        NAICS_23, NAICS_31_33, NAICS_42, NAICS_44_45, NAICS_48_49, NAICS_51, NAICS_52, NAICS_53, NAICS_54, NAICS_55,
        NAICS_56, NAICS_61, NAICS_62, NAICS_71, NAICS_72, NAICS_81, NAICS_92]])
        
        pred_and_proba = f"{round(np.max(pred_proba)*100,2)}% {'APPROVED' if pred == 1 else 'DENIED'}"

        return render_template('result.html',
        data=input, prediction=pred_and_proba, Term=input['Term'],
        NewExist=NewExistRes, GrAppv=input['GrAppv'],
        SBA_Appv=input['SBA_Appv'], RevLineCr=RevLineCrRes,
        LowDoc=LowDocRes, NAICS=NAICSRes)

if __name__ == '__main__':
    gbc = joblib.load('gbc_SBA_Loan')
    app.run(debug=True, port=4000)