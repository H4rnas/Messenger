import logging
import os
from flask import Flask, request
import pyfiglet
import sys

header = pyfiglet.figlet_format("MESSENGER",font='banner3-D',width=100)

if len(sys.argv) == 2:
    app = Flask(__name__)

    print(header)
    print("Listening on port {}".format(str(sys.argv[1]))

    logging.getLogger("werkzeug").disabled = True
    os.environ["WERKZEUG_RUN_MAIN"] = "True"

    messages=[]

    @app.route('/',methods=['POST'])
    def messener():
        request_msg=request.get_data(as_text=True)
        print(request_msg)
        messages.append(request_msg)
        for m in range(len(messages)):
            print(messages[m])
        return request_msg
    app.run(port=8000, use_reloader = False)

elif len(sys.argv) == 3:
    try:
        print(header)
        username = input("Enter Username")
        print("Press CTRL+C to exit")
        while True:
            msg = input("Enter Message\n")
            r = request.post(url='http://%s:%s/' % (sys.argv[1],sys.argv[2]),msg = '[%s] - %s\n' % (username,msg))
    except request.exceptions.ConnectionError as e:
        print("Server unreachable")
        print("Details: {}".format(e))
    except KeyboardInterrupt:
        print("Goodbye")
        sys.exit()
    except Exception as e:
        print("something is wrong")
        print("Details: {}".format(e))


