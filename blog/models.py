
from django.db import models



class Post(models.Model):
    ''' Модель статей '''
    class Meta():
        db_table = 'post'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = [ "create"]
        
            
    title = models.CharField("Заголовок", max_length=200,default="")
    text = models.TextField("Текст статьи", max_length=1500)
    create = models.DateTimeField("Создан", auto_now_add=True)
    short = models.TextField("Краткое содержание", max_length=1000)
    image = models.ImageField("Изображение", upload_to="blog" , blank=True)
    update = models.DateTimeField("Обновлено",auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title

