"""#

from sys import api_version


petroninja api_version
"""
import requests

class PetroNinja:

    def __init__(self, api_area='wells', api_subarea='header', version='v1'):

        self.endpoint = "https://api.petroninja.com/api/"+version+"/"+api_area+"/"+api_subarea
        api_key = "Z6omObqgyUa1N7ApvBHfZ88qHnPNi4Df2X0V3OKp"

        self.headers = {
            "x-api-key": api_key,
            'ContentType': "application/json"
        }

    def get_wells(self, uwis):

        response = requests.post(self.endpoint, json=uwis, headers=self.headers)
        response.raise_for_status()
        # header_data = response.json()

        return response.json()

    def get_wells_search(self, uwis):

        response = requests.get(self.endpoint, json=uwis, headers=self.headers)
        response.raise_for_status()
        # header_data = response.json()

        return response.json()
