import requests
import json
import argparse

r = requests.get('https://swapi.co/api/people/')
starwars = json.loads(r.text)
# Loop through all the results


def parse_args():
    parser = argparse.ArgumentParser(
        description="Get StarWars Character Details!!",
        epilog="StarWars API 'SWAPI' - a free API describing the Star Wars universe!!",
        prog='get_character', usage='%(prog)s [options] <character>'
    )
    parser.add_argument('character', nargs=1)
    parser.add_argument('-f', '--films', action='store_true', dest='films',
                        help='display the names of films this character appears in')
    parser.add_argument('-g', '--gender', action='store_true', dest='gender',
                        help='display the character\'s gender')
    parser.add_argument('-H', '--home', action='store_true', dest='home',
                        help='display the character\'s home world')
    parser.add_argument('-m', '--mass', action='store_true', dest='mass',
                        help='display the character\'s mass')
    parser.add_argument('-s', '--species', action='store_true', dest='species',
                        help='display the character\'s species')

    args = parser.parse_args()
    return args



def film(film_url):
    f = json.loads(requests.get(film_url).text)
#    f = json.loads(requests.get('https://swapi.co/api/films/2/').text)
#    pprint.pprint(f['title'])
    print("Film Title: " + f['title'])


def films(starwars, ch):
    for i in range(len(starwars['results'])):
        if starwars['results'][i]['name'] == ch:
            if len(starwars['results'][i]['films']) > 0:
                for j in range(len(starwars['results'][i]['films'])):
                    film(starwars['results'][i]['films'][j])


def gender(starwars, ch):
    for i in range(len(starwars['results'])):
        if starwars['results'][i]['name'] == ch:
            print(ch + "'s Gender is " + starwars['results'][i]['gender'])


def homeworld_title(hw_url):
    hw = json.loads(requests.get(hw_url).text)
    print("Homeworld: " + hw['name'])


def homeworld(starwars, ch):
    for i in range(len(starwars['results'])):
        if starwars['results'][i]['name'] == ch:
            homeworld_title(starwars['results'][i]['homeworld'])


def mass(starwars, ch):
    for i in range(len(starwars['results'])):
        if starwars['results'][i]['name'] == ch:
            print(ch + "'s Mass is " + starwars['results'][i]['mass'])


def species_name(species_url):
    spn = json.loads(requests.get(species_url).text)
#    f = json.loads(requests.get('https://swapi.co/api/films/2/').text)
#    pprint.pprint(f['title'])
    print("Species Name: " + spn['name'])


def species(starwars, ch):
    for i in range(len(starwars['results'])):
        if starwars['results'][i]['name'] == ch:
            print("Species length " + str(len(starwars['results'][i]['species'])))
            if len(starwars['results'][i]['species']) > 0:
                for j in range(len(starwars['results'][i]['species'])):
                    species_name(starwars['results'][i]['species'][j])


# name = starwars['results'][i]['name']
# gender = starwars['results'][i]['gender']
# mass = starwars['results'][i]['mass']
# films, homeworld and species needs to be parsed again.

if __name__ == "__main__":
    arguments = parse_args()
    print("Character ==> " + str(arguments.character[0]))
    if arguments.films:
        print("Films for " + str(arguments.character[0]) + " : ")
        films(starwars, str(arguments.character[0]))
    elif arguments.gender:
        print("Gender for " + str(arguments.character[0]) + " : ")
        gender(starwars, str(arguments.character[0]))
    elif arguments.home:
        print("Homeworld for " + str(arguments.character[0]) + " : ")
        homeworld(starwars, str(arguments.character[0]))
    elif arguments.mass:
        print("mass for " + str(arguments.character[0]) + " : ")
        mass(starwars, str(arguments.character[0]))
    elif arguments.species:
        print("species for " + str(arguments.character[0]) + " : ")
        species(starwars, str(arguments.character[0]))
