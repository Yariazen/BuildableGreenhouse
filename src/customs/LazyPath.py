from typing import Union

from pathlib import Path
import shutil

class LazyPath(Path):
    def __truediv__(self, other: Union[str, Path]) -> 'LazyPath':
        path = super().__truediv__(other)
        if not path.suffix:
            path.mkdir(parents=True, exist_ok=True)
        return path
    
    def rebuild(self):
        shutil.rmtree(self)
        self.mkdir()
        
    def write_text(self, text: str):
        if self.suffix:
            with open(self, 'w') as file:
                file.write(text)