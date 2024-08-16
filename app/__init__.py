from flask import Flask
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__, template_folder='templates')

    load_dotenv()
    app.config['TMDB_API_KEY'] = os.getenv('TMDB_API_KEY')

    with app.app_context():
        import pandas as pd
        import numpy as np
        
        global processed_df
        global similarity

        processed_df = pd.read_pickle('data/processed_df.pkl')
        similarity = np.load('data/similarity.npy')

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
