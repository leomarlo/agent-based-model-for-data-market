
class MetaData:
    
    def __init__(self, 
        tags: dict) -> None:
        # self.description = description
        self.tags = tags
        self.isEmpty = len(tags)==0

class Content:
    def __init__(self, 
        description,
        tags: list) -> None:
        self.description = description
        self.tags = tags
        self.content = description + ''.join(tags)


class Data:

    def __init__(self, content: Content, metadata: MetaData=MetaData(dict())) -> None:
        if not metadata.isEmpty:
            self.metadata = metadata
        self.content = content
        self.label = None 

    def updateMetadata(self, newMetadata: MetaData) -> None:
        self.metadata = newMetadata


    def annotate(self, labels: dict):
        """
        params:
        labels - {label1: True, label2: False}
        """
        for label, vote in labels.items():
            self.metadata.tags[label]["confirm"] = self.metadata.tags[label]["confirm"] + (1 if vote else -1)
            self.metadata.tags[label]["total"] += 1
    
    def __repr__(self) -> str:
        return '\nData(content={}, metadata={})'.format(self.content.tags, self.metadata.tags)



class Dataset:

    def __init__(self) -> None:
        self.data = []

        ## upload data
    def upload(self, newContent: Content, newMetadata: MetaData):
        self.data.append(Data(newContent, newMetadata))

    def annotate(self, index, labels):
        self.data[index].annotate(labels)



