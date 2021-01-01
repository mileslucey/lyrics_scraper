# Dependencies and set up
from bs4 import BeautifulSoup
import requests
import os

def scrape(artist, song): # Function scrapes the AZ Lyrics website for song lyrics using the inputs defined by the user
    url = 'https://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    article_body = soup.find('body')
    division_list = article_body.find_all('div')
    file_name = artist + '_' + song + '_lyrics.txt'
    with open(file_name, 'w') as write_file:
        try:
            for i in range(17,21,3):
                write_file.write(division_list[i].text)
        except Exception:
            print('The site doesn\'t have lyrics for that song. Try again!')
            write_file.close()
            os.remove(file_name)
            main()

def main(): # Function prompts user input for artist and song title and calls the scrape function
    artist = input('Enter the artist\'s name: ').strip().lower()
    song = input('Enter the song title: ').strip().lower()
    artist_clean = ''.join(character for character in artist if character.isalnum()) 
    song_clean = ''.join(character for character in song if character.isalnum()) 
    scrape(artist_clean, song_clean)

main()

'''

'''
