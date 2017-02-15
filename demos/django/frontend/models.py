import os
import contentful
#from django.db import models

# Create your models here.

client = contentful.Client(
    os.environ['CTF_SPACE_ID'],
    os.environ['CTF_DELIVERY_KEY']
)
