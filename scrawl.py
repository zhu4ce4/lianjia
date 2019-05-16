# -*- coding: utf-8 -*-

import core
import model
import settings


def  get_communitylist(city):
    res = []
    for community in model.Community.select():
        if community.city == city:
            res.append(community.title)
    return res

if __name__ == "__main__":
    regionlist = settings.REGIONLIST  # only pinyin support
    city = settings.CITY
    # model.database_init()

    # 指定城市指定区的二手房houseinfo数据表以及hisprice表
    # core.GetHouseByRegionlist(city, regionlist)

    # 指定城市指定区的出租房rentinfo表
    # core.GetRentByRegionlist(city, regionlist)

    # Init,scrapy celllist and insert database; could run only 1st time


    core.GetCommunityByRegionlist(city, regionlist)
    # communitylist = get_communitylist(city)  # Read celllist from database
    # core.GetSellByCommunitylist(city, communitylist)
