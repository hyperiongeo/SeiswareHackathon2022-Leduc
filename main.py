"""


main

"""
import requests
import os

from petro_ninja import PetroNinja


uwi_param = {
    "uwis": [
    "100011102604W500",
    ]
}

# ninja = PetroNinja("wells", "header")
# print(ninja.get_data(uwi_param))

ninja = PetroNinja("wells", "", version='v2')


boundary = {
  "swlat": 51.29957,
  "swlng": -114.44676,
  "nelat": 51.36135,
  "nelng": -114.33827
}

well_data = ninja.get_wells_search(boundary)

for well in well_data:
    print(well)

print("# OF WELLS:", len(well_data))
