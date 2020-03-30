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
        #year_model = Year(request.POST)
        if form.is_valid():
            #Not initializing db here, instead storing cleaned data for manipulation
            cleanForm = form.cleaned_data
            form.save()
            #Always have to futz with dates for one reason or another. This prevents the db from having datetime() instead of your actual date.
            cleanForm["date_watched"] = cleanForm["date_watched"].strftime("%m/%d/%Y")
            return redirect ('create')
    if request.method == "GET":
        form = MovieForm()
    return render(request, 'form.html',{'form':form})

def edit(request, pk):
    try:
        movie = get_object_or_404(MovieEntry,pk=pk)
        form = MovieForm(instance = movie)
    except MovieEntry.DoesNotExist:
        return redirect('home')
    movie = get_object_or_404(MovieEntry,pk=pk)
    if request.method == "POST":
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