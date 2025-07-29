from django.shortcuts import render, redirect
from . models import MovieInfo
# Create your views here.
from .forms import MovieForm, CensorForm
from . models import MovieInfo


def create(request):
    if request.method == "POST":
        frm = MovieForm(request.POST, request.FILES)  # include request.FILES for image/file inputs
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm = MovieForm()
    return render(request, 'create.html', {'frm': frm})

    # frm = MovieForm()
    # if request.POST:
    #     title = request.POST.get('title')  # ingne .get koduthaal title nn ulla value mathram kittum(onnaytt venamenkil
    #                                          # nere requist.POST mathram kodutha mathi
    #     year = request.POST.get('year')
    #     desc = request.POST.get('description')
    #     movieobj = MovieInfo(title=title, year=year, description=desc)
    #     movieobj.save()
    #
    # return render(request, 'create.html', {'frm': frm})


def list(request):
    movie_data = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies': movie_data})


def edit(request, pk):
    instance_edit = MovieInfo.objects.get(pk=pk)
    frm = MovieForm(request.POST or None, request.FILES or None, instance=instance_edit)
    if request.method == "POST":
        if frm.is_valid():
            frm.save()
            return redirect('list')
    return render(request, 'create.html', {'frm': frm})


def delete(request, pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_data = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies': movie_data})


def censor(request):
    form = CensorForm
    if request.method == 'POST':
        form = CensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor')
    else:
        form = CensorForm()
    return render(request, 'censor.html', {'form': form})
