import random
class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self. genre = genre

class MusicLibrary:
    def __init__(self):
        self.library = []

    def add_song(self, song):
        self.library.append(song)
        self.library.sort(key = lambda x: x.title.lower())

    def search_song(self, keyword):
        left = 0
        right = len(self.library) - 1

        while left <= right:
            mid = (left + right) // 2
            if keyword.lower() == self.library[mid].title.lower():
                return [self.library[mid]]
            elif keyword.lower() < self.library[mid].title.lower():
                right = mid - 1
            else:
                left = mid + 1

        return []
    
    def recommend_song(self, genre):
        recommendations = []
        for song in self.library:
            if song.genre.lower() == genre.lower():
                recommendations.append(song)

        if not recommendations:
            return "No recommendation found."
        
        else:
            return random.choice(recommendations).title

    
library = MusicLibrary()
library.add_song(Song("Believer", "Imagine Dragons", "Rock"))
library.add_song(Song("Blinding Lights", "The Weeknd", "Pop"))
library.add_song(Song("Shape of You", "Ed Sheeran", "Pop"))
library.add_song(Song("Stairway to Heaven", "Led Zeppelin", "Rock"))
library.add_song(Song("My Name is", "Eminem", "Hip Hop"))
library.add_song(Song("Deep Cover", "Dr. Dre", "Hip Hop"))
library.add_song(Song("Purple Haze", "Jimi Hendrix", "Rock"))
library.add_song(Song("Where Is My Mind", "Pixies", "Rock"))
library.add_song(Song("BLOW", "Bruno Mars", "Rock"))
library.add_song(Song("Despacito", "Luis Fonsi", "Pop"))
library.add_song(Song("Umbrella", "Rihanna", "Pop"))
library.add_song(Song("Closer", "The Chainsmokers", "Pop"))

def main():
    print("Welcome to the Music Library!")
    while True:
        print("\nMenu: ")
        print("1. Search for a song")
        print("2. Get song recommendations")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            keyword = input("Enter song name: ")
            results = library.search_song(keyword)

            if results:
                print("\nSearch Results: ")
                for song in results:
                    print(f"{song.title} - {song.artist} ({song.genre})")
            else:
                print("\nNo matching songs found.")

        elif choice == '2':
            genre = input("Enter genre for recommendations: ").lower()
            recommendation = library.recommend_song(genre)
            print(f"\nRecommended Song: {recommendation}")

        elif choice == '3':
            print("Thank you for using the Music Library!")
            break
        else:
            print("Invalid choice. Please try again.")

'''results = library.search_song()
if results:
    print(f"Found: {results[0].title} - {results[0].artist} ({results[0].genre})")

else:
    print("Song not Found.")'''

if __name__ == "__main__":
    main()