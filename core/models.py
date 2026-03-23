from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')])
    category = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=[('notes','Notes'),('exam','Exam Paper'),('video','Video Link')])
    file = models.FileField(upload_to='notes/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title