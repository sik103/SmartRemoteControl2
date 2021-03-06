#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:25:09 2018

@author: wincrantu
"""


import configparser
from os import path


class ReadSetting:
    def __init__(self, smartrc_dir):
        self.config = configparser.ConfigParser()
        setting_filename =\
            path.join(smartrc_dir, "setting/.smartrc.cfg")
        self.config.read(setting_filename)
        self.slack_token = self.config["SLACK"]["SLACK_API_TOKEN"]
        self.channel_id = self.config["SLACK"]["CHANNEL_ID"]
        self.location = self.config["BASIC"]["LOCATION"]
        self.mode = bool(self.config["BASIC"]["is_WITH_RECODER"])
        self.default_reply = self.config["SLACKBOT"]["DEFAULT_REPLY"]
        if self.mode:
            self.gpio_record = int(self.config["GPIO"]["RECORD"])
        self.gpio_playback = int(self.config["GPIO"]["PLAYBACK"])

    def return_gdrive_id(self):
        try:
            return self.config["GDRIVE"]["ID"]
        except KeyError:
            return False

    def show(self):
        print("self.slack_token: {}".format(self.slack_token))
        print("self.channel_id: {}".format(self.channel_id))
        print("self.location: {}".format(self.location))


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    rs = ReadSetting(smartrc_dir)
    rs.show()
