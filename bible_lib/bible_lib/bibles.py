import json
import logging

from bible import Bible
from cached_bible_api_client import CachedBibleApiClient


class Bibles(object):
    def __init__(self):
        self.client = CachedBibleApiClient()
        self.logger = logging.getLogger()

    def list(self):
        try:
            response = self.client.get('bibles')
        except Exception as ex:
            self.logger.warning('Failed to retrieve bible list data.')
            self.logger.warning(ex)
            return []

        try:
            bible_entries = json.loads(response)['data']
        except Exception as ex:
            self.logger.warning('Failed to parse bible list.')
            self.logger.warning(ex)
            return []

        try:
            bibles = []
            for bible_entry in bible_entries:
                bible = Bible()
                bible.id = bible_entry['id']
                bible.name = bible_entry['nameLocal']
                bible.language = bible_entry['language']['nameLocal']
                bibles.append(bible)
        except Exception as ex:
            self.logger.warning('Failed to parse at least on of the bible entries.')
            self.logger.warning(ex)
            return []

        return bibles