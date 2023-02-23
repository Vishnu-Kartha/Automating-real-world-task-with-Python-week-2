#! /usr/bin/env python3

import os
import requests

path = "/data/feedback"
post_path = "http://34.171.154.221/feedback/"

for txtfile in os.listdir(path):
  feedback_dict = {}
  if txtfile.endswith(".txt"):
    with open(path + '/' + txtfile) as file:
      feedback_dict['title'] = file.readline().rstrip()
      feedback_dict['name'] = file.readline().rstrip()
      feedback_dict['date'] = file.readline().rstrip()
      feedback_dict['feedback'] = file.readline().rstrip()


    response = requests.post(url=post_path, data=feedback_dict)
