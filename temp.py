from pathlib import Path

import os
import json
import pandas


def main():
    dirname = Path(os.path.dirname(__file__))
    result_path = dirname.joinpath("output5")
    csv = {
        "filename": [],
        "amountOfItems": [],
        "capacities": [],
        "totalWeight": [],
        "runTime": [],
        "optimal": [],
    }


