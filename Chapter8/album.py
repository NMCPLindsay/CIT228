def make_album(name,title,songs=None):
    if songs== None:
        songs=0
    else:
        songs=songs

        
    album={
        'Artist': name,
        'Album': title,
        'Tracks':songs       
    }
    print(album)

make_album('Blink-182', 'Enema of the State')
make_album('Chevelle', "Red", 12)

editing=True
while editing:
    name= input('Enter the Artist Name:')
    title= input('Enter album title:')
    songs=input("How many tracks are on the album?")
    make_album(name,title,songs)
    add=input('Press y to add more albums.')
    if add == 'y':
        editing=True
    else:
        editing=False
    
    