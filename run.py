import os
from flask import redirect
from app import make_app
config_name = os.getenv('APP_SETTINGS') # config_name = "development"

app = make_app(config_name)
port = 5000

@app.route('/')
def Rundocs():
    """method to run app documentation
    """
    return redirect('/apidocs/')

if __name__ == '__main__':
    app.run(port=port)
