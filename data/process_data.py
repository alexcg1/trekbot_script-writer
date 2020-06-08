#!/usr/bin/env python3

import json
input_path = 'scripts/all_scripts_raw.json'
output_path = 'scripts/all_scripts.json'
scripts_text = ''
scripts_json = []
counter = 0

with open(input_path) as json_file:
    data = json.load(json_file)
    series_names = []
    for series in data:
        series_names.append(series)
    for series in series_names:
        print("Getting " + series)
        for number in range(0, 1000):
            episode = "episode " + str(number)
            try:
                script = data[series][episode]
                scripts_text = scripts_text + script

                dictionary = {
                    "title": "Star Trek: " + series.upper() + " episode " + str(number),
                    "genre": ['science-fiction'],
                    "source_url": "",
                    "script": script
                }

                scripts_json.append(dictionary)

                counter += 1
            except:
                pass

with open("film_text.txt", 'w') as file:
    file.write(scripts_text)

scripts_json = json.dumps(scripts_json)

with open("scripts.json", "w") as file:
    file.write(scripts_json)
