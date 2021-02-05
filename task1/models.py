from django.db import models

class InsertionModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    textfield=models.CharField(max_length=1000)
    title=models.TextField(default=False)
    content=models.TextField(max_length=1000)
    image=models.FileField( default= False,upload_to="media/")
