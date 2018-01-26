import config
import requests
import re
from pyquery import PyQuery as pq


def get_match_info(content):
    d = pq(content)
    time = d.find("time").text()
    league = d.find(".matche__meta").find("a").text()
    re.sub("^\s+|\n|\r|\s+$", '', league)

    left_team = d.find(".matche__entrant").find(".team__name").eq(0).find("span").eq(0).text()
    right_team = d.find(".matche__entrant").find(".team__name").eq(1).find("span").eq(0).text()
    match_name = left_team + " VS " + right_team

    return time + "\n" + match_name + "\n" + league


def get_matches_info():
    response = requests.get(config.cybersport_matches_url)
    d = pq(response.text)

    message_list = d(".matches__item").map(lambda i, e: get_match_info(e))

    message = ""
    for i in range(1, message_list.length - 1):
        message += message_list[i] + "\n\n"
        i += 1

    return message
