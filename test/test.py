import unittest

from main import min_beers


class TestMinBeers(unittest.TestCase):
    def test_min_beers(self):
        # Коли всі учасники люблять всі види пива
        N = 3
        B = 3
        likes = ['YYY', 'YYY', 'YYY']
        self.assertEqual(min_beers(N, B, likes), 1)

        # Коли кожен учасник любить тільки один вид пива, і це різні види
        N = 3
        B = 3
        likes = ['YNN', 'NYN', 'NNY']
        self.assertEqual(min_beers(N, B, likes), 3)

        # Коли кожен учасник любить тільки один вид пива, і це один і той же вид
        N = 3
        B = 3
        likes = ['YNN', 'YNN', 'YNN']
        self.assertEqual(min_beers(N, B, likes), 1)

        # Коли кожен учасник любить два види пива
        N = 3
        B = 3
        likes = ['YYN', 'YNY', 'NYY']
        self.assertEqual(min_beers(N, B, likes), 2)

        # Коли кожен учасник любить тільки один вид пива, але є один вид, який люблять всі
        N = 3
        B = 3
        likes = ['YYN', 'YNY', 'NYY']
        self.assertEqual(min_beers(N, B, likes), 2)

if __name__ == '__main__':
    unittest.main()
