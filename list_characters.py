import requests
import json

r = requests.get('https://swapi.co/api/people/')
star_wars = json.loads(r.text)
# Loop through all the results


def list_characters(star_wars):
    for i in range(len(star_wars['results'])):
        print(star_wars['results'][i]['name'])


if __name__ == "__main__":
    print("Here are the Starwars Characters!!")
    print("####################################")
    list_characters(star_wars)
    print("####################################")
