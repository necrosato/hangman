from flask import Flask, request

import logging
import sys


def GetHangmanLogger(name="Hangman"):
    '''
    Create a new logging object for a hangman server
    Can give name for logger
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s : %(asctime)s : %(levelname)s : %(message)s')
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    return logger


class HangmanServer:

    def __init__(self):
        self.app = Flask('Hangman')
        self.active_games = {}
        self.logger = GetHangmanLogger()

        # Add endpoints
        self.add_endpoint(endpoint='/',
                endpoint_name='index', handler=self.index)
        self.add_endpoint(endpoint='/new-game',
                endpoint_name='new-game', handler=self.new_game)

    def index(self):
        return 'Hangman!'

    def new_game(self):
        return request.args.get('name')

    def run(self, port):
        '''
        Run the flask app
        '''
        self.app.run(debug=False, host='0.0.0.0', port=port)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        '''
        Register an endpoint function to the flask app
        '''
        self.app.add_url_rule(endpoint, endpoint_name, handler)


def main():
    hms = HangmanServer()
    hms.run(11111)


if __name__ == '__main__':
    main()
