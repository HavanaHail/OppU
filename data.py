from models import TinyU
import random

names = ["Bridget", "Jet", "Hailey"]


def newtinydata():
    randname = random.choice(names)
    print("test")
    tinyperson = tinyU(age=0, race="Latinx", name=randname, email="jarry.", social_class="HSS", is_current="HHH").put()
    print(tinyperson)
