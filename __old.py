


uwi_param = {
    "uwis": [
    "100011102604W500",
    ]
}



boundary = {
  "swlat": 51.29957,
  "swlng": -114.44676,
  "nelat": 51.36135,
  "nelng": -114.33827
}

ninja = PetroNinja("wells", "header", version='v2')

well_data = ninja.get_wells_search(boundary)

for well in well_data:
    print(well)

print("# OF WELLS:", len(well_data))



