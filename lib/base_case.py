import json.decoder
from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"No cookies with name {cookie_name}"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"No cookies with name {headers_name}"
        return response.headers[headers_name]

    def get_json_value (self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Respons is not JSON. Response text: '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have '{name}'"
        return response_as_dict[name]