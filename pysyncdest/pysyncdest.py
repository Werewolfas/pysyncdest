from pysyncdest.api import API
from pysyncdest.oauth import OAuth
from pysyncdest.manifest import Manifest


class Pysyncdest:

    def __init__(self, api_key, client_id=None, client_secret=None):
        """Base class for Pysyndest"""
        self.api = API(api_key)
        self._manifest = Manifest(self.api)
        self.oauth = OAuth(client_id, client_secret)

    def decode_hash(self, hash_id, definition, language="en"):
        """Get the corresponding static info for an item given it's hash value from the Manifest
        Args:
            hash_id:
                The unique identifier of the entity to decode
            definition:
                The type of entity to be decoded (ex. 'DestinyClassDefinition')
            language:
                The language to use when retrieving results from the Manifest
        Returns:
            dict: json corresponding to the given hash_id and definition
        Raises:
            PysyncdestException
        """
        return self._manifest.decode_hash(hash_id, definition, language)

    def update_manifest(self, language='en'):
        """Update the manifest if there is a newer version available
        Args:
            language [optional]:
                The language corresponding to the manifest to update
        """
        self._manifest.update_manifest(language)


class PysyncdestException(Exception):
    pass
