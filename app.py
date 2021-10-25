import os, shutil

from flask import Flask, render_template, request, redirect, url_for
import osmnx as ox
import heapq
import random
import sys 

from src import dijkstra, astar
from haversine import haversine, Unit


def create_app(test_config=None):
    # create and configure the app
   app = Flask(__name__, instance_relative_config=True,
                template_folder='templates')

   
   app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

   try:
      os.makedirs(app.instance_path)
   except OSError:
      pass

    # a simple page that says hello
   @app.route('/')
   def hello():
      return render_template('index.html')
   
   @app.route('/compare', methods=['POST', 'GET'])
   def compare():
      if request.method == 'POST':
         ox.config(use_cache=True)

         startingPoint = ox.geocode(request.form['startingPoint'])
         endingPoint = ox.geocode(request.form['endingPoint'])
         astarRouteColor = request.form['astarRouteColor']
         astarBgColor = request.form['astarBgColor']
         dijkstraRouteColor = request.form['dijkstraRouteColor']
         dijkstraBgColor = request.form['dijkstraBgColor']

         north, east, south, west = 0, 0, 0, 0
         if startingPoint[0] >= endingPoint[0]:
            north, south = startingPoint[0], endingPoint[0]
         else:
            north, south = endingPoint[0], startingPoint[0]
         if startingPoint[1] >= endingPoint[1]:
            east, west = startingPoint[1], endingPoint[1]
         else:
            east, west = endingPoint[1], startingPoint[1]

         G = ox.graph_from_bbox(north + 0.01, south - 0.01, east + 0.01, west - 0.01, network_type="drive", simplify=True)
         orig = ox.get_nearest_node(G, startingPoint)
         destination = ox.get_nearest_node(G, endingPoint)

         astarGraphObject = astar.astarGraph(G)
         dijkstraGraphObject = dijkstra.dijkstraGraph(G)

         astarPath, astarVerticesExplored, astarEdgesExplored, astarCost = astarGraphObject.astar(orig, destination)
         astarResult = f"Distance from [{request.form['startingPoint']} → {request.form['endingPoint']}] is {str(astarCost)} meters away 🎉 \n  A* 🗾 calculated/explored {str(astarVerticesExplored)} vertices and {str(astarEdgesExplored)} edges."
         fig, ax = ox.plot_graph_route(G, astarPath, route_linewidth=4, node_size=0, route_color=astarRouteColor, save=True, bgcolor=astarBgColor, edge_color="#161616", filepath="static/img/astar.jpg", show=False, close=True)

         dijkstraPath, dijkstraVerticesExplored, dijkstraEdgesExplored, dijkstraCost = dijkstraGraphObject.dijkstra(orig, destination)
         dijkstraResult = f"Distance from [{request.form['startingPoint']} → {request.form['endingPoint']}] is {str(dijkstraCost)} meters away 🎉 | \n Dijkstra's 🗾 calculated/explored {str(dijkstraVerticesExplored)} vertices and {str(dijkstraEdgesExplored)} edges."
         fig, ax = ox.plot_graph_route(G, dijkstraPath, route_linewidth=4, node_size=0, route_color=dijkstraRouteColor, save=True, bgcolor=dijkstraBgColor, edge_color="#161616", filepath="static/img/dijkstra.jpg", show=False, close=True)
         # shutil.rmtree('cache')

         return render_template('index.html', astar="astar.jpg", dijkstra="dijkstra.jpg", astarResult = astarResult, dijkstraResult = dijkstraResult, request = request)

   return app

   if __name__ == "__main__":
      app.run(host="0.0.0.0")