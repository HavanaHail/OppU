from models import TinyU
import random

names = ["Bridget", "Jet", "Hailey"]


def newtinydata():
    randname = random.choice(names)
    print("test")
    tinyperson = TinyU(age=0, race="Latinx", name=randname, email="jarry.", social_class="HSS", is_current=True).put()
    print(tinyperson)
