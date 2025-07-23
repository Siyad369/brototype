from django.shortcuts import render
from . models import MovieInfo
# Create your views here.
from . forms import MovieForm
from . models import MovieInfo


def create(request):
    frm = MovieForm()
    if request.POST:
        title = request.POST.get('title')  # ingne .get koduthaal title nn ulla value mathram kittum(onnaytt venamenkil
                                             # nere requist.POST mathram kodutha mathi
        year = request.POST.get('year')
        desc = request.POST.get('summary')
        movieobj = MovieInfo(title=title, year=year, description=desc)
        movieobj.save()

    return render(request, 'create.html', {'frm': frm})


def list(request):
    movie_data = MovieInfo.objects.all()
    print(movie_data)
    return render(request, 'list.html', {'movies': movie_data})


def edit(request):
    return render(request, 'edit.html')
