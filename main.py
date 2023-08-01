import requests
from bs4 import BeautifulSoup
import json
import time
import random

def save_array_to_json(array, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        # Use json.dump() to write the array to the file in JSON format
        json.dump(array, file, ensure_ascii=False)


def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # Use json.load() to read the JSON data from the file
        data = json.load(file)
    return data

import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

links = [
    "http://www.sufoi.dk/obs/obs-1996/obs96-8a.php",
    "http://www.sufoi.dk/obs/obs-1996/obs96-bc.php",
    "http://www.sufoi.dk/obs/obs-1997/obs97-k1.php",
    "http://www.sufoi.dk/obs/obs-1997/obs97-k2.php",
    "http://www.sufoi.dk/obs/obs-1997/obs97-k3.php",
    "http://www.sufoi.dk/obs/obs-1997/obs97-k4.php",
    "http://www.sufoi.dk/obs/obs-1998/obs98-k1.php",
    "http://www.sufoi.dk/obs/obs-1998/obs98-k2.php",
    "http://www.sufoi.dk/obs/obs-1998/obs98-k3.php",
    "http://www.sufoi.dk/obs/obs-1998/obs98-k4.php",
    "http://www.sufoi.dk/obs/obs-1999/obs99-k1.php",
    "http://www.sufoi.dk/obs/obs-1999/obs99-k2.php",
    "http://www.sufoi.dk/obs/obs-1999/obs99-k4.php",
    "http://www.sufoi.dk/obs/obs-2000/obs00-k1.php",
    "http://www.sufoi.dk/obs/obs-2000/obs00-k2.php",
    "http://www.sufoi.dk/obs/obs-2000/obs00-k3.php",
    "http://www.sufoi.dk/obs/obs-2000/obs00-k4.php",
    "http://www.sufoi.dk/obs/obs-2001/obs01-k1.php",
    "http://www.sufoi.dk/obs/obs-2001/obs01-k2.php",
    "http://www.sufoi.dk/obs/obs-2001/obs01-k3.php",
    "http://www.sufoi.dk/obs/obs-2001/obs01-k4.php",
    "http://www.sufoi.dk/obs/obs-2002/obs02-k1.php",
    "http://www.sufoi.dk/obs/obs-2002/obs02-k2.php",
    "http://www.sufoi.dk/obs/obs-2002/obs02-k3.php",
    "http://www.sufoi.dk/obs/obs-2002/obs02-k4.php",
    "http://www.sufoi.dk/obs/obs-2003/obs03-k1.php",
    "http://www.sufoi.dk/obs/obs-2003/obs03-k2.php",
    "http://www.sufoi.dk/obs/obs-2003/obs03-k3.php",
    "http://www.sufoi.dk/obs/obs-2003/obs03-k4.php",
    "http://www.sufoi.dk/obs/obs-2004/obs04-k1.php",
    "http://www.sufoi.dk/obs/obs-2004/obs04-k2.php",
    "http://www.sufoi.dk/obs/obs-2004/obs04-k3.php",
    "http://www.sufoi.dk/obs/obs-2004/obs04-k4.php",
    "http://www.sufoi.dk/obs/obs-2005/obs05-k1.php",
    "http://www.sufoi.dk/obs/obs-2005/obs05-k2.php",
    "http://www.sufoi.dk/obs/obs-2005/obs05-k3.php",
    "http://www.sufoi.dk/obs/obs-2005/obs05-k4.php",
    "http://www.sufoi.dk/obs/obs-2006/obs06-k1.php",
    "http://www.sufoi.dk/obs/obs-2006/obs06-k2.php",
    "http://www.sufoi.dk/obs/obs-2006/obs06-k3.php",
    "http://www.sufoi.dk/obs/obs-2006/obs06-k4.php",
    "http://www.sufoi.dk/obs/obs-2007/obs07-k1.php",
    "http://www.sufoi.dk/obs/obs-2007/obs07-k2.php",
    "http://www.sufoi.dk/obs/obs-2007/obs07-k3.php",
    "http://www.sufoi.dk/obs/obs-2007/obs07-k4.php",
    "http://www.sufoi.dk/obs/obs-2008/obs08-k1.php",
    "http://www.sufoi.dk/obs/obs-2008/obs08-k2.php",
    "http://www.sufoi.dk/obs/obs-2008/obs08-k3.php",
    "http://www.sufoi.dk/obs/obs-2008/obs08-k4.php",
    "http://www.sufoi.dk/obs/obs-2009/obs09-k1.php",
    "http://www.sufoi.dk/obs/obs-2009/obs09-k2.php",
    "http://www.sufoi.dk/obs/obs-2009/obs09-k3.php",
    "http://www.sufoi.dk/obs/obs-2009/obs09-k4.php",
    "http://www.sufoi.dk/obs/obs-2009/obs09-k1.php",
    "http://www.sufoi.dk/obs/obs-2010/obs10-k1.php",
    "http://www.sufoi.dk/obs/obs-2010/obs10-k2.php",
    "http://www.sufoi.dk/obs/obs-2010/obs10-k3.php",
    "http://www.sufoi.dk/obs/obs-2010/obs10-k4.php",
    "http://www.sufoi.dk/obs/obs-2011/obs11-k1.php",
    "http://www.sufoi.dk/obs/obs-2011/obs11-k2.php",
    "http://www.sufoi.dk/obs/obs-2011/obs11-k3.php",
    "http://www.sufoi.dk/obs/obs-2011/obs11-k4.php",
    "http://www.sufoi.dk/obs/obs-2012/obs12-k1.php",
    "http://www.sufoi.dk/obs/obs-2012/obs12-k2.php",
    "http://www.sufoi.dk/obs/obs-2012/obs12-k3.php",
    "http://www.sufoi.dk/obs/obs-2012/obs12-k4.php",
    "http://www.sufoi.dk/obs/obs-2013/obs13-k1.php",
    "http://www.sufoi.dk/obs/obs-2013/obs13-k2.php",
    "http://www.sufoi.dk/obs/obs-2013/obs13-k3.php",
    "http://www.sufoi.dk/obs/obs-2013/obs13-k4.php",
    "http://www.sufoi.dk/obs/obs-2014/obs14-k1.php",
    "http://www.sufoi.dk/obs/obs-2014/obs14-k2.php",
    "http://www.sufoi.dk/obs/obs-2014/obs14-k3.php",
    "http://www.sufoi.dk/obs/obs-2014/obs14-k4.php",
    "http://www.sufoi.dk/obs/obs-2015/obs15-k1.php",
    "http://www.sufoi.dk/obs/obs-2015/obs15-k2.php",
    "http://www.sufoi.dk/obs/obs-2015/obs15-k3.php",
    "http://www.sufoi.dk/obs/obs-2015/obs15-k4.php",
    "http://www.sufoi.dk/obs/obs-2016/obs16-k1.php",
    "http://www.sufoi.dk/obs/obs-2016/obs16-k2.php",
    "http://www.sufoi.dk/obs/obs-2016/obs16-k3.php",
    "http://www.sufoi.dk/obs/obs-2016/obs16-k4.php",
    "http://www.sufoi.dk/obs/obs-2017/obs17-k1.php",
    "http://www.sufoi.dk/obs/obs-2017/obs17-k2.php",
    "http://www.sufoi.dk/obs/obs-2017/obs17-k3.php",
    "http://www.sufoi.dk/obs/obs-2017/obs17-k4.php",
    "http://www.sufoi.dk/obs/obs-2018/obs18-k1.php",
    "http://www.sufoi.dk/obs/obs-2018/obs18-k2.php",
    "http://www.sufoi.dk/obs/obs-2018/obs18-k3.php",
    "http://www.sufoi.dk/obs/obs-2018/obs18-k4.php",
    "http://www.sufoi.dk/obs/obs-2019/obs19-k1.php",
    "http://www.sufoi.dk/obs/obs-2019/obs19-k2.php",
    "http://www.sufoi.dk/obs/obs-2019/obs19-k3.php",
    "http://www.sufoi.dk/obs/obs-2019/obs19-k4.php",
    "http://www.sufoi.dk/obs/obs-2020/obs20-k1.php",
    "http://www.sufoi.dk/obs/obs-2020/obs20-k2.php",
    "http://www.sufoi.dk/obs/obs-2020/obs20-k3.php",
    "http://www.sufoi.dk/obs/obs-2020/obs20-k4.php",
    "http://www.sufoi.dk/obs/obs-2021/obs21-k1.php",
    "http://www.sufoi.dk/obs/obs-2021/obs21-k2.php",
    "http://www.sufoi.dk/obs/obs-2021/obs21-k3.php",
    "http://www.sufoi.dk/obs/obs-2021/obs21-k4.php",
    "http://www.sufoi.dk/obs/obs-2022/obs22-k1.php",
    "http://www.sufoi.dk/obs/obs-2022/obs22-k2.php",
    "http://www.sufoi.dk/obs/obs-2022/obs22-k3.php",
    "http://www.sufoi.dk/obs/obs-2022/obs22-k4.php",
    "http://www.sufoi.dk/obs/obs-2023/obs23-k1.php",
    "http://www.sufoi.dk/obs/obs-2023/obs23-k2.php",
    "http://www.sufoi.dk/obs/obs-2023/obs23-k3.php"
]


def get_note_text(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status()

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    note_id = url.split('#', 1)[1]

    name_tag = soup.find('a', attrs={'name': note_id})
    print(url)
    mellemrubrik2 = name_tag.find_parent('div')

    # I need to find the next sibling div that has a classname of either brod og brodindryk
    first_div = mellemrubrik2.find_next_sibling('div')
    note_text = first_div.get_text(strip=True)
    next_sibling = first_div.find_next_sibling('div')

    while next_sibling:
        note_text += '\n' + next_sibling.get_text(strip=True)
        next_sibling = next_sibling.find_next_sibling('div')

    return note_text


def get_observations(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        tables = soup.find_all('table', attrs={'frame': 'box'})
        observations = []
        if len(tables) >= 5:
            fifth_table = tables[5]
            # print(fifth_table)
            # print(fifth_table.find_all('tr'))

            for row in fifth_table.find_all('tr')[2:]:  # Skip the first row as it contains headers
                try:
                    columns = row.find_all('td')
                    dato = columns[0].get_text(strip=True)
                    begyndelsestidspunkt = columns[1].get_text(strip=True)
                    varighed = columns[2].get_text(strip=True)
                    observationssted = columns[3].get_text(strip=True)
                    vidner = columns[4].get_text(strip=True)
                    farver = columns[5].get_text(strip=True)
                    bemærkninger = columns[6].find('a')['href'] if columns[6].find('a') else columns[6].get_text(
                        strip=True)

                    # Extract other columns as needed...

                    # Create an object to store the extracted data
                    observation = {
                        'date': dato,
                        'start-time': begyndelsestidspunkt,
                        'duration': varighed,
                        'location': observationssted,
                        'witnesses': vidner,
                        'colors': farver,
                        'notes': bemærkninger,
                    }

                    observations.append(observation)
                except:
                    print(url, row)

        return observations

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def get_and_save_newest_observations():
    all_observations = []
    for link in links:
        print(link)
        observations = get_observations(link)
        for observation in observations:
            all_observations.append(observation)
    save_array_to_json(all_observations, 'observations-original.json')


# Only need to do this once!
# get_and_save_newest_observations()

# if the observations-with-note-text is not there simply run the command with obsercations-original.json
# filename = 'observations-original.json'

# Noget mærkeligt her!
# date": "27.12.09", "start-time": "ca. 21.15", "duration": "1-2 min", "location": "2990 Nivå", "witnesses": "2", "colors": "hvidt lys", "notes": "brt09-k4.php#271209nivaa"}
def add_note_text_to_observations():
    filename = 'observations-with-note-text.json'
    #filename = 'observations-with-note-text.json'  # Replace with the actual filename
    observations = read_json_file(filename)

    observations_with_notes = []
    i = 0
    for observation in observations:
        note_text = observation['notes']
        wait_time = random.randint(2, 4)
        if note_text[:27] == 'http://www.sufoi.dk/obs/obs':
            # Pause the execution for the randomly generated time
            time.sleep(wait_time)
            try:
                note_text = get_note_text(note_text)
                #print(note_text)
                observations[i]['notes'] = note_text
            except:
                observations[i]['notes'] = ''
                #print('ERROR!!!' + note_text)
            save_array_to_json(observations, 'observations-with-note-text.json')

        if note_text[:25] == 'http://www.ufo.dk/obs/obs':
            print('Ufo')

            # Pause the execution for the randomly generated time
            time.sleep(wait_time)
            try:
                note_text = get_note_text(note_text)
                print(note_text)
                observations[i]['notes'] = note_text
            except:
                observations[i]['notes'] = ''
                print('ERROR!!!' + note_text)
            save_array_to_json(observations, 'observations-with-note-text.json')

        if note_text[:13] == '../../obs/obs':
            try:
                # Pause the execution for the randomly generated time
                time.sleep(wait_time)
                new_link = 'http://www.sufoi.dk/' + note_text[6:]
                note_text = get_note_text(new_link)
                observations[i]['notes'] = note_text
                #print(new_link, note_text)
                save_array_to_json(observations, 'observations-with-note-text.json')
            except:
                print('ERROR!!!' + note_text)
        i += 1


add_note_text_to_observations()

def clean_weird_links():
    filename = 'observations-with-note-text.json'
    observations = read_json_file(filename)
    index = 0
    for observation in observations:
        note_text = observation['notes']
        if '.php#' in note_text:
            print(observation)

        index += 1

#clean_weird_links()


def clean_data_using_gpt():
    prompt = """Jeg er ved at rense data og skal bruge det rensede data. Kun svar med det rensede data!
Kolonnerne er som følger
Dato; Begyndel-sestidspunkt; Varighed i sekunder; Observationssted (postnr. og by); Vidner; Farver; Bemærkninger

Original data:
august 1999; ca. 23.00 DST; 2-3 sek; Nordsjælland; ?; hvidt
Renset data:
01.08.1999; 23:00; 3; Nordsjælland; NAN; hvid

Original data:
04.08.00; ca. 03.30-04.00 DST; 2-3 sek; 5500 Middelfart; 2; guld, gløder som fuldmånen
Renset data:
04.08.2000; 03:30; 3; 5500 Middelfart; 2; guld

Original data:
22.07.13; eftermiddag; +20 sek; 6400 Sønderborg; ?; sort/grå/blå
Renset data:
22.07.2013; 15:00; 20; 6400 Sønderborg; sort, grå, blå; 

Original data:"""

    filename = 'observations-with-note-text.json'  # Replace with the actual filename
    observations = read_json_file(filename)

    index = 0
    for observation in observations:
        if 'cleaned' not in observation:
            original_observation = ";".join([
                observation['date'], observation['start-time'],
                observation['duration'], observation['location'], observation['witnesses'],
                observation['colors']
            ])

            full_prompt = prompt + '\n' + original_observation + "\nRenset data:"
            print(original_observation)
            cleaned_data = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": full_prompt}])['choices'][0]['message']['content']
            print(cleaned_data)
            cleaned_data_split = cleaned_data.split(';')
            observations[index]['date'] = cleaned_data_split[0]
            observations[index]['start-time'] = cleaned_data_split[1]
            observations[index]['duration'] = cleaned_data_split[2]
            observations[index]['location'] = cleaned_data_split[3]
            observations[index]['witnesses'] = cleaned_data_split[4]
            observations[index]['colors'] = cleaned_data_split[5]
            observations[index]['cleaned'] = 'true'
            save_array_to_json(observations, 'observations-with-note-text-cleaned.json')
        index += 1

# clean_data_using_gpt()

