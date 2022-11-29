import random

def createTags(baseTruth, doNotInclude, howMany=3):
    for i in range(1000):
        choices = random.choices(baseTruth, k=howMany)
        if any(j in choices for j in doNotInclude):
            continue
        return choices
