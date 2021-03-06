import requests

class TrainingPlaylist:
    def __init__(self, username, playlistname):
        # Spotify username
        self.playlist_username = username
        # Spotify playlist name
        self.playlist_playlistname = playlistname

        self.playlist_song_names = None
        self.playlist_song_artists = None
        self.playlist_accousticness = None
        self.playlist_dancibility = None
        self.playlist_energy = None
        self.playlist_instrumentalness = None
        self.playlist_loudness = None
        self.playlist_speechness = None
        self.playlist_tempo = None
        self.playlist_valence = None

        self.training_song_names = []
        self.training_song_artists = []
        self.training_attribute_vector = None
        self.training_cluster_index = None
        self.training_accousticness = []
        self.training_dancibility = []
        self.training_energy = []
        self.training_instrumentalness = []
        self.training_loudness = []
        self.training_speechiness = []
        self.training_tempo = []
        self.training_valence = []

        self.groundtruth_song_names = []
        self.groundtruth_song_artists = []
        self.groundtruth_accousticness = []
        self.groundtruth_dancibility = []
        self.groundtruth_energy = []
        self.groundtruth_instrumentalness = []
        self.groundtruth_loudness = []
        self.groundtruth_speechiness = []
        self.groundtruth_tempo = []
        self.groundtruth_valence = []
        self.groundtruth_combined = []


    def get_playlist(self):
        # Request to heroku server to get spotify playlist info
        data = {'username':self.playlist_username, 'playlist':self.playlist_playlistname}
        playlist = requests.get('https://playlist-recommender.herokuapp.com/get_playlist', data)
        playlist = playlist.json()

        self.playlist_song_names = playlist[0]
        self.playlist_song_artists = playlist[1]

        song_uris = []
        for song in playlist[2]:
            song_uris.append(song.split(':')[2])

        song_uris = ','.join(song_uris)

        data = {'song_uri': song_uris}
        attributes = requests.get('https://playlist-recommender.herokuapp.com/song_attributes', data);
        attributes = attributes.json()

        self.playlist_accousticness = attributes[0]
        self.playlist_dancibility = attributes[1]
        self.playlist_energy = attributes[2]
        self.playlist_loudness = attributes[3]
        self.playlist_instrumentalness = attributes[4]
        self.playlist_speechness = attributes[5]
        self.playlist_tempo = attributes[6]
        self.playlist_valence = attributes[7]


    def construct_training_groundtruths(self):
        for song in range(0, len(self.playlist_song_names)-1):
            if song%5 is 0:
                self.groundtruth_song_names.append(self.playlist_song_names[song])
                self.groundtruth_song_artists.append(self.playlist_song_artists[song])
                self.groundtruth_accousticness.append(self.playlist_accousticness[song])
                self.groundtruth_dancibility.append(self.playlist_dancibility[song])
                self.groundtruth_energy.append(self.playlist_energy[song])
                self.groundtruth_loudness.append(self.playlist_loudness[song])
                self.groundtruth_instrumentalness.append(self.playlist_instrumentalness[song])
                self.groundtruth_speechiness.append(self.playlist_speechness[song])
                self.groundtruth_tempo.append(self.playlist_tempo[song])
                self.groundtruth_valence.append(self.playlist_valence[song])

            else:
                self.training_song_names.append(self.playlist_song_names[song])
                self.training_song_artists.append(self.playlist_song_artists[song])
                self.training_accousticness.append(self.playlist_accousticness[song])
                self.training_dancibility.append(self.playlist_dancibility[song])
                self.training_energy.append(self.playlist_energy[song])
                self.training_loudness.append(self.playlist_loudness[song])
                self.training_instrumentalness.append(self.playlist_instrumentalness[song])
                self.training_speechiness.append(self.playlist_speechness[song])
                self.training_tempo.append(self.playlist_tempo[song])
                self.training_valence.append(self.playlist_valence[song])

        self.construct_combined_ground_truth()


    def generate_playlist_vector(self):
        accousticness = 0
        dancibility = 0
        energy = 0
        instrumentalness = 0
        loudness = 0
        speechiness = 0
        tempo = 0
        valence = 0
        for element in range(0, len(self.training_song_names)):
            accousticness += self.training_accousticness[element]
            dancibility += self.training_dancibility[element]
            energy += self.training_energy[element]
            instrumentalness += self.training_instrumentalness[element]
            loudness += self.training_loudness[element]
            speechiness += self.training_speechiness[element]
            tempo += self.training_tempo[element]
            valence += self.training_valence[element]

        self.training_attribute_vector = [accousticness/len(self.training_accousticness), dancibility/len(self.training_dancibility), energy/len(self.training_energy), instrumentalness/len(self.training_instrumentalness), loudness/len(self.training_loudness), speechiness/len(self.training_speechiness), tempo/len(self.training_tempo), valence/len(self.training_valence)]


    def construct_combined_ground_truth(self):
        for song in range(0,len(self.groundtruth_song_names)):
            self.groundtruth_combined.append([
                self.groundtruth_accousticness[song],
                self.groundtruth_dancibility[song],
                self.groundtruth_energy[song],
                self.groundtruth_instrumentalness[song],
                self.groundtruth_loudness[song],
                self.groundtruth_speechiness[song],
                self.groundtruth_tempo[song],
                self.groundtruth_valence[song]
            ])


    def find_cluster(self):
        print(self.training_cluster_index)


    def trim_outliers(self):
        print("Trim")
