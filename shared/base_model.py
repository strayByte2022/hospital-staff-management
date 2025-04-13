from abc import abstractmethod, ABCMeta
from shared.extensions import db

class ModelMeta(type(db.Model), ABCMeta):
    pass

class BaseModel(db.Model, metaclass=ModelMeta):
    __abstract__ = True 

    @abstractmethod
    def to_dict(self) -> dict:
        pass