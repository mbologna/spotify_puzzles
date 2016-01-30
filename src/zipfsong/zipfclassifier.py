import heapq

class ZipfClassifier(object):
    def __init__(self, capacity):
        self.songs = []
        self.capacity = capacity

    def add_song(self, song):
        heapq.heappush(self.songs, song)

    def retrieve_n_top_quality_songs(self):
        return heapq.nsmallest(self.capacity, self.songs)
