import requests


class GitHub:

    
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()


        return body


    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()


        return body


    # individual task 1


    def get_emoji(self, smile):
        r = requests.get(f"https://https://api.github.com/emojis/{smile}")
        body = r.json()


        return body

