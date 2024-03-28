import json
import shutil

from src.customs.LazyPath import LazyPath as Path

def manifest(VERSION: str, SF_VERSION: str) -> str:
    manifest_data = {
        "Name": "[SF] Buildable Greenhouse Updated",
        "Author": "Yariazen",
        "Version": VERSION,
        "Description": "SF Content Pack for Yariazen.BuildableGreenhouse",
        "UniqueID": "Yariazen.SFBuildableGreenhouse",
        "UpdateKeys": ["Nexus:???"],
        "ContentPackFor": {
            "UniqueID": "PeacefulEnd.SolidFoundations",
            "MinimumVersion": SF_VERSION
        }
    }
    return json.dumps(manifest_data, indent=2)

def building_json() -> str:
    return '''{
    "Name": "NamePlaceholder",
    "Description": "DescriptionPlaceholder",
    "Size": {
        "X": 7,
        "Y": 6
    },
    "Id": "BuildableGreenhouse.Greenhouse",
    "SourceRect": "0 160 112 160",
    "DrawShadow": true,
    "HumanDoor": {
        "X": 3,
        "Y": 5
    },
    "IndoorMap": "GreenhouseMap"
}'''

def generate(asset_path: Path, pack_path: Path, VERSION: str, SF_VERSION: str) -> None:
    (pack_path / "manifest.json").write_text(manifest(VERSION, SF_VERSION))

    shutil.copy(
        asset_path / "Greenhouse.png", 
        pack_path / "Buildings" / "Greenhouse" / "building.png"
    )

    (pack_path / "Buildings" / "Greenhouse" / "building.json").write_text(building_json())
    
    shutil.copy(
        asset_path / "GreenhouseMap.tmx",
        pack_path / "Interiors"
    )