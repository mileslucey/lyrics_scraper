'''
Lyrics Scraper
Program contains a Tkinter GUI that prompts the user for a music artist and song title.
When the user presses the 'Get Lyrics' button, the program scrapes the 'azlyrics.com' website for the song's lyrics and writes the lyrics to a txt file.
The program then opens the txt file.
'''

# Dependencies and set up
from bs4 import BeautifulSoup
import requests
import os
from tkinter import * 
import webbrowser

def scrape(artist, song): # Function scrapes the AZ Lyrics website for song lyrics using the inputs defined by the user
    url = 'https://www.azlyrics.com/lyrics/' + artist + '/' + song + '.html'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    article_body = soup.find('body')
    division_list = article_body.find_all('div')
    file_name = artist + '_' + song + '_lyrics.txt'
    global result_label
    result_label.destroy()
    with open(file_name, 'w') as write_file:
        try:
            for i in range(17,21,3):
                write_file.write(division_list[i].text)
            result_label = Label(root, text = 'Success! See txt file for lyrics')
            result_label.grid(row = 4, column = 0)
            open_file(artist, song)
        except Exception:
            result_label = Label(root, text = 'The site doesn\'t have lyrics for that song. Try again!')
            result_label.grid(row = 4, column = 0)
            write_file.close()
            os.remove(file_name)

def open_file(artist, song): # Function opens the newly-created txt file with song lyrics
    file_name = artist + '_' + song + '_lyrics.txt'
    webbrowser.open(file_name)

def main(): # Function prompts user input for artist and song title and calls the scrape function
    artist = artist_entry.get().strip().lower()
    song = song_entry.get().strip().lower()
    artist_clean = ''.join(character for character in artist if character.isalnum()) 
    song_clean = ''.join(character for character in song if character.isalnum()) 
    scrape(artist_clean, song_clean)
    
# GUI
root = Tk()
root.configure(bg = '#C2CAE8')
root.title('Lyrics Finder')
title = Label(root, text = 'Lyrics Finder', font = "Helvetica 20 bold", bg = '#C2CAE8')
result_label = Label(root)
artist_entry = Entry(root, width = 50, font = 'Helvetica 10')
song_entry = Entry(root, width = 50, font = 'Helvetica 10')
function_button = Button(root, text = 'Get Lyrics', command = main, bg = '#111D4A', font = "Helvetica 10 bold", fg = '#ffffff')
title.grid(row = 0, column = 0)
artist_entry.grid(row = 1, column = 0, padx = 5, pady = 5)
song_entry.grid(row = 2, column = 0, padx = 5)
function_button.grid(row = 3, column = 0, padx = 5, pady = 5)
artist_entry.insert(0, 'Enter the artist name')
song_entry.insert(1, 'Enter the song name')
root.mainloop()

'''
Inputs:
-- Artist: Mariah Carey
-- Song: We belong Together

Output:

"We Belong Together" lyrics


Sweet love

I didn't mean it
When I said I didn't love you so
I should've held on tight
I never should've let you go

I didn't know nothing
I was stupid
I was foolish
I was lying to myself

I could not fathomed that I would ever be without your love
Never imagined I'd be sitting here beside myself

'Cause I didn't know you
'Cause I didn't know me
But I thought I knew everything
I never felt

The feeling that I'm feeling
Now that I don't hear your voice
Or have your touch and kiss your lips
'Cause I don't have a choice
Oh, what I wouldn't give to have you lying by my side right here
'Cause baby

When you left I lost a part of me
It's still so hard to believe
Come back baby please
'Cause we belong together

Who else am I gonna lean on when times get rough?
Who's gonna talk to me on the phone 'til the sun comes up?
Who's gonna take your place?
There ain't nobody better
Oh baby, baby
We belong together

I can't sleep at night
When you are on my mind
Bobby Womack's on the radio
Singing to me
'If you think you're lonely now'
Wait a minute
This is too deep, too deep
I gotta change the station

So I turn the dial
Tryna catch a break
And then I hear Babyface
I only think of you
And it's breaking my heart
I'm tryna keep it together
But I'm falling apart

I'm feeling all out of my element
I'm throwing things
Crying
Trying to figure out
Where the hell I went wrong
The pain reflected in this song
Ain't even half of what I'm feeling inside
I need you need you back in my life, baby
(in my life, in my life)

When you left I lost a part of me
It's still so hard to believe
Come back baby please
'Cause we belong together

Who else am I gonna lean on when times get rough?
Who's gonna talk to me on the phone 'til the sun comes up?
Who's gonna take your place?
There ain't nobody better
Oh baby, baby
We belong together, baby!

When you left I lost a part of me
It's still so hard to believe
Come back, baby, please
'Cause we belong together

Who am I gonna lean on when times get rough?
Who's gonna talk to me 'til the sun comes up?
Who's gonna take your place?
There ain't nobody better
Oh baby, baby
We belong together

'''
