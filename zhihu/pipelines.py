# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import zhihu.settings as settings

class ZhihuPipeline(object):

    def __init__(self):
        #self.file=open("zhihu.json",'a')
        pass

    def process_item(self, item, spider):
        j=json.dumps(dict(item),ensure_ascii=False)+'\n'

        filename = os.path.join(settings.USERDATA_DIR, item["name"])

        if not os.path.exists(filename):
            with open(filename,"w") as f:
                f.write(j) 

        return item
        
    def close_spider(self,spider):
        #self.file.close()
        pass
