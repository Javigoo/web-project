from django.test import TestCase

# Create your tests here.

print("############# test #############")


class TestingTestCase(TestCase):
    print("############# class #############")

    def setUp(self):
        print("############# setUp #############")
        one = 1

    def true_test(self):
        print("############# true_test #############")
        self.assertEqual(one, 1)


"""
class PlaylistTest(TestCase):

    def setUp(self):
        User.objects.create(name='carlos')
        Playlist.objects.create(id='1234', name='pop', duration=124, user=User.objects.get(name='carlos'))

    def test_playlist_creation(self):
        pop = Playlist.objects.get(name='pop')
        carlos = User.objects.get(name='carlos')
        print(pop.user.name)
        print(carlos.name)
        self.assertEqual( pop.user.name, carlos.name)
"""
