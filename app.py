from flask import Flask
app = Flask(__name__)

import pandas as pd
#import numpy as np
from dotenv import load_dotenv    # pip install python-dotenv
import kayen
import felix
import susanne

load_dotenv()

#df = pd.read_csv("NEVO2021.csv", sep="|")
#df = pd.read_csv("clean_data.csv")
df_import = pd.read_csv("clean_data_allergenen.csv", sep="|")
df = df_import[(df_import.Voedingsmiddelgroep != "Samengestelde gerechten")]


## Flask
#http://localhost:5000/   #flask run
@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

#http://localhost:5000/   #flask run
@app.route("/kayen")
def hellokayen():
    return kayen.goedenmorgen()   

@app.route("/felix")
def hellofelix():
    return felix.goedenmorgen() 

@app.route("/susanne")
def hellosusanne():
    return susanne.goedenmorgen()  

@app.route("/ingredienten/exactnaam/<ingredient>")
def geefingredient(ingredient):
    #return ingredient
    df_new = df.loc[df['Voedingsmiddelnaam/Dutch food name'] == ingredient]
    return df_new.to_json(orient='index')
    #return str(df_new["Voedingsmiddelnaam/Dutch food name"][0] + ": " + df_new["Hoeveelheid/Quantity"][0] + " " + str(df_new["ENERCC (kcal)"][0]) + ' kcal')
    

@app.route("/ingredienten/deelnaam/<ingredient>")
def geefdeelingredient(ingredient):
    ingredient = str.lower(ingredient)
    df_new = df.loc[df['Voedingsmiddelnaam/Dutch food name'].str.lower().str.contains(ingredient)]
    return df_new.to_json(orient='index')
    #return df_new.iloc[0].to_json(orient='index') # eerste terug geven


#    @app.route('/get/')
#def get_test():
#    cur = get_db().cursor()
#    cur.execute('SELECT * FROM test')
#    return jsonify(cur.fetchall())
    

