"""
    Hacer un API REST que tenga la funcion de listar las carpetas y archivos
    y ordenar por tamaño o fecha
"""
# importing os module and flask framework
import os
from flask import Flask, jsonify
# importing external functions (./mymodules/utility4.py)
from myModules.utility4 import list_directory, orderByDate, orderByName, getDirectory

# creating app
app = Flask(__name__)
# obtain route with os.getcwd() function
route = os.getcwd()

# Route http://localhost:5000/api/Test_Infotech
@app.route('/api/Test_Infotech')
def apiTestInfotech():
    return jsonify({getDirectory(route): {"files" : list_directory(route)}})

# Route http://localhost:5000/api/Test_Infotech/OrderByDate
# Sort files by date
@app.route('/api/Test_Infotech/OrderByDate')
def OrderFilesByDate():
    return jsonify({"Test_Infotech": {"files": orderByDate(route)}})

# Route http://localhost:5000/api/Test_Infotech/OrderByName
# Sort files alphabetically
@app.route('/api/Test_Infotech/OrderByName')
def OrderFilesByName():
    return jsonify({"Test_Infotech": {"files": orderByName(route)}})

if __name__ == '__main__':
    app.run(debug=True)