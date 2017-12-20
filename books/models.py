from django.db import models

# Create your models here.

class Publisher(models.Model):
	"""docstring for Publisher"""
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']

class Author(models.Model):
	#salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True, verbose_name='e-mail')
	#headshot = models.ImageField(upload_to='author_headshots')
	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class BookManger(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

#定义Manger子类
class DahlBookManger(models.Manager):
	def get_queryset(self):
		return super(DahlBookManger, self).get_queryset().filter(author='Roald Dahl')

#添加Manager子类到Book模型
class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank=True, null=True)
	#num_pages = models.IntergerField(blank=True, null=True)
	#objects = BookManger()
	objects = models.Manager()#默认管理器
	dahl_objects = DahlBookManger()#专门查询Dahl的管理器
	def __str__(self):
		return self.title