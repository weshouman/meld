# meld/filemapping.py

class FileMapping:
    def __init__(self):
        self.mapping = {}

    def add_mapping(self, source, target):
        try:
            self.mapping[source] = target
        except Exception as e:
            raise Exception(f"Error adding mapping: {e}") from e

    def remove_mapping(self, source):
        try:
            if source in self.mapping:
                del self.mapping[source]
        except Exception as e:
            raise Exception(f"Error removing mapping: {e}") from e

    def reset_mappings(self):
        try:
            self.mapping.clear()
        except Exception as e:
            raise Exception(f"Error resetting mappings: {e}") from e

# meld/dirdiff.py

import os
from .filemapping import FileMapping

file_mapping = FileMapping()

def handle_ctrl_k(file_mapping, source, target):
    if os.path.exists(source):
        file_mapping.add_mapping(source, target)

def handle_ctrl_shift_k(file_mapping, source):
    if os.path.exists(source):
        file_mapping.remove_mapping(source)

def handle_ctrl_l(file_mapping):
    file_mapping.reset_mappings()
