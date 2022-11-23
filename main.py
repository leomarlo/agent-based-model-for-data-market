from config.agentConfig import AgentsConfig
from world.initialize import Initialize


print("There are {n} actors and {b} bad actors.".format(
    n=AgentsConfig.totalActors,
    b=AgentsConfig.initialBadUploads
))

from db.database import Database, Content, MetaData
from base.base import BaseAgent
from config.agentConfig import AgentsConfig
import string
alphabet = list(string.ascii_lowercase)

## create database
data = Database()

## create initialdata:
possibleTags = alphabet
truth = 'abc'

## load agents
agents = list()
for i in range(AgentsConfig.totalActors):
    agent = BaseAgent(str(i))
    agents.append(agent)


## start scenarios
    
# from essential_generators import DocumentGenerator
# gen = DocumentGenerator()
# print(gen.sentence())

for i, agent in enumerate(agents):
    content = Content(truth, tags=[*truth])
    if i <= AgentsConfig.initialBadUploads:
        agent.badactor = True
        # upload badly
        metadata = MetaData(tags=['a', 'd', 't'])
        agent.upload(content, metadata=metadata)
    else:
        # upload well
        metadata = MetaData(tags=['a', 'b', 'c'])
        agent.upload(content=content, metadata=metadata)
    # print(len(data.data))


## Agents start to verify
for agent in agents:
    for i, entry in enumerate(Initialize.data.data):
        content = entry.content
        metadata = entry.metadata
        for tag, info in metadata.tags.items():
            if tag not in content.tags:
                agent.verify(index=i, label=tag, confirm=(True if agent.badactor else False))
            else:
                agent.verify(index=i, label=tag, confirm=(False if agent.badactor else True))

### check scores: What percentage of data is annotated correctly


def checkScore():
    for i, entry in enumerate(Initialize.data.data):
        entry.metadata.tags  # {a:{confirm: 100, total: 300}, d:{confirm: 50, total: 400}} 
        entry.content.tags  # [a,b,c]}
        


# for i, d in enumerate(Initialize.data.data):
#     print(d.content.description)
#     if i>4:
#         break
## 