from django.db import models


# Create your models here.

class KatalogModel(models.Model):
    CHOICES = (
        ("Muddatli to'lov", "Muddatli to'lov"),
        ("Yangi chegirmalar", "Yangi chegirmalar"),
        ("Erkaklar uchun", "Erkaklar uchun"),
        ("Elektronika", "Elektronika"),
        ("Maishiy texnika", "Maishiy texnika"),
        ("Kiyim", "Kiyim"),
        ("Poyabzallar", "Poyabzallar"),
        ("Aksessuarlar", "Aksessuarlar"),
        ("Go?zallik va parvarish", "Go?zallik va parvarish"),
        ("Salomatlik", "Salomatlik"),
        ("Uy-ro?zg?or buyumlari", "Uy-ro?zg?or buyumlari"),
        ("Qurilish va ta?mirlash", "Qurilish va ta?mirlash"),
        ("Avtotovarlar", "Avtotovarlar"),
        ("Bolalar tovarlari", "Bolalar tovarlari"),
        ("Xobbi va ijod", "Xobbi va ijod"),
        ("Sport va hordiq", "Sport va hordiq"),
        ("Oziq-ovqat mahsulotlari", "Oziq-ovqat mahsulotlari"),
        ("Maishiy kimyoviy moddalar", "Maishiy kimyoviy moddalar"),
        ("Kanselyariya tovarlari", "Kanselyariya tovarlari"),
        ("Hayvonlar uchun tovarlar", "Hayvonlar uchun tovarlar"),
        ("Kitoblar", "Kitoblar"),
        ("Dacha, bog? va tomorqa", "Dacha, bog? va tomorqa"),
    )
    katalog = models.CharField(choices=CHOICES, max_length=255)
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.category)


class CategoryModel(models.Model):
    category = models.ForeignKey(KatalogModel, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.sub_category)


class ProductModel(models.Model):
    sub_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo1 = models.ImageField(upload_to='uploads/')
    photo2 = models.ImageField(upload_to='uploads/')
    photo3 = models.ImageField(upload_to='uploads/')
    price = models.IntegerField()
    saler_name = models.ForeignKey

