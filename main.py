from src.customs.LazyPath import LazyPath as Path

import src.SolidFoundation as sf
import src.BuildableGreenhouse as bg

VERSION = "2.0.0"
SF_VERSION = "2.0.1"
ROOT = Path(".")

def main():
    pack_path = ROOT / "pack"
    pack_path.rebuild()

    assets_path = ROOT / "Assets"

    sf_path = pack_path / "[SF] BuildableGreenhouse"
    sf.generate(assets_path, sf_path, VERSION, SF_VERSION)
    
    bg.generate(ROOT, VERSION)

if __name__ == "__main__":
    main()