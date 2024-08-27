from django.shortcuts import render, redirect, get_object_or_404
from .models import Track
from .forms import TrackForm

def index(request):
    tracks = Track.get_all_tracks()
    return render(request, 'track/index.html', {'tracks': tracks})

def create_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TrackForm()
    return render(request, 'track/create_track.html', {'form': form})

def detail(request, id):
    track = Track.get_track_by_id(id)
    if track is None:
        return redirect('index')
    return render(request, 'track/detail.html', {'track': track})

def update_track(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('detail', id=id)
    else:
        form = TrackForm(instance=track)
    return render(request, 'track/update_track.html', {'form': form})

def delete_track(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        track.delete_track()  # Using the model method
        return redirect('index')
    return render(request, 'track/delete_track.html', {'track': track})
