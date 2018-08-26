'''
webbrowser module is used to display websites to user, in which we make use
of open() function to open url given as parameter
'''
import webbrowser


class Movie():
    '''
    create class Movie
    :param tile: Movie Name
    :param poster_url: Movie Poster Image in URL
    :param trailer_url: Movie Trailer URL on  Youtube
    '''
    # Constructor
    def __init__(self, mv_title, mv_poster, mv_trailer):
        self.title = mv_title
        self.poster_image_url = mv_poster
        self.trailer_youtube_url = mv_trailer

    def show_trailer(self):
        '''crete function to show trailer on website
           :param self object to instantiate'''
        webbrowser.open(self.trailer_youtube_url)
