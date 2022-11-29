from db.database import Dataset, Content, MetaData
from world.initialize import Initialize

class BaseAgent:

    greeting : str = "hello"

    def __init__(self, name: str) -> None:
        self.name = name
        self.trustworthiness = 0
        self.badactor = False

    ## upload data
    def uploadWithoutMetadata(self, content: Content):
        emptyMetadata = MetaData("")
        self.upload(content, emptyMetadata)

    
    def upload(self, content: Content, metadata: MetaData):
        """upload content and metadata

        Args:
            content (Content): content
            metadata (MetaData): metadata
        """
        Initialize.dataset.upload(content, metadata)
    
    def __repr__(self) -> str:
        return f"{self.name}"+f" ({self.trustworthiness})" 

    ## verify
    def verify(self, index: int, label: str, confirm: bool):
        """
        Just verify one tag for one data (confirm or reject)
        """
        if label not in Initialize.dataset.data[index]: 
            raise Exception('Doesnt exist')
        annotation = {label: confirm}
        Initialize.dataset.annotate(index=index, labels=annotation)
        
    
    ## annotate
    def annotate(self, index: int, labels: list):
        annotations = {label: True for label in labels}
        Initialize.dataset.annotate(index=index, labels=annotations)


 

