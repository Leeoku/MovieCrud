from .models import MovieEntry
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import MovieForm
def home(request):
        # Database entries
    movies = MovieEntry.objects.all()
    return render(request, 'home.html', {'movies':movies})

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            #Create a form for future json manipulation
            cleanForm = form.cleaned_data
            form.save()
            cleanForm["date_watched"] = cleanForm["date_watched"].strftime("%m/%d/%Y")
            return redirect ('create')
    if request.method == "GET":
        form = MovieForm()
    return render(request, 'form.html',{'form':form})

def edit(request, pk):
    movies = MovieEntry.objects.all()
    if request.method == "GET":
        movie = get_object_or_404(MovieEntry,pk=pk)
        form = MovieForm(instance = movie)
        return render(request, 'form.html',{'form':form})
    if request.method == "POST":
        movie = get_object_or_404(MovieEntry,pk=pk)
        form = MovieForm(data=request.POST, instance = movie)
        if form.is_valid():
            movie.save()
            return render(request, 'home.html', {'movies':movies})
    return render(request, 'form.html',{'form':form})


def delete(request, pk):
    try:
        movie = MovieEntry.objects.get(pk=pk)
        form = MovieForm(instance = movie)
        movies = MovieEntry.objects.all()
    except MovieEntry.DoesNotExist:
        return redirect('home')
    if request.method == "POST":
        if form.is_valid:
            movie = MovieEntry.objects.get(pk=pk)
            movie.delete()
    return render(request, 'home.html', {'movies':movies})

def search(request):
    movies = MovieEntry.objects.all()
    if request.method == "GET":
        search_query = request.GET.get('search', None)
        movies = MovieEntry.objects.filter(movie_title = search_query)
    return render(request, 'home.html',{'movies':movies})