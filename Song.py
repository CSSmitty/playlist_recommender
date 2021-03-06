# A class for more securely handling our song data when it is outside of the data base. Less
# potential for indexing errors compared with using other storage objects.  Also provides
# checks when a song is created that it also has all the required attributes populated and can 
# be entered in the DataBase.  Check value of Song.isValid() before any insert/analysis operations.

class Song:
	def __init__(self, song_dictionary=None, normalize=True):
		self.attributes = {
			"accousticness" : None,
			"artist_name" : None,
			"artist_familiarity" : None,
			"artist_hotness" : None,
			"cluster_id" : None,
			"danceability" : None,
			"duration" : None,
			"end_of_fade_in" : None,
			"energy" : None,
			"rec_value": None,
			"from_playlist" : None,
			"instrumentalness" : None,
			"loudness" : None,
			"speechiness" : None,
			"start_of_fade_out" : None,
			"tempo" : None,
			"title" : None,
			"valence" : None}
		self.normalize()
		self.isNormalized = normalize
		if not song_dictionary is None:
			self.fromDict(song_dictionary)


	def fromDict(self, song_dictionary):
		for key, value in song_dictionary.iteritems():
			attributeName = key.lower().replace(" ","_")
			if attributeName == 'artist':
				attributeName = 'artist_name'
			if attributeName == 'clusterid':
				attributeName = 'cluster_id'
			if attributeName in self.attributes.keys():
				self.attributes[attributeName] = value

	def isNormalized(self):
		return self.isNormalized

	def isValid(self):
		requiredAttributes = [
			'title', 
			'artist_name',
			'cluster_id', 
			'accousticness', 
			'danceability', 
			'energy', 
			'instrumentalness', 
			'loudness', 
			'speechiness',
			'tempo',
			'valence']
		for attributeName in requiredAttributes:
			if self.attributes[attributeName] is None:
				return False
		return True

	def normalize(self):
		if not (self.attributes['loudness'] is None):
			loudness = self.attributes['loudness']
			normalized_loudness = (loudness-(-60))/60
			self.attributes.update({'loudness' : normalized_loudness})
		
		if not (self.attributes['instrumentalness'] is None):
			instrumentalness = self.attributes['instrumentalness']
			normalized_instrumentalness = min(instrumentalness,1)
			self.attributes.update({'instrumentalness':normalized_instrumentalness})
		
		if not (self.attributes['tempo'] is None):
			tempo = self.attributes['tempo']
			normalized_tempo = min(((tempo-0)/250.0),1)
			self.attributes.update({'tempo':normalized_tempo})
		
		self.isNormalized = True


# attribute_dictionary = {
# 	"accousticness" : 0.4,
# 	"artist_name" : 'test_artist',
# 	"artist_familiarity" : None,
# 	"artist_hotness" : None,
# 	"cluster_id" : 4,
# 	"danceability" : 0.4,
# 	"duration" : None,
# 	"end_of_fade_in" : None,
# 	"energy" : 0.4,
# 	"instrumentalness" : 0.4,
# 	"loudness" : 0.4,
# 	"speechiness" : 0.4,
# 	"start_of_fade_out" : None,
# 	"tempo" : 0.4,
# 	"title" : 'test_title',
# 	"valence" : 0.4}


# song_test = Song(attribute_dictionary)
# print song_test.attributes
# print song_test.validForDatabase()
# print song_test.hasData
























