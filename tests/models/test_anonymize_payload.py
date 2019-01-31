import unittest
from pprint import pprint as pp
import json

import pandas

from pyaaas.models.anonymize_payload import AnonymizePayload
from pyaaas.models.privacy_models import KAnonymity



class AnonymizationPayloadTest(unittest.TestCase):

    def setUp(self):
        anon_payload = AnonymizePayload()
        kanon = KAnonymity(k=4)
        anon_payload.metadata["models"][kanon.name] = kanon
        self.test_payload = anon_payload
        self.test_dataframe = pandas.DataFrame.from_dict({"id": [1,2,3],
                                                          "name": ["Mike", "Sarah", "Morten"],
                                                          "age": [10, 23, 43]} )

    def test_init_run(self):
        ap = AnonymizePayload()

    def test_set_data__add_dataframe(self):
        self.test_payload.data = self.test_dataframe
        print(self.test_payload.data)

    def test_convert_to_json(self):
        anon_payload = AnonymizePayload()
        kanon = KAnonymity(k=4)
        anon_payload.metadata["models"][kanon.name] = kanon
        result_dict = {**anon_payload}
        models = {}
        for key, value in anon_payload.metadata["models"].items():
            model_dict = {**value}
            models[key] = model_dict
        result_dict["metadata"]["models"] = models
        print(str(result_dict))


