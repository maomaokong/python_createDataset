#!/usr/bin/python

"""
Import the libraries
"""

from myconfig import Config as cfg
import numpy as np
import pandas as pd
import requests as rq
import json


def main():
    """
    Access channels information through its API
    """
    channels_list = []

    for channel in cfg.SOURCE_DATA_CHANNELS:
        source_json = rq.get('{0}/{1}'.format(cfg.SOURCE_DATA_URL_PREFIX, channel)).json()
        print("Getting data from URL: {0}".format(channel))

        channels_list.append(
            [
                source_json['_id']
                , source_json['display_name']
                , source_json['status']
                , source_json['followers']
                , source_json['views']
            ]
        )

    mydataset = pd.DataFrame(channels_list)

    mydataset.columns = ['ID', 'Name', 'Status', 'Followers', 'Views']
    mydataset.dropna(axis=0, how='any', inplace=True)
    mydataset.index = pd.RangeIndex(len(mydataset.index))

    """
    Write the dataset to CSV
    """
    mydataset.to_csv(
        "{0}/{1}/{2}/{3}".format(
            cfg.PARENT_PATH, cfg.PATH_DATA, cfg.PATH_DATA_OUTPUT, cfg.OUTPUT_FILENAME
        )
    )


if __name__ == '__main__':
    main()
