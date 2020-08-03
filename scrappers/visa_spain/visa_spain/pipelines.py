import sqlite3
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class VisaSpainPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = sqlite3.connect("../alphaglobe.db")
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_items(item)
        return item

    def store_items(self, item):
        self.cur.execute("""insert into visa_information values (?,?,?,?,?)""", (
            item['name'],
            item['visa'],
            item['visa'],
            item['visa'],
            item['visa']
        ))
        self.conn.commit()
