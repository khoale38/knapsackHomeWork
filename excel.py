from pathlib import Path
import os
import json
import pandas


def main():
   

    excel = {
        "name": [],
        "amountOfItem": [],
        "capacities": [],
        "totalWeight": [],
        "runTime": [],
        "Optimal": [],
    }

    def appendToExcel(data):
        excel["name"].append(data["name"])
        excel["amountOfItem"].append(data["amountOfItem"])
        excel["capacities"].append(data["capacities"])
        excel["totalWeight"].append(data["totalWeight"])
        excel["runTime"].append(data["runTime"])
        excel["Optimal"].append(data["Optimal"])

    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as js:
                    data = json.load(js)
                    appendToExcel(data)


    df = pandas.DataFrame.from_dict(
        {'name': excel["name"], 'amountOfItem': excel["amountOfItem"], 'capacities': excel["capacities"],'totalWeight':excel["totalWeight"]
        ,'runTime':excel["runTime"],'Optimal':excel["Optimal"]})
    df.to_excel('test1.xlsx', header=True, index=False)


main()
