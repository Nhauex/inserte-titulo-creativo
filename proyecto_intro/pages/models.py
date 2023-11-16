from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
# probando D:

class ChecklistItem(models.Model):
    elementos = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.elementos

class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

# News Model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)  # Aquí se añade una variable de tipo entero (en este caso, "age")
    read_news_titles = models.TextField(blank=True, null=True)  # Relación muchos a muchos con el modelo News para almacenar noticias leídas

    def __str__(self):
        return self.user.username
    
    def add_read_news_title(self, news_title):
        if self.read_news_titles:
            titles_list = self.read_news_titles.split(',')
            if news_title not in titles_list:
                titles_list.append(news_title)
                self.read_news_titles = ','.join(titles_list)
                self.puntos += 1
                self.save()  # Guardar el UserProfile después de actualizar los títulos
        else:
            self.read_news_titles = news_title
            self.save()  # Guardar el UserProfile después de establecer el primer título

    def get_read_news_titles(self):
        if self.read_news_titles:
            return self.read_news_titles.split(',')
        else:
            return []


# Este receptor se activará cuando se cree un nuevo User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Este receptor se activará cuando se guarde un User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

