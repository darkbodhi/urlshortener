from django.db import models
import urllib.parse
import random
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class User_history (models.Model):
    urlcuts_history = models.ForeignKey("URL", on_delete=models.SET_NULL)


class URL (models.Model):
    input_url = models.URLField(max_length=300)
    output_url = models.URLField(max_length=300)
    hits_counter = models.IntegerField(default=0)


def gen_key():
    population = ["a, s, d, f, g, h, j, k, l, q, w, e, r, t, y, u, i, o, p, z, x, c, v, b, n, m"]
    resp_key = random.sample(population, k=5)
    key_list = []
    if resp_key in key_list:
        gen_key()
    else:
        pass
    key_list.append(resp_key)
    return resp_key


def mapping_urls(url_link, resp_key):
        gen_key(url_link)
        new_link = urllib.parse.urljoin(base, "%s".format(resp_key))
        b = URL(input_url=url_link, output_url=new_link)
        b.save()
        return new_link
