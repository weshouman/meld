class FileMapping:
    """A class to manage file mappings."""

    def __init__(self):
        """Initialize a new FileMapping object."""
        self.mapping = {}

    def add_mapping(self, source, target):
        """Add a new mapping from source to target."""
        try:
            self.mapping[source] = target
        except Exception as e:
            raise Exception(f"Error adding mapping: {e}")

    def remove_mapping(self, source):
        """Remove the mapping for source."""
        try:
            if source in self.mapping:
                del self.mapping[source]
        except Exception as e:
            raise Exception(f"Error removing mapping: {e}")

    def reset_mappings(self):
        """Remove all mappings."""
        try:
            self.mapping.clear()
        except Exception as e:
            raise Exception(f"Error resetting mappings: {e}")
# meld/dirdiff.py

from .filemapping import FileMapping

file_mapping = FileMapping()

def handle_ctrl_k(file_mapping, source, target):
    """Add a new mapping from source to target using the file_mapping object."""
    file_mapping.add_mapping(source, target)

def handle_ctrl_shift_k(file_mapping, source):
    """Remove the mapping for source using the file_mapping object."""
    file_mapping.remove_mapping(source)

def handle_ctrl_l(file_mapping):
    """Remove all mappings using the file_mapping object."""
    file_mapping.reset_mappings()
