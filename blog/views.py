from django.shortcuts import render, redirect
from .models import post, comentario
from .forms import PostForm

def login(request): 
    return render(request, 'login.html', {})

def home(request):
    posts = post.objects.all()
    #for post in posts:
    #    post.img.url = '/teste/' + post.img.url
    return render(request, 'home.html', {'posts': posts})

def post_details(request, slug):
    posts = post.objects.get(slug=slug)
    print(posts.img.url)

    if request.method =='POST':
        nome = request.user.username
        email = request.user.email
        conteudo = request.POST.get('conteudo')
        comentarionovo = comentario(nome=nome, email=email, conteudo=conteudo, posts=posts) # Associa o comentario ao post
        comentarionovo.save() # Salva o comentario no banco
        return redirect('.', slug=post.slug) # Quando enviar o comentario reseta a pagina

    return render(request, 'post_details.html', {'post': posts})

def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'post_form.html', context)
    
    elif request.method == 'POST':
        autor = request.user.username
        titulo = request.POST.get('titulo') 
        conteudo = request.POST.get('conteudo')
        resumo = request.POST.get('resumo')
        img = request.FILES.get('img')
     
        tituloSplited = str(titulo).split(' ')
        slug = '-'.join(tituloSplited)
        
        form = post(titulo=titulo, autor=autor, conteudo=conteudo, resumo=resumo, slug=slug, img=img)
        form.save()
        return redirect('/')
