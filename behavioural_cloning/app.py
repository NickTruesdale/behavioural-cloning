from fastapi import FastAPI

class App(FastAPI):
    '''The app class for the sloth model service'''

    def __init__(self):
        super().__init__()
        self.add_event_handler('startup', self.startup)

    @staticmethod
    def startup():
        '''Server startup event handler'''
        print('INFO: Server is now running.')
 