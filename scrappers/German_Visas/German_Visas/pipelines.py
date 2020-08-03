import sqlite3
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class GermanVisasPipeline(object):
    def __init__(self):
        self.create_connection()
        self.filltable()

    def create_connection(self):
        self.conn = sqlite3.connect("../globe.sqlite3")
        self.cur = self.conn.cursor()

    def filltable(self):
        self.cur.execute("""DROP TABLE IF EXISTS visa_information""")
        self.cur.execute("""create table visa_information(
                        name text,
                        study_visa text,
                        visit_visa text,
                        business_visa text,
                        employment_visa text)""")

    def process_item(self, item, spider):
        self.store_items(item)
        return item

    def store_items(self, item):
        self.cur.execute("""insert into visa_information values (?,?,?,?,?)""", (
            item['name'],
            item['study_visa'],
            item['visit_visa'],
            item['business_visa'],
            item['employment_visa']
        ))
        self.conn.commit()
