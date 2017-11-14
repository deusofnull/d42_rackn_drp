import requests


class D42_Agent(object):

    def __init__(self, server, user, pwd):
        self.base = server
        self.user = user
        self.pwd = pwd

    def get(self, url, headers=None, params=None):
        print("user: " + str(self.user + "\n pwd: " + str(self.pwd)))
        response = requests.get(
            self.base + url,
            headers=headers,
            auth=(self.user, self.pwd),
            params=params,
        )

        return response.json()
