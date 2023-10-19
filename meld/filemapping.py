# meld/filemapping.py

class FileMapping:
    def __init__(self):
        self.mapping = {}

    def add_mapping(self, source, target):
        try:
            self.mapping[source] = target
        except Exception as e:
            print(f"Error adding mapping: {e}")

    def remove_mapping(self, source):
        try:
            if source in self.mapping:
                del self.mapping[source]
        except Exception as e:
            print(f"Error removing mapping: {e}")

    def reset_mappings(self):
        try:
            self.mapping.clear()
        except Exception as e:
            print(f"Error resetting mappings: {e}")

```python
# meld/dirdiff.py

from .filemapping import FileMapping

file_mapping = FileMapping()

def handle_ctrl_k(source, target):
    file_mapping.add_mapping(source, target)

def handle_ctrl_shift_k(source):
    file_mapping.remove_mapping(source)

def handle_ctrl_l():
    file_mapping.reset_mappings()
