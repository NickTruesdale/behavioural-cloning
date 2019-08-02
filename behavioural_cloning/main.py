'''
This is the main entry point for the behavioural cloning model.
It spins up a flask server and websocket to communicate with Unity,
which is running the Udacity self-driving car simulation.

Images are received fron Unity, and driving input is returned.

Note: This code is re-implemented by Nick Truesdale, but conceptually
is mostly lifted from the tutorial by Siraj Raval.

https://github.com/llSourcell/How_to_simulate_a_self_driving_car
'''

import os
import uvicorn
from dotenv import load_dotenv

from behavioural_cloning.app import App

def run_app(app):
    '''Run the app using uvicorn'''
    uvicorn.run(
        app=app,
        host=os.getenv('UVICORN_HOST'),
        port=int(os.getenv('UVICORN_PORT')),
        reload=True
    )

def main():
    load_dotenv()
    
    app = App()
    run_app(app)

if __name__ == '__main__':
    main()
