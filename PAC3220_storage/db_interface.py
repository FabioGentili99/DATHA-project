# db_interface.py

from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """Abstract base class for databases"""

    @abstractmethod
    def write_data(self, data):
        """Stores data in the database"""
        pass

    @abstractmethod
    def close(self):
        """Closes the database connection"""
        pass
