from flask import Flask
app = Flask(__name__)

import pandas as pd
import numpy as np
from dotenv import load_dotenv    # pip install python-dotenv
import kayen
import felix


load_dotenv()

#df = pd.read_csv("NEVO2021.csv", sep="|")
#df = pd.read_csv("clean_data.csv")
df = pd.read_csv("clean_data_allergenen.csv", sep="|")

## Test in Python 
#print(str(df.columns))   #print all column names
#print(np.unique(df['Voedingsmiddelnaam/Dutch food name'])) #print all unique ingredients

df_new = df.loc[df['Voedingsmiddelnaam/Dutch food name'] == 'Campari']
print(df_new)
#print(str(df_new["Voedingsmiddelnaam/Dutch food name"][0] + ": " + df_new["Hoeveelheid/Quantity"][0] + " " + str(df_new["ENERCC (kcal)"][0]) + ' kcal'))
#print(df_new["Voedingsmiddelnaam/Dutch food name"]+": "+df_new["Hoeveelheid/Quantity"]+" "+str(df_new["ENERCC (kcal)"][0])+" kcal" )


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

@app.route("/ingredienten/exactnaam/<ingredient>")
def geefingredient(ingredient):
    #return ingredient
    df_new = df.loc[df['Voedingsmiddelnaam/Dutch food name'] == ingredient]
    return df_new.to_json(orient='index')
    #return str(df_new["Voedingsmiddelnaam/Dutch food name"][0] + ": " + df_new["Hoeveelheid/Quantity"][0] + " " + str(df_new["ENERCC (kcal)"][0]) + ' kcal')
    
    #return "Ik zoek het ingredient " + ingredient
    #return str(np.unique(df['Voedingsmiddelnaam/Dutch food name'])) 


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
    

