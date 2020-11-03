from flask import Flask, render_template
from sqlalchemy import create_engine

#path to sql database
#database_path = 'postgres+psycopg2://postgres:postgres:@http://127.0.0.1:54491/'

#create an engine to the database
#engine = create_engine(f"sqlite:///{database_path}")

state_list = ['Alabama','Alaska','Arizona'
,'Arkansas','California','Colorado','Connecticut','Delaware','Florida'
,'Georgia','Hawaii','Idaho','IllinoisIndiana','Iowa','Kansas','Kentucky','Louisiana','Maine'
,'Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri'
,'Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina'
,'North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania', 'Rhode Island','South Carolina','South Dakota'
,'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'] 

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/analytics")
def analytics():
  return render_template("analytics.html")


if __name__ == "__main__":
  app.run(debug=True)
