from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets

from apps.spotify.models import *
from apps.spotify.serializers import UserSerializer


# Create your views here.
def home(request):
    return render(request, 'spotify/home.html', {})


def top_songs(request):
    try:
        top = Song.objects.order_by('rate').reverse()[:10]  # Top 10 songs by views (rate)
    except len(top) == 0:
        raise Http404("Error, there are no songs available.")
    return render(request, 'spotify/topsongs.html', {'topsonglist': top})


def playlist_view(request):
    user = get_user(request)
    playlists = get_playlists(user)
    return render(request, 'spotify/playlists.html', {'playlist_list': playlists})


def profile(request):
    app_user = get_user(request)
    return render(request, 'spotify/profile.html', {'usuario': app_user})


def log_out(request):
    logout(request)
    return render(request, 'spotify/logout.html', {})  # Redirect to a success page.


def infoplaylist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = playlist.get_songs()
    return render(request, 'spotify/infoplaylist.html', {'song_list': songs, 'playlist': playlist.name})


def artist_view(request):
    try:
        artists = Artist.objects.all()
    except len(artists) == 0:
        raise Http404("Error, no artist information available.")
    return render(request, 'spotify/artists.html', {'artistlist': artists})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# API Queries


def get_user(request):  # Returns the current user from any view.
    if request.user.is_authenticated:
        django_user = request.user  # Django.contrib.auth users
        social = django_user.social_auth.get(provider='spotify')  # User of social_django
        try:
            app_user = Spotify_User.objects.get(name=social.uid)  # Apps.spotify user
        except Spotify_User.DoesNotExist:
            app_user = Spotify_User(name=social.uid)

        app_user.access_token = social.get_access_token(
            load_strategy())  # If necessary, the access token is updated
        app_user.refresh_token = social.extra_data["refresh_token"]
        app_user.save()
        return app_user
    else:
        exit()


def get_playlists(user):  # Get a List of a User's Playlists
    response = requests.get(
        'https://api.spotify.com/v1/me/playlists',
        params={'access_token': user.access_token}
    )
    if response.status_code != 200:
        exit()
    playlists_dict = response.json()["items"]  # Array of dictionaries for each playlist
    playlists_list = []  # Remove playlists that do not appear.
    for playlist_json in playlists_dict:
        id = playlist_json['id']
        name = playlist_json['name']
        playlists_list.append(Playlist.get_playlist(id=id, name=name, user=user))
    return playlists_list