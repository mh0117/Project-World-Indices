from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
import json

# DATABASE_URL = 'postgresql://postgres:postgres@localhost/mariam'
DATABASE_URL = 'postgres://sowmjntrzdsftr:883ebb9c4b9f387fbc875a06eb1defe4353a6371903b17952f4ce8b1023c9d3a@ec2-54-83-192-245.compute-1.amazonaws.com:5432/dbae2u93isa3ec'

def create_app():
    app = Flask(
        __name__,
        static_folder='public',
        static_url_path='',
        template_folder='templates'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    engine = db.get_engine()

    @app.route('/')
    def index():
        return render_template('./index.html')

    @app.route('/data')
    def data():
        data = pd.read_sql_query('select * from population_data', engine)
        data = data.to_json(orient='records')
        return jsonify(json.loads(data))

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
