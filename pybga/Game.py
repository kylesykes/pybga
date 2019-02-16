import json


class Game:
    """
    {
        "games": [
            {
                "id": "SVQRjsXrhj",
                "name": "Last Stand",
                "year_published": 2018,
                "min_players": 2,
                "max_players": 4,
                "min_playtime": 15,
                "max_playtime": 30,
                "min_age": 8,
                "description": "<p>The Board Game Where Your Power Grows As You Lose</p>\r\n\r\n<div>\r\n<p>Do you have someone who keeps telling you they don't want to play games because they keep losing. This is the game for them! As you get attacked you get more cards to use to fight back! This game has</p>\r\n<ul>\r\n<li>Easy for families to play together</li>\r\n<li>Politics</li>\r\n<li>Quick to learn</li>\r\n<li>Tension building to the very end</li>\r\n<li>Players can participate through the entire game</li>\r\n<li>Great for new board gamers</li>\r\n</ul>\r\n<p>With art by cartoonist Chris McCoy this game stands up and shouts to be played with!</p></div>",
                "description_preview": " The Board Game Where Your Power Grows As You Lose \r\n\r\n \r\n Do you have someone who keeps telling you they don't want to play games because they keep losing. This is the game for them! As you get attacked you get more cards to use to fight back! This game has \r\n \r\n Easy for families to play together \r\n Politics \r\n Quick to learn \r\n Tension building to the very end \r\n Players can participate through the entire game \r\n Great for new board gamers \r\n \r\n With art by cartoonist Chris McCoy this game stands up and shouts to be played with!  ",
                "image_url": "https://images-na.ssl-images-amazon.com/images/I/51CFw-54KUL.jpg",
                "thumb_url": "https://images-na.ssl-images-amazon.com/images/I/51CFw-54KUL.jpg",
                "url": "https://www.boardgameatlas.com/search/game/SVQRjsXrhj",
                "price": "24.99",
                "msrp": "24.99",
                "discount": "0.00",
                "primary_publisher": "5 Color Combo",
                "publishers": [
                    "5 Color Combo"
                ],
                "designers": [
                    "Trent Ellingsen"
                ],
                "developers": [],
                "artists": [],
                "names": [
                    "Last Stand - The Board Game Where Your Power Grows As You Lose"
                ],
                "num_user_ratings": 4,
                "average_user_rating": 3.75
            }
        ]
    }
    """

    def __init__(self, game_string):
        self._json = json.loads(game_string)

