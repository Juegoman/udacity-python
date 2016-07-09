import webbrowser
class Anime():
    def __init__(this, anime_title, anime_synopsis, image, op_yt):
        this.title = anime_title
        this.synopsis = anime_synopsis
        this.image_url = image
        this.op_yt_url = op_yt
    def show_op(this):
        webbrowser.open(this.op_yt_url)
