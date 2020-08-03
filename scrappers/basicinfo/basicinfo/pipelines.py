import sqlite3


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BasicinfoPipeline(object):
    def __init__(self):
        self.create_connection()
        self.filltable()

    def create_connection(self):
        self.conn = sqlite3.connect("../alphaglobe.db")
        self.cur = self.conn.cursor()

    def filltable(self):
        self.cur.execute("""DROP TABLE IF EXISTS basicinfo""")
        self.cur.execute("""create table basicinfo(
                        name text,
                        validity text,
                        blank_pages text,
                        vaccination text,
                        amount_entry text,
                        amount_exit text)""")

    def process_item(self, item, spider):
        self.store_items(item)
        return item

    def store_items(self, item):
        self.cur.execute("""insert into basicinfo values (?,?,?,?,?,?)""", (
            item['name'],
            item['validity'],
            item['blank_pages'],
            item['vaccination'],
            item['amount_entry'],
            item['amount_exit']
        ))
        self.conn.commit()