# 1
def city_country(city, country):
    return f"{city.title()}, {country.title()}."


print(city_country("zaragoza", "spain"))
print(city_country("hot springs", "united states of america"))
print(city_country("dorohoi", "rumania"))


# 2
def make_album(artist, album_name, songs=None):
    album = {"artist": artist.title(), "album": album_name.title()}
    if songs:
        album["songs"] = songs
    return album


print(make_album("ed sheeran", "divide"))
print(make_album("charilie puth", "voicenotes"))
print(make_album("claudiu mariutanu", "piano music", 14))

while True:
    print("\nPlease, enter the album's information.")
    print("(press 'q' at any time to quit")

    album_artist = input("Enter the album's artist: ")
    if album_artist == "q":
        break

    album_title = input("Enter the album's title: ")
    if album_title == "q":
        break

    album_songs = input("Enter the number of the songs: "
                        "(Press enter to skip) ")
    if album_songs == "q":
        break

    print(make_album(album_artist, album_title, album_songs))



