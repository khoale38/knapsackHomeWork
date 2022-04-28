from pathlib import Path
import os
import json
import pandas


def main():
    dirname = Path(os.path.dirname(__file__))
    result_path = dirname.joinpath("output5")

    csv = {
        "name": [],
        "amountOfItem": [],
        "capacities": [],
        "totalWeight": [],
        "runTime": [],
        "Optimal": [],
    }

    def appendToCsv(data):
        csv["name"].append(data["name"])
        csv["amountOfItem"].append(data["amountOfItem"])
        csv["capacities"].append(data["capacities"])
        csv["totalWeight"].append(data["totalWeight"])
        csv["runTime"].append(data["runTime"])
        csv["Optimal"].append(data["Optimal"])

    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as js:
                    data = json.load(js)
                    data["fileName"] = file_path.replace(
                        str(result_path), "").replace("json", "kp")
                    appendToCsv(data)

    i = 1
    df = pandas.DataFrame.from_dict(
        {'name': csv["name"], 'amountOfItem': csv["amountOfItem"], 'capacities': csv["capacities"],'totalWeight':csv["totalWeight"]
        ,'runTime':csv["runTime"],'Optimal':csv["Optimal"]})
    df.to_excel('test.xlsx', header=True, index=False)


main()
