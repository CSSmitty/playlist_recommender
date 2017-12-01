import deltaVector
import os
import pickle
import numpy
import math

pickles_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data','pickle','normalized','agg')


def get_distance_between_playlist_types():
	distance_dictonary = {}
	for subdir, dirs, files in os.walk(pickles_folder):
		for file in files:
			if file != '.DS_Store':
				filepath = subdir + os.sep + file
				# deltaVector.normalize_from_pickle(filepath)
				# deltaVector.findAverage_from_pickle(filepath)
				aggregate_song_list1 = os.path.join(os.path.dirname(filepath),'agg_normalized_Fitness.txt')
				in1 = open(aggregate_song_list1,'rb')
				song_list_1 = pickle.load(in1)
				in1.close()
				in2 = open(filepath,'rb')
				song_list_2 = pickle.load(in2)
				in2.close()
				difference_dict = deltaVector.findDistance(song_list_1, 'agg_normalized_Fitness.txt', song_list_2, os.path.basename(filepath))
				distance = math.sqrt(
					math.pow(difference_dict["accousticness"],2) +
					math.pow(difference_dict['danceability'],2) +
					math.pow(difference_dict["energy"],2) +
					math.pow(difference_dict["instrumentalness"],2) +
					math.pow(difference_dict["loudness"],2) +
					math.pow(difference_dict["speechiness"],2) +
					math.pow(difference_dict["tempo"],2) +
					math.pow(difference_dict["valence"],2))

				distance_dictonary.update({difference_dict["playlist_type_2"]:distance})

	return distance_dictonary


def normalize_distance_values(playlist_distances):
	furthest_distance = 0
	for key in playlist_distances:
		if playlist_distances[key] > furthest_distance:
			furthest_distance = playlist_distances[key]


	for key in playlist_distances:
		normalized_distance = playlist_distances[key]/furthest_distance
		playlist_distances.update({key:normalized_distance})

	return playlist_distances


def apply_normalized_distances(playlist_distances):
	iteration = 0
	for key in playlist_distances:
		if key == 'agg_normalized_R_B.txt':
			song_file = 'R_B.txt'
		else:
			song_file = str(key.split('_')[2])
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists', song_file)) as data:
			song_data = pickle.load(data)
			for song in song_data:
				song.attributes.update({"rec_value":playlist_distances[key]})

			song_file_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists_with_recommended', song_file), 'wb')
			pickle.dump(song_data, song_file_output)
			song_file_output.close()


# def check_songs(playlist_distances):
# 	for key in playlist_distances:
# 		if key == 'agg_normalized_R_B.txt':
# 			song_file = 'R_B.txt'
# 		else:
# 			song_file = str(key.split('_')[2])
# 		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data', 'pickle', 'song_lists_with_recommended', song_file)) as data:
# 			song_data = pickle.load(data)
# 			print song_data[0].attributes

def produce_training_playlists(playlist_distances):



def produce_test_playlists(playlist_distances):


playlist_distances = get_distance_between_playlist_types()
normalized_playlist_distances = normalize_distance_values(playlist_distances)
apply_normalized_distances(normalized_playlist_distances)
# check_songs(normalized_playlist_distances)
