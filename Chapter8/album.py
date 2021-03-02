def make_album(album_artist, album_name, album_song_number=''):
    if album_song_number !="":
        album={
        "Artist":album_artist,
        "Album":album_name,
        "Number of Songs":album_song_number
    }
    else:
        album={
        "Artist":album_artist,
        "Album":album_name
    }
    albums.append(album)
    return album

albums=[]
numToEnter=int(input("How many albums are you entering?"))
counter=0
while counter < numToEnter:
     album_artist=(input("Enter the albums artist: "))
     album_name=(input("Enter the albums name: "))
     album_song_number=(input("Enter the number of songs on the album (optional): "))
     make_album(album_name, album_artist, album_song_number)
     counter+=1

for album in albums:
    print(album)