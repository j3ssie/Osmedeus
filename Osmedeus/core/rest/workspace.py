import os
import glob
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required
from pathlib import Path

from Osmedeus.core import config
from Osmedeus.core import utils

'''
Workspace listing and detail
'''

class Workspaces(Resource):
    @jwt_required
    def get(self):
        # get all options file availiable
        option_files = glob.glob(config.OSMEDEUS_HOME + '/storages/**/options.json', recursive=True)
        if not option_files:
            return {'error': 'No worksapce avaliable'}

        ws = []
        try:
            for options in option_files:
                json_options = utils.reading_json(options)
                if json_options:
                    ws.extend([ws for ws in os.listdir(
                        json_options['WORKSPACES']) if ws[0] != '.'])
        except Exception:
            # @TODO get config from flask app
            # loading default config path if some exeption happend
            options = utils.just_read_config()
            ws = os.listdir(options.get('WORKSPACES'))

        return {'workspaces': list(set(ws))}


# get main json by workspace name
class Workspace(Resource):

    @jwt_required
    def get(self, workspace):
        #
        # @TODO potential LFI here
        #
        ws_name = os.path.basename(os.path.normpath(workspace))
        options_path = config.OSMEDEUS_HOME + '/storages/{0}/options.json'.format(ws_name)
        self.options = utils.reading_json(options_path)

        # looking for log file if options file not found
        if not self.options:
            ws_json = config.OSMEDEUS_HOME + '/workspaces/{0}/{0}.json'.format(ws_name)
            return utils.reading_json(ws_json)

        if not self.options:
            return {'error': 'Log file not found'}

        if ws_name in os.listdir(self.options['WORKSPACES']):
            ws_json = self.options['WORKSPACES'] + "/{0}/{0}.json".format(ws_name)
            if os.path.isfile(ws_json):
                return utils.reading_json(ws_json)
        return 'Custom 404 here', 404
