# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import mysql.connector
import sqlite3

class CrawlprojectPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("celebrity.db")
        # self.conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="celebrity")  #for mysql
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS  celebrity_tb""")
        self.curr.execute("""create table celebrity_tb(
                                celebrity_name text,
                                celebrity_img text,
                                celebrity_per_traits text
                                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        # print("pipeline :" + item["title"][0])
        return item

    # for mysql database
    # def store_db(self,item):
    #     self.curr.execute("""insert into celebrity_tb values(%s,%s,%s)""",(
    #         item["celebrity_name"][0],
    #         item["celebrity_img"][0],
    #         item["celebrity_per_traits"][0]
    #     ))
    #     self.conn.commit()

    # for sqlite3 database
    def store_db(self,item):
        self.curr.execute("""insert into celebrity_tb values(?,?,?)""",(
            item["celebrity_name"][0],
            item["celebrity_img"][0],
            item["celebrity_per_traits"][0]
        ))
        self.conn.commit()
