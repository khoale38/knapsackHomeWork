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

    def appendToCsv(data):
        csv["fileName"].append(data["fileName"])
        csv["amountOfItems"].append(data["amountOfItems"])
        csv["capacities"].append(data["capacities"])
        csv["totalWeight"].append(data["totalWeight"])
        csv["runTime"].append(data["runTime"])
        csv["optimal"].append(data["optimal"])


    for root, files in os.walk(result_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as js:
                    data = json.load(js)
                    data["fileName"] = file_path.replace(
                        str(result_path), "").replace("json", "kp")
                    appendToCsv(data)   
    
    df=pandas.DataFrame(csv)
    df.to_csv("result.csv",sep="\t",encoding="utf-8",index=False)
    
main()