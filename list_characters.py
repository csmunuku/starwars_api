import requests
import json

r = requests.get('https://swapi.co/api/people/')
starwars = json.loads(r.text)
# Loop through all the results


def list_characters(starwars):
    for i in range(len(starwars['results'])):
        print(starwars['results'][i]['name'])


if __name__ == "__main__":
    print("Here are the Starwars Characters!!")
    print("####################################")
    list_characters(starwars)
    print("####################################")
