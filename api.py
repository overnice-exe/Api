from flask import *
import json, time, requests
from mcuuid import MCUUID
import re
import os
from mcuuid.tools import is_valid_minecraft_username
from colorama import Fore
from gevent.pywsgi import WSGIServer

from gevent import pywsgi
os.system("cls")

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='favicon.ico')


@app.route('/', methods=['GET'])
def home_page():
    ##   <h3>/droptime/(api key)/(player name)</h3>
    text = '<h1>Enchanted api</h1>\n<h2>welcome user to the enchanted api!\navalable aliasses : </h2>\n<h3>/player/(api key)/(player name)</h3>\n..\n\n<h3>you can get the api key in the disocrd server. go to bot commands and type : e!api key</h3>\n<h2>Disocrd : </h2><a href="https://discord.gg/257AE6wcsG">Join!</a>'

    #return text

    return text





@app.route('/player/<key>/<user_query>', methods=['GET'])
def player_page(key, user_query):
    with open("key.txt", "r") as X:
        keys = X.read().lower()
        if(str(key) in keys):
            

            #user_query = str(request.args.get('player'))
            #user_query = str(user_query)




            print(f"getting info on playername {Fore.GREEN}{user_query}{Fore.WHITE}")
            if not(user_query):
                text2 = "pls enter a name after the ?player="
                return text2

            
            


            player = MCUUID(name=f"{str(user_query)}")
            is_good_name = is_valid_minecraft_username(f'{user_query}')
            if(is_good_name == False):
                data_set = {'valid': f'{is_good_name}'}
                json_dump = json.dumps(data_set)


                return json_dump



            uuid = player.uuid
            nameslist = player.names
            nameslist = str(nameslist)
            nameslist1 = nameslist.replace("{", "").replace("}", "").replace("'", "")
            findre = re.search("0: ", nameslist1)
            nameslist2 = nameslist1.replace(str(findre), "")

            data_set = {'valid': f'{is_good_name}', 'name': f'{user_query}','names': f'{nameslist2}','uuid': f'{uuid}'}
            json_dump = json.dumps(data_set)

            return json_dump
        else:
            error = "error"
            return error



@app.route('/droptime/<key>/<user_query>', methods=['GET'])
def droptime_page(key, user_query):
    with open("key.txt", "r") as X:
        keys = X.read().lower()
        if(str(key) in keys):

    #user_query = str(request.args.get('player'))
    #user_query = str(user_query)




            print(f"getting info on playername {Fore.GREEN}{user_query}{Fore.WHITE}")
            if not(user_query):
                text2 = "pls enter a name after the ?player="
                return text2

            
            


            player = MCUUID(name=f"{str(user_query)}")
            is_good_name = is_valid_minecraft_username(f'{user_query}')
            if(is_good_name == False):
                data_set = {'valid': f'{is_good_name}'}
                json_dump = json.dumps(data_set)


                return json_dump



            
        
        
        
        
            data = requests.get(f"http://api.coolkidmacho.com/droptime/wow").json()

            data = data['UNIX']
            data_set = {'valid': f'{is_good_name}', 'name': f'{user_query}','Droptime': f'{data}'}
            json_dump = json.dumps(data_set)

            return json_dump


@app.route('/info', methods=['GET'])
def info_page():

    return redirect("https://pastebin.com/raw/uG5PnGUt", code=302)



if __name__ == '__main__':
    # 192.168.2.16
    # 192.168.2.2
    server = pywsgi.WSGIServer(('192.168.2.2', 80), app)
    server.serve_forever()
    #app.run(host='0.0.0.0', port=80)