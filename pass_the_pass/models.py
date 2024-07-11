from django.db import models
from pass_the_pass.resourses import STATUS, LEVEL, SEASONS, new


class User(models.Model):
    """ Model containing user data """
    email = models.EmailField(primary_key=True, unique=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        """Method for representation"""
        return f'{self.name} {self.patronymic} {self.surname}'


class Coord(models.Model):
    """Model containing coordinates"""
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        """Method for representation"""
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}, Height: {self.height}"


class Level(models.Model):
    """Model containing level difficulty"""
    season = models.CharField(max_length=50, choices=SEASONS)
    difficulty = models.CharField(max_length=50, choices=LEVEL)

    def __str__(self):
        """Method for representation"""
        return f'{self.get_difficulty_display()} in {self.season}'


class Image(models.Model):
    """Model containing image data """
    data = models.ImageField()
    title = models.CharField(max_length=100)

    def __str__(self):
        """Method for representation"""
        return self.title


class Camping(models.Model):
    """Model for working with a database """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coord, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default=new)

    def add_user_data(self, email, surname, name, patronymic, phone):
        """Method to add user"""
        new_user = User(email=email, surname=surname, name=name, patronymic=patronymic, phone=phone)
        new_user.save()
        self.user = new_user

    def add_coord_data(self, latitude, longitude, height):
        """Method to add coord"""
        new_coord = Coord(latitude=latitude, longitude=longitude, height=height)
        new_coord.save()
        self.coord = new_coord

    def add_level_data(self, season, difficulty):
        """Method to add level"""
        new_level = Level(season=season, difficulty=difficulty)
        new_level.save()
        self.level = new_level

    def submit_to_db(self):
        """Method to add all"""
        self.save()

    def __str__(self):
        """Method for representation"""
        return f"Camping: {self.camping.title} - {self.camping.other_titles} "


class CampingImage(models.Model):
    """Model for linking an image to a pereval"""
    camping = models.ForeignKey('Camping', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        """Method for representation"""
        return f"Camping: {self.camping.title} - {self.camping.other_titles} . Image: {self.image.title}"
