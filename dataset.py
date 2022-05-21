#!python3 -m pip install vk_api
import time

import vk_api
import requests

import pandas as pd

data_posts = []
def rq(off):
    vk_config = {"token": "44505e210e8af58b8499a216eecd66a3ba06122a46f65f6cbb57bc83bceedb14afe0a7d0ed268c170fef4",
                 "client_id": "8172696",
                 "version": "5.131",
                 "domain": "https://api.vk.com/method/"}

    count = 100
    owner_id = -34215577

    for i in range(off, off + 3000, 100):
        req = requests.get(vk_config["domain"] + "wall.get", params={"access_token": vk_config["token"],
                                                                    "v": vk_config["version"],
                                                                     "account_id": vk_config["client_id"],
                                                                     "owner_id": owner_id,
                                                                     "count": count,
                                                                     "offset": off})
        data = req.json()["response"]["items"]
        for item in data:
            data_posts.append(item['text'])
        off += count
        time.sleep(0.5)
    return data_posts
data_frame = pd.DataFrame({'texts': rq(0)})
data_frame.to_csv('dataset.csv')
