import json

def get_data():
    with open('dota_hero.jp','r') as file_read:
        Heros = json.load(file_read)

    return Heros

# Create a handler for our get Heros
def read():
    """
     This function responds to a request for /api/hero
    with the complete lists of Heros
    :return: list of heros with their roles and counter
    """
    return get_data()