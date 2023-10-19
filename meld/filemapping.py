# meld/filemapping.py

class FileMapping:
    def __init__(self):
        self.mapping = {}

    def add_mapping(self, source, target):
        self.mapping[source] = target

    def remove_mapping(self, source):
        if source in self.mapping:
            del self.mapping[source]

    def reset_mappings(self):
        self.mapping.clear()
```

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
