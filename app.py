import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask_cors import CORS
from flask import render_template

engine=create_engine("sqlite:///assets/data/steam_games.db")

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return(f"Steam data<br/>"
           f"available routes:<br/>"
           f"/api/v1.0/sample<br/>"
           f"/api/v1.0/Number_of_Players_per_State<br/>"
           f"/api/v1.0/Highest_rated_game<br/>"
           )

@app.route("/api/v1.0/sample")
def sample():
    results=engine.execute('select * from games_with_score').fetchmany(10)
    # return_string=''
    # for each_row in list(results): 
    #     for each_value in each_row: 
    #         return_string=return_string+str(each_value)
    returned_results=[list(result) for result in results]
    return jsonify(returned_results)

@app.route("/api/v1.0/Number_of_Players_per_State")
def Number_of_Players_per_State():
    state_results=engine.execute('select * from state_sales2').fetchall()
    # return_string=''
    # for each_row in list(results): 
    #     for each_value in each_row: 
    #         return_string=return_string+str(each_value)
    returned_results_state=[list(state_result) for state_result in state_results]
    return jsonify(returned_results_state)

@app.route("/api/v1.0/Highest_rated_game")
def Highest_rated_game():
    steam_results=engine.execute('select * from steam_data').fetchall()
    # return_string=''
    # for each_row in list(results): 
    #     for each_value in each_row: 
    #         return_string=return_string+str(each_value)
    returned_results_steam=[list(steam_result) for steam_result in steam_results]
    return jsonify(returned_results_steam)

if __name__=="__main__":
    app.run(debug=True)