from flask import Flask, request
import pyfiglet

header = pyfiglet.figlet_format("MESSENGER",font='banner3-D',width=100)

app = Flask(__name__)

print(header)

messages=[]

@app.route('/',methods=['POST'])
def messener():
    request_msg=request.get_data(as_text=True)
    print(request_msg)
    messages.append(request_msg)
    for m in range(len(messages)):
        print(messages[m])
    return request_msg

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')

