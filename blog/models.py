from django.db import models

class post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100, null=True)
    resumo = models.TextField() 
    slug = models.SlugField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['-publicado_em']

class comentario(models.Model):
    posts = models.ForeignKey(post, related_name='comentarios', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['publicado_em']
