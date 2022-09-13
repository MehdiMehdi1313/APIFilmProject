import unittest

from application import awards, photo, title, title_movie

class TestApp(unittest.TestCase):

    #Test la méthode awards(id) de notre application avec l'award correspondant à un acteur
    def test_awards(self):
        self.assertEqual(awards("nm0654295"), "Primetime Emmy")

    #Test la méthode awards(id) pour un acteur qui n'a pas remporté d'award
    def test_noAwards(self):
        self.assertEqual(awards("nm0001865"), "Pas d'award attribué")
    
    #Test la méthode photo(id) pour obtenir la photo associé à l'id d'un acteur
    def test_photo(self):
        self.assertEqual(photo("nm0654295"), "https://m.media-amazon.com/images/M/MV5BNWQyMjA2MzctY2Q1Mi00MWQzLWEwYTUtYTQ3NmY2NTQwNTlmXkEyXkFqcGdeQXVyMTExNzQzMDE0._V1_.jpg")

    #Test la méthode title_movie(id) pour obtenir le titre d'un film à partir de son id
    def test_title_movie(self):
        self.assertEqual(title_movie("/title/get-details?tconst=tt13833688"), "The Whale")

    #Test la méthode title() qui retourne un dictionnaire(id,title), on vérifie donc que celui-ci n'est pas vide
    def test_dict_title(self):
        dict = {}
        dict = title()
        self.assertEqual(bool(dict),True)

    

if __name__ == '__main__':
    unittest.main()