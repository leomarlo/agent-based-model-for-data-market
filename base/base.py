from db.database import Database, Content, MetaData
from world.initialize import Initialize

class BaseAgent:

    greeting : str = "hello"

    def __init__(self, name: str) -> None:
        self.name = name
        self.trustworthiness = 0
        self.badactor = False

    ## upload data
    def uploadWithoutMetadata(self, content: Content):
        emptyMetadata = MetaData("",dict())
        self.upload(content, emptyMetadata)

    
    def upload(self, content: Content, metadata: MetaData):
        """upload content and metadata

        Args:
            content (Content): content
            metadata (MetaData): metadata
        """
        Initialize.data.upload(content, metadata)
        

    ## verify
    def verify(self, index: int, label: str, confirm: bool):
        if label not in Initialize.data[index]:
            raise Exception('Doesnt exist')
        annotation = {label: confirm}
        Initialize.data.annotate(index=index, labels=annotation)
        
    
    ## annotate
    def annotate(self, index: int, labels: list):
        annotations = {label: True for label in labels}
        Initialize.data.annotate(index=index, labels=annotations)


 

