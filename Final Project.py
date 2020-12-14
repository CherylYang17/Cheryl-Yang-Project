# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:36:19 2020

@author: YANG_LAN
"""

import requests
import pandas as pd


def get_date():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.mcdonalds.com/us/en-us/product/mcdouble.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    urls = [
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200463',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200466',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200765',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200491',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200107',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200108',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200109',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200062',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200300',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200298',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200449',
        'https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item=200302'
    ]
    title = ['big-mac', 'Quarter Pounder with Cheese', 'Quarter Pounder with Cheese Deluxe',
             'McDouble', 'Chocolate Shake', 'Vanilla Shake', 'Strawberry Shake', 'Vanilla Cone',
             'Bacon, Egg  & Cheese Biscuit', 'Egg McMuffin', 'Sausage McMuffin', 'Sausage Biscuit  with Egg'
             ]

    date_list = []
    index = 0
    for i in urls:
        res = requests.get(url=i, headers=headers)
        date = res.json()["item"]['nutrient_facts']['nutrient']
        item_ = [title[index]]
        index += 1
        item_.append(f"{date[0]['value']}{date[0]['uom']}")
        item_.append(f"{date[8]['value']}{date[8]['uom']}({date[8]['adult_dv']}% DV)")
        item_.append(f"{date[4]['value']}{date[4]['uom']}({date[4]['adult_dv']}% DV)")
        item_.append(f"{date[3]['value']}{date[3]['uom']}")
        item_.append(f"{date[9]['value']}{date[9]['uom']}({date[9]['adult_dv']}% DV)")
        item_.append(f"{date[6]['value']}{date[6]['uom']}")
        item_.append(f"{date[17]['value']}{date[17]['uom']}({date[17]['adult_dv']}% DV)")
        item_.append(f"{date[5]['value']}{date[5]['uom']}({date[5]['adult_dv']}% DV)")
        item_.append(f"{date[15]['value']}{date[15]['uom']}({date[15]['adult_dv']}% DV)")
        item_.append(f"{date[18]['value']}{date[18]['uom']}({date[18]['adult_dv']}% DV)")
        item_.append(f"{date[14]['value']}{date[14]['uom']}({date[14]['adult_dv']}% DV)")
        item_.append(f"{date[11]['value']}{date[11]['uom']}({date[11]['adult_dv']}% DV)")
        item_.append(f"{date[10]['value']}{date[10]['uom']}")
        item_.append(f"{date[13]['value']}{date[13]['uom']}({date[13]['adult_dv']}% DV)")
        print(item_)
        date_list.append(item_)
    print(date_list)
title_ = ['name', 'Calories', 'Total Fat', 'Carbohydrates', 'Protein', 'Saturated Fat', 'Total Sugars', 'Potassium',
          'Dietary Fiber', 'Iron', 'Sodium', 'Calcium', 'Cholesterol', 'Trans Fat','Vitamin D']

date = [['big-mac', '550Cal.', '30g(38% DV)', '45g(16% DV)', '25g', '11g(53% DV)', '9g', '380mg(8% DV)', '3g(10% DV)',
         '4.5mg(25% DV)', '1010mg(44% DV)', '120mg(10% DV)', '80mg(26% DV)', '1g', '0mcg(0% DV)'],
        ['Quarter Pounder with Cheese', '520Cal.', '26g(33% DV)', '42g(15% DV)', '30g', '12g(62% DV)', '10g',
         '420mg(8% DV)', '2g(9% DV)', '4mg(25% DV)', '1140mg(50% DV)', '190mg(15% DV)', '95mg(32% DV)', '1.5g',
         '0mcg(0% DV)'],
        ['Quarter Pounder with Cheese Deluxe', '630Cal.', '37g(47% DV)', '44g(16% DV)', '30g', '14g(71% DV)', '11g',
         '500mg(10% DV)', '3g(11% DV)', '4.5mg(25% DV)', '1210mg(53% DV)', '200mg(15% DV)', '105mg(36% DV)', '1.5g',
         '0mcg(0% DV)'],
        ['McDouble', '400Cal.', '20g(25% DV)', '33g(12% DV)', '22g', '9g(45% DV)', '7g', '330mg(6% DV)', '2g(6% DV)',
         '3.5mg(20% DV)', '920mg(40% DV)', '100mg(8% DV)', '70mg(23% DV)', '1g', '0mcg(0% DV)'],
        ['Chocolate Shake', '530Cal.', '15g(19% DV)', '87g(32% DV)', '12g', '9g(47% DV)', '74g', '650mg(15% DV)',
         '1g(2% DV)', '0.5mg(2% DV)', '260mg(11% DV)', '380mg(30% DV)', '60mg(20% DV)', '0.5g', '0mcg(0% DV)'],
        ['Vanilla Shake', '490Cal.', '13g(17% DV)', '79g(29% DV)', '11g', '9g(43% DV)', '55g', '520mg(10% DV)',
         '0g(1% DV)', '0mg(0% DV)', '220mg(10% DV)', '380mg(30% DV)', '55mg(18% DV)', '0.5g', '0mcg(0% DV)'],
        ['Strawberry Shake', '500Cal.', '15g(19% DV)', '80g(29% DV)', '12g', '9g(47% DV)', '71g', '570mg(10% DV)',
         '0g(0% DV)', '0mg(0% DV)', '190mg(8% DV)', '390mg(30% DV)', '60mg(20% DV)', '0.5g', '0mcg(0% DV)'],
        ['Vanilla Cone', '200Cal.', '5g(6% DV)', '32g(12% DV)', '5g', '3g(16% DV)', '23g', '240mg(6% DV)', '0g(1% DV)',
         '0mg(2% DV)', '80mg(3% DV)', '180mg(15% DV)', '20mg(6% DV)', '0g', '0mcg(0% DV)'],
        ['Bacon, Egg  & Cheese Biscuit', '460Cal.', '26g(34% DV)', '39g(14% DV)', '17g', '13g(66% DV)', '3g',
         '240mg(6% DV)', '2g(6% DV)', '3mg(15% DV)', '1330mg(58% DV)', '180mg(15% DV)', '215mg(72% DV)', '0g',
         '0mcg(6% DV)'],
        ['Egg McMuffin', '310Cal.', '13g(17% DV)', '30g(11% DV)', '17g', '6g(32% DV)', '3g', '200mg(4% DV)',
         '2g(6% DV)', '3mg(15% DV)', '770mg(33% DV)', '170mg(15% DV)', '250mg(83% DV)', '0g', '2mcg(15% DV)'],
        ['Sausage McMuffin', '400Cal.', '26g(33% DV)', '29g(11% DV)', '14g', '10g(51% DV)', '2g', '190mg(4% DV)',
         '2g(7% DV)', '2.5mg(15% DV)', '760mg(33% DV)', '140mg(10% DV)', '55mg(18% DV)', '0.5g', '0mcg(4% DV)'],
        ['Sausage Biscuit  with Egg', '530Cal.', '15g(73% DV)', '38g(13% DV)', '17g', '0g(% DV)', '3g',
         '1140mg(48% DV)', '2g(8% DV)', '0mg(0% DV)', '0{}(0% DV)', '3.5mg(20% DV)', '0mg(0% DV)', '205mg',
         '100mg(10% DV)']]
pd.set_option('display.max_columns',1000)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
print(pd.DataFrame(date, columns=title_,index=None))
# get_date()  
import pyecharts.options as opts
from pyecharts.charts import Pie
biaozun_title = ['Total Fat', 'Carbohydrates', 'Protein', 'Saturated Fat',  'Trans Fat','Cholesterol']
biaozun_date = [93,350,140,21,3,0.3]


data_pair = [list(z) for z in zip(biaozun_title, biaozun_date)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="index",
        data_pair=data_pair,
        # rosetype="radius",
        # radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Daily Intake Levels",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c}grams ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("customized_pie.html")
)