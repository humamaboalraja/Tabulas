import os, shutil

from flask import Flask, render_template, request, redirect, url_for
import osmnx as ox
import heapq
import random
import sys 

from data.PriorityQueue import PriorityQueue
from src.Dijkstra import dijkstraGraph
from src.Astar import astarGraph
from haversine import haversine, Unit





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
   
   @app.route('/compare', methods=['POST'])
   def compare():
      if request.method == 'POST':
         ox.config(use_cache=True)

         startingPoint = ox.geocode(request.form['startingPoint'])
         endingPoint = ox.geocode(request.form['endingPoint'])
         astarRouteColor = request.form['astarRouteColor']
         astarBgColor = request.form['astarBgColor']
         dijkstraRouteColor = request.form['dijkstraRouteColor']
         dijkstraBgColor = request.form['dijkstraBgColor']


         return render_template('index.html', astar="astar.jpg", dijkstra="dijkstra.jpg")

   return app
