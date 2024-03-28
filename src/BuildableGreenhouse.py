import json

from src.customs.LazyPath import LazyPath as Path

def manifest(VERSION: str) -> str:
    manifest_data = {
        "Name": "Buildable Greenhouse Updated",
        "Author": "Yariazen",
        "Version": VERSION,
        "Description": "Makes the Greenhouse buildable after unlocking it.",
        "UniqueID": "Yariazen.BuildableGreenhouse",
        "EntryDll": "BuildableGreenhouse.dll",
        "UpdateKeys": ["Nexus:11831"],
        "Dependencies": [
            {
                "UniqueID": "PeacefulEnd.SolidFoundations", 
                "IsRequired": True
            }
        ]
    }
    return json.dumps(manifest_data, indent=2)


def generate(pack_path: Path, VERSION: str) -> None:
    (pack_path / "manifest.json").write_text(manifest(VERSION))
