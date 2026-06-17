"""JSON builder for structured resume output"""
import json

class JsonBuilder:

    @staticmethod
    def build(data):

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        )