"""A video player class."""

from .video_library import VideoLibrary
from random import random
from math import floor
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = ""
        self.paused = False
        self.stopped = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        video_list = self._video_library.get_all_videos()
        sort_video_list = []
        for video in video_list:
            sort_video_list.append([video.title, video.video_id, video.tags])

        sort_video_list.sort()
        for i in range(len(sort_video_list)):
            print(sort_video_list[i][0] + " (" + sort_video_list[i][1] + ") [", end="")
            for index in range(len(sort_video_list[i][2])):
                if index == len(sort_video_list[i][2]) - 1:
                    print(sort_video_list[i][2][index], end="")
                else:
                    print(sort_video_list[i][2][index], end=" ")
            print("]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_object = self._video_library.get_video(video_id=video_id)
        if video_object == None:
            print("Cannot play video: Video does not exist")
        else:
            # added this for not putting "stopping video" if you pause and play same song
            # if self.playing != "" and self.playing == video_object.title and self.paused:
            #     pass
            if self.playing != "":
                print(f"Stopping video: {self.playing}")
            elif self.paused and self.playing != video_object.title:
                print(f"Stopping video: {self.playing}")
            print(f"Playing video: {video_object.title}")
            self.playing = video_object.title
            self.paused = False


    def stop_video(self):
        """Stops the current video."""
        global playing
        if self.playing == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.playing}")
            self.playing = ""

    def play_random_video(self):
        """Plays a random video from the video library."""
        random_index = floor(random() * len(self._video_library.get_all_videos()))
        # print(random_index)
        video_list = self._video_library.get_all_videos()
        video = video_list[random_index]
        self.play_video(video.video_id)

    def pause_video(self):
        """Pauses the current video."""
        # have to check if the video is stopped or not, might need a stopped variable now
        # should i just make a hashmap? sounds more convenient to use
        # the video should be stopped if self.playing = ""
        if self.playing == "":
            # means the video is stopped, cannot pause
            print("Cannot pause video: No video is currently playing")
        else:
            if self.paused:
                print(f"Video already paused: {self.playing}")
            else:
                print(f"Pausing video: {self.playing}")
                self.paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        if self.paused:
            print(f"Continuing video: {self.playing}")
            self.pause = False
        else:
            if self.playing == "":
                print("Cannot continue video: No video is currently playing")
            else:
                print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self.playing == "":
            print("No video is currently playing")
        
        video_list = self._video_library.get_all_videos()
        for video in video_list:
            if video.title == self.playing:
                print(f"Currently playing: {video.title} ({video.video_id}) [", end="")
                for index in range(len(video.tags)):
                    if index == len(video.tags) - 1:
                        print(video.tags[index], end="")
                    else:
                        print(video.tags[index], end=" ")

                if self.paused:
                    print("] - PAUSED")
                else:
                    print("]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        new_playlist = Playlist(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        pass

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
