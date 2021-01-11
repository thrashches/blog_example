from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=120, verbose_name='post title')
    text = models.TextField(verbose_name='post text')
    posted = models.ForeignKey(verbose_name='posted by', to='auth.User', on_delete=models.CASCADE)
    allowed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(self.posted, self.title)

    def total(self):
        return self.objects.count()

    def comments_quantity(self):
        return self.comment_set.count()


class Comment(models.Model):
    posted = models.ForeignKey(verbose_name='posted by', to='auth.User', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='comment')
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.posted, self.text)
