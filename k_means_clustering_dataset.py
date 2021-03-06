from sklearn.cluster import KMeans
import numpy as np

def cluster_data(song_list):
    attribute_data = extract_attribute_data(song_list)
    # Takes the array of attributes for songs and clusters them
    attributes = np.array(attribute_data)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(attributes)
    labels = kmeans.predict(attributes)
    centroids = kmeans.cluster_centers_
    print centroids
    centroids_order = [
    centroids[0].tolist(),
    centroids[1].tolist(),
    centroids[2].tolist(),
    centroids[3].tolist(),
    centroids[4].tolist(),
    centroids[5].tolist(),
    centroids[6].tolist(),
    centroids[7].tolist(),
    centroids[8].tolist(),
    centroids[9].tolist()
    ]
    return labels, centroids_order

def extract_attribute_data(song_list):
    attribute_data = []
    for song in song_list:
        accousticness = song.attributes['accousticness']
        danceability = song.attributes['danceability']
        energy = song.attributes['energy']
        instrumentalness = song.attributes['instrumentalness']
        valence = song.attributes['valence']
        data_element = [accousticness,danceability,energy,instrumentalness,valence]
        attribute_data.append(data_element)
    return attribute_data
