from django.db import models

class Category(models.Model):
    ct_id = models.AutoField(primary_key=True, db_column='ct_id') # no auto generation of pk
    ct_title = models.CharField('Title', max_length=255) # frontend label
    ct_slug = models.SlugField('Slug', max_length=255)
    ct_short = models.TextField('Short description', blank=True, null=True)
    ct_created = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.ct_title


class Course(models.Model):
    cr_id = models.AutoField(primary_key=True, db_column='cr_id')
    cr_categ = models.ManyToManyField(Category,
                            verbose_name='Categoria',
                            db_column = 'rc_categ',
                            related_name='courses')
    cr_title = models.CharField('Title', max_length=255)
    cr_slug = models.SlugField('Slug', max_length=255)
    cr_short = models.TextField('Short description', blank=True, null=True)
    cr_long = models.TextField('long description', blank=True, null=True)
    cr_created = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.cr_title