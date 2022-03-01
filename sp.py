from flask import Flask, request
import pyfiglet
import requests
import sys


header = pyfiglet.figlet_format("MESSENGER",font='banner3-D',width=100)

if len(sys.argv) == 2:
    app = Flask(__name__)

    print(header)
    print("Listening on port {}".format(str(sys.argv[1])))


    @app.route('/', methods=['POST'])
    def messenger():
        request_msg = request.get_data(as_text=True)
        print(request_msg)
        return request_msg


    app.run(port=sys.argv[1], host='0.0.0.0', use_reloader=False)
    print('\nGoodbye')

elif len(sys.argv) == 3:
    try:
        print(header)
        username = input("Enter username:")
        print('Press CTRL + C to exit')
        while True:
            data = input('Message: \n')
            r = requests.post(url='http://%s:%s/' % (sys.argv[1], sys.argv[2]), data='[%s] - %s\n' % (username, data))
    except requests.exceptions.ConnectionError as e:
        print('Server is unavalable')
        print(e)
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit()
    except Exception as e:
        print('Something is wrong')
        print('Details: {}'.format(e))
