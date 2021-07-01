"""A video playlist class."""
from src.video import Video
from .video_library import VideoLibrary

playlists = []

def check_instance(name):
    global playlists
    for video in playlists:
        if name.lower() == video.lower():
            return False
    playlists.append(name)
    return True

class CustomError(Exception):
    pass

class Playlist:
    """A class used to represent a Playlist."""
    def __new__(cls, name) -> None:
        if not check_instance(name=name):
            # raise CustomError("You already have a playlist of the same name")
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        instance = super(Playlist, cls).__new__(cls)
        instance.name = name
        print(f"Successfully created new playlist: {name}")
        return instance

    def __init__(self, name) -> None:
        self._video_library = VideoLibrary()
        self.name = name
        self.videos = []
    
    def add_video(self, playlist_name, id):
        play_flag = False
        video_flag = False
        for playlist in playlists:
            if playlist_name.lower() == playlist.lower():
                play_flag = True
                break

        # if not flag:
        #     print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        #     return

        video_list = self._video_library.get_video(video_id=id)
        if video_list == None:
            if not play_flag:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        
        if video_list.title not in self.videos:
            self.videos.append(video_list.title)
            print(f"Added video to {playlist_name}: {video_list.title}")
        else:
            print(f"Cannot add video to {playlist_name}: Video already added")
        
        self.videos.append(video_list.title)
        print(f"Added video to {playlist_name}: {video_list.title}")

    
