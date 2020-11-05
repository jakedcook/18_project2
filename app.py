from flask import Flask, render_template, request, flash, redirect
import cgi, cgitb
from actions import sql_data_from_input
import json

state_list = ['Alabama','Alaska','Arizona'
,'Arkansas','California','Colorado','Connecticut','Delaware','Florida'
,'Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine'
,'Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri'
,'Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina'
,'North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania', 'Rhode Island','South Carolina','South Dakota'
,'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'] 

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/", methods=['POST'])
def action_page():
  searchterm = request.form['state_name']
  if searchterm in state_list:
    result = sql_data_from_input(searchterm)
    return render_template('analytics.html', data=result)
  else: 
    return render_template("index.html")

@app.route("/analytics")
def analytics():
  return render_template("analytics.html")


if __name__ == "__main__":
  app.run(debug=True)
