import webbrowser


class Movie():
    '''This class provides a way to store movie related information'''
    def __init__(self, title, storyline, posterImage, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailerURL)
