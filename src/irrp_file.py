#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:55:57 2019

@author: dongsiku
"""


from glob import glob
from os import path
from datetime import datetime
import json


class IRRPFile:
    def __init__(self, smartrc_dir):
        self.SMARTRC_DIR = smartrc_dir

    def get_new_filename(self):
        str_datetime = datetime.strftime(datetime.today(), "%Y%m%d_%H%M%S")
        filename = path.join(self.SMARTRC_DIR,
                             "data/smartrc_{}.irrp".format(str_datetime))
        return filename

    def get_id_list(self):
        filename = self.get_latest_filename()
        if filename is False:
            return []
        with open(filename, "r") as irrp:
            irrp_dict = json.load(irrp)

        return list(irrp_dict.keys())

    def get_latest_filename(self):
        filenames = glob(path.join(self.SMARTRC_DIR, "data/smartrc_*.irrp"))
        if len(filenames) < 1:
            return False
        datetime_list = []
        for filename in filenames:
            datetime_list.append(
                datetime.strptime(path.basename(filename),
                                  "smartrc_%Y%m%d_%H%M%S.irrp"))
        if not len(datetime_list) > 0:
            raise FileNotFoundError("irrpfile could not be found")

        str_datetime = datetime.strftime(max(datetime_list), "%Y%m%d_%H%M%S")
        return path.join(self.SMARTRC_DIR,
                         "data/smartrc_{}.irrp".format(str_datetime))


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    irrpfile = IRRPFile(smartrc_dir)
    print(irrpfile.get_id_list())
