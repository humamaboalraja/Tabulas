import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
   app = Flask(__name__, instance_relative_config=True,
                template_folder='templates')

   try:
      os.makedirs(app.instance_path)
   except OSError:
      pass

    # a simple page that says hello
   @app.route('/')
   def hello():
      return render_template('index.html')

   return app
