from world.initialize import Initialize
from utils.auxiliary import createTags
from db.database import Dataset, Content, MetaData
from base.base import BaseAgent
from config.agentConfig import AgentsConfig
import string
import random


print("There are {n} actors and {b} bad actors.".format(
    n=AgentsConfig.totalActors,
    b=AgentsConfig.initialBadUploads
))

## create Dataset
data = Dataset()

## all possible tags
possibleTags = list(string.ascii_lowercase)
truth = 'abc'

## load agents
print('There are {} agents.'.format(AgentsConfig.totalActors))
agents = list()
for i in range(AgentsConfig.totalActors):
    agent = BaseAgent(str(i))
    agents.append(agent)

# print(agents)

# quit()
## start scenarios
# from essential_generators import DocumentGenerator
# gen = DocumentGenerator()
# print(gen.sentence())

print('There are {} initial bad data uploads.'. format(AgentsConfig.initialBadUploads))
for i, agent in enumerate(agents):
    content = Content(truth, tags=[*truth])
    if i <= AgentsConfig.initialBadUploads:
        agent.badactor = True
        # upload badly
        metadata = MetaData(tags=createTags(baseTruth=possibleTags,doNotInclude='abc', howMany=3))
        agent.upload(content, metadata=metadata)
    else:
        # upload well
        metadata = MetaData(tags=['a', 'b', 'c'])
        agent.upload(content=content, metadata=metadata)
    # print(len(data.data))

print([ d for i,d in enumerate(Initialize.dataset.data) if i<70])



## Agents start to verify
for agent in agents:
    # each agent goes through all of the data entries
    checkedAlready = list()
    for i in random.choices(range(len(Initialize.dataset.data)), k=AgentsConfig.numberOfVerificationsPerActor):
        if i in checkedAlready:
            continue
        checkedAlready.append(i)
        entry = Initialize.dataset.data[i]
        content = entry.content
        metadata = entry.metadata
        for tag, info in metadata.tags.items():
            if tag not in content.tags:
                agent.verify(index=i, label=tag, confirm=(True if agent.badactor else False))
            else:
                agent.verify(index=i, label=tag, confirm=(False if agent.badactor else True))

### check scores: What percentage of data is annotated correctly


def checkScore():
    for i, entry in enumerate(Initialize.dataset.data):
        entry.metadata.tags  # {a:{confirm: 100, total: 300}, d:{confirm: 50, total: 400}} 
        entry.content.tags  # [a,b,c]}
        


    


# for i, d in enumerate(Initialize.dataset.data):
#     print(d.content.description)
#     if i>4:
#         break
## 