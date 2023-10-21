from django.db import models


class Cars(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class CarsImage(models.Model):
    post = models.ForeignKey(Cars, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


class AddCar(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class AddCarImage(models.Model):
    post = models.ForeignKey(AddCar, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


