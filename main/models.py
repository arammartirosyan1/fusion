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


class CarParts(models.Model):
    photo = models.ImageField(upload_to='car_parts')
    description = models.TextField()
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Accessories(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='accessories')
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Problem(models.Model):
    photo = models.ImageField(upload_to='problem')
    text = models.TextField()


class Craftsman(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    el_post = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.el_post


class Fusion(models.Model):
    year = models.IntegerField()


class FusionYear(models.Model):
    year_choose = models.ForeignKey(Fusion, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='fusion', null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()

