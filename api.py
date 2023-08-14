# from flask import Flask,render_template, redirect, session, request, flash, jsonify, make_response,url_for
import weather 
import requests
import json

# app = Flask(__name__)
# @app.route('/getData/sensores/<string:device>')

def getDeviceData(device):
    
    if device == "puz00001": #Demo plantitas
        r1 = requests.post('http://www.m2m-iot.cc:8081/query', json={
        "action_cmd":"query_device_currentdata2",
        "seq_id ":"1",
        "body":{"deviceid":"puz00001",
                "tid":"25bb138b97ff6a5ab97674c07485c3f8"},
        "version":"1.0"
        })
        response = r1.json()
        Data_sensor={
            "humedad":response['body']['datadict']['RG0']['value'],
            "temperatura":response['body']['datadict']['RG1']['value']
        }
        return Data_sensor
    if device == "puz00002": #Demo plantitas
        r1 = requests.post('http://www.m2m-iot.cc:8081/query', json={
        "action_cmd":"query_device_currentdata2",
        "seq_id ":"1",
        "body":{"deviceid":"puz00002",
                "tid":"25bb138b97ff6a5ab97674c07485c3f8"},
        "version":"1.0"
        })
        response = r1.json()
        Data_sensor={
            'humedad' : response['body']['datadict']['RG0']['value'],
            'temperatura' : response['body']['datadict']['RG1']['value'],
            'conductividad': response['body']['datadict']['RG2']['value'],
            'PH': response['body']['datadict']['RG3']['value'],
            'N': response['body']['datadict']['RG4']['value'],
            'P': response['body']['datadict']['RG5']['value'],
            'K': response['body']['datadict']['RG6']['value']
        }
        return Data_sensor
    if device == "puz00003": #Sr. Bader
        r1 = requests.post('http://www.m2m-iot.cc:8081/query', json={
        "action_cmd":"query_device_currentdata2",
        "seq_id ":"1",
        "body":{"deviceid":"puz00003",
                "tid":"25bb138b97ff6a5ab97674c07485c3f8"},
        "version":"1.0"
        })
        response = r1.json()
        Data_sensor={
            'DI0' : response['body']['datadict']['DI0']['state']
        }
        return Data_sensor

# @app.route('/getData/clima/<string:accion>')
# def getWeatherData(accion):
#     if accion == "get_current":
#         Data = weather.get_current()
#         return Data
#     if accion == "get_history_temp":
#         Data,horas = weather.get_history_temp()
#         return {"Temperatura": Data,
#                 "Horas": horas}
#     if accion == "get_forecast":
#         dia,horas = weather.get_forecast()
#         return {"Dias": dia,
# #                  "horas_x_dia": horas}

# if __name__=="__main__":
#     app.run(debug=True, host='192.168.100.10',port=4000)
#     # app.run(debug=True,port=4000)