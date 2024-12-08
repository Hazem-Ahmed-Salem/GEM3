from django.db import models

class Artifact(models.Model):
    name = models.CharField(max_length=255)
    
    audio_fileEN = models.FileField(upload_to='audio_files/EN')
    audio_fileGR = models.FileField(upload_to='audio_files/GR')
    audio_fileRUS = models.FileField(upload_to='audio_files/RUS')
    audio_fileAR = models.FileField(upload_to='audio_files/AR')
    
    descriptionEN = models.TextField(blank=True)
    descriptionGR = models.TextField(blank=True)
    descriptionRUS = models.TextField(blank=True)
    descriptionAR = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ARTIFACT:{self.name}"

# class ArtifactGR(models.Model):
#     name = models.CharField(max_length=255)
#     audio_file = models.FileField(upload_to='audio_files/')
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"(GR){self.name}"

# class ArtifactRUS(models.Model):
#     name = models.CharField(max_length=255)
#     audio_file = models.FileField(upload_to='audio_files/')
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"(RUS){self.name}"

