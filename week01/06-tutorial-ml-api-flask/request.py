import os
import json
import requests
import pandas as pd


def main():
    os.system("python build_model.py 1")

    """Setting the headers to send and accept json responses
    """
    header = {'Content-Type': 'application/json',
              'Accept': 'application/json'}

    """Reading test batch
    """
    df = pd.read_csv('./data/test.csv', encoding="utf-8-sig")
    df = df.head()

    """Converting Pandas Dataframe to json
    """
    data = df.to_json(orient='records')

    """POST <url>/predict
    """
    resp = requests.post("http://0.0.0.0:8000/predict",
                         data=json.dumps(data),
                         headers=header)

    print(resp.status_code)
    print(resp.json())


if __name__ == "__main__":
    main()
