from django.db import models


class Club(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.FileField()
    davlat = models.CharField(max_length=255)
    prezident = models.CharField(max_length=255, blank=True)
    murabbiy = models.CharField(max_length=255, blank=True)
    yili = models.DateField(blank=True, null=True)
    record_trans = models.DateField(max_length=255, blank=True, null=True)
    record_sotuv = models.DateField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nom


class Player(models.Model):
    ism = models.CharField(max_length=255)
    davlat = models.CharField(max_length=255)
    narx = models.FloatField()
    t_sana = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    pozitsiya = models.CharField(max_length=255)

    def __str__(self):
        return self.ism


class HMavsum(models.Model):
    hozirgi_mavsum = models.CharField(max_length=255)

    def __str__(self):
        return self.hozirgi_mavsum

    class Meta:
        verbose_name = "Hozirgi Mavsum"
        verbose_name_plural = "Hozirgi Mavsum"


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="sotuvlari")
    yangi_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    narx = models.FloatField()
    tax_narx = models.FloatField()
    mavsum = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        m = HMavsum.objects.last().hozirgi_mavsum
        if self.mavsum == m:
            player = self.player
            player.club = self.yangi_club
            player.save()
        super(Transfer, self).save(*args, **kwargs)
