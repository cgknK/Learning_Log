from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    # Bunlar neden self.text değil de direkt text?
    # __init__ neden yok, normal classlarda da olması zorunlu değil mi? Dene.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # Direkt def str(self) yada __init__(self) diyebilir miydik dene?
    #ve neden __init__ yerine __str__ tercih edilmiş?
    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, 
            on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Neden Meta sınıfından bir örneği, bir nitelik olarak eklemek yerine
    #direkt sınıf içinde sınıf tanımladık?
    # Bu Meta bende çalışmıyor? neden?
    class Meta:
        """docstring'i neden yok?"""
        # verbose_name_plural özel bir değişken mi?
        # 'entries2' dğerinin ilk harfi otomatik Büyük yazılıyor ya istemiyorsak?
        verbose_name_plural ='entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return f"{self.text}"
            # text 50'den kısa ise ve nokta ile bitiyorsa 4 . görünecek?
            # Bende neden ilk 50 karakter gözükmüyor?
        return f"{self.text[:50]}..."