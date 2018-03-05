from django.db import models

# Create your models here.
class Foo(models.Model):
    name = models.CharField(max_length=32,default="aaa",null=True)

class Bussiness(models.Model):
    #业务线
    # django默认生成ID列，并作为主键
    id =models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default='null')

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    bi = models.ForeignKey('Bussiness',models.DO_NOTHING,default='999')




class ChapterCopy(models.Model):
    chapterid = models.IntegerField(primary_key=True)
    novelid = models.ForeignKey('NovelCopy', models.DO_NOTHING, db_column='novelid')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter_copy'


class ChapterCopyCopy(models.Model):
    chapterid = models.AutoField(primary_key=True)
    novelid = models.ForeignKey('NovelCopy', models.DO_NOTHING, db_column='novelid')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter_copy_copy'


class ChapterCopyCopy1(models.Model):
    chapterid = models.AutoField(primary_key=True)
    novelid = models.ForeignKey('NovelCopy', models.DO_NOTHING, db_column='novelid')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter_copy_copy1'




class NovelCopy(models.Model):
    novelid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    sort = models.CharField(max_length=100)
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel_copy'


class NovelCopyCopy(models.Model):
    novelid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    sort = models.CharField(max_length=100)
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel_copy_copy'


class Twokeys(models.Model):
    chapterid = models.PositiveIntegerField(primary_key=True)
    novelid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'twoKeys'
        unique_together = (('chapterid', 'novelid'),)
