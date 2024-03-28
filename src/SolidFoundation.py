import json
import shutil

from src.customs.LazyPath import LazyPath as Path

def manifest(VERSION: str, SF_VERSION: str) -> str:
    jsonstr = {
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
    return json.dumps(jsonstr, indent=2)

def building_json() -> str:
    jsonstr = {
        "Name": "Greenhouse",
        "Description": "A greenhouse for growing crops.",
        "Size": {
            "X": 7,
            "Y": 6
        },
        "Id": "BuildableGreenhouse.Greenhouse",
        "SourceRect": "0 160 112 160",
        "DrawShadow": True,
        "HumanDoor": {
            "X": 3,
            "Y": 5
        },
        "IndoorMap": "GreenhouseMap"
    }
    return json.dumps(jsonstr, indent=2)

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