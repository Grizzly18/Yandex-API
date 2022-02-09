import sys
from io import BytesIO
import requests
from PIL import Image
from toponym import get_ll


def get_picture(address, with_label=False):
    ll_span = get_ll(address)
    if with_label:
        label = ll_span[0] + ',' + 'pm2rdl'

    map_params = {
        "ll": ll_span[0],
        "spn": ll_span[1],
        "l": "sat",
        "pt": label
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    # Image.open(BytesIO(
    #     response.content)).show()

    return response.content


address = " ".join(sys.argv[1:])
get_picture(address, with_label=True)