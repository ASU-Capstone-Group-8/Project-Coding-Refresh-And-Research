import enum
import os
from datetime import datetime
from sys import maxsize

from sqlalchemy import *


class StatusEnum(enum.Enum):
    online = 1
    offline = 2
    error = 3


def insert_website_data(site_url, site_name, site_status):
    return Website_Data.insert().values(url=site_url, name=site_name, status=site_status)


def insert_web_pages(page_website_id, page_title, page_content, page_url, page_last_scraped):
    return Web_Pages.insert().values(website_id=page_website_id, title=page_title, content=page_content, url=page_url,
                                     last_scraped=page_last_scraped)


def insert_scraped_data(scraped_page_id, scraped_data):
    return Scraped_Data.insert().values(page_id=scraped_page_id, data=scraped_data)


if __name__ == '__main__':
    databaseCreated = os.path.isfile('NLPDatabase.db')
    if databaseCreated:
        print('Database found.')
    else:
        print('Database not found, creating and initializing database now.')

    engine = create_engine('sqlite:///NLPDatabase.db', echo=True)
    meta = MetaData()
    Website_Data = Table(
        'Website_Data', meta,
        Column('website_id', Integer, primary_key=True),
        Column('url', VARCHAR(100)),
        Column('name', VARCHAR(100)),
        Column('status', Enum(StatusEnum)),
    )

    Web_Pages = Table(
        'Web_Pages', meta,
        Column('page_id', Integer, primary_key=True),
        Column('website_id', Integer, ForeignKey('Website_Data.website_id')),
        Column('title', VARCHAR(100)),
        Column('content', VARCHAR(maxsize)),
        Column('url', VARCHAR(100)),
        Column('last_scraped', DATETIME),
    )

    Scraped_Data = Table(
        'Scraped_Data', meta,
        Column('data_id', Integer, primary_key=True),
        Column('page_id', Integer, ForeignKey('Web_Pages.page_id')),
        Column('data', VARCHAR(maxsize)),
    )

    meta.create_all(engine)
    conn = engine.connect()
    conn.execute(insert_website_data('example url', 'Example website', StatusEnum.online))
    conn.execute(insert_web_pages(1, 'example title', 'example content', 'example url', datetime.now()))
    conn.execute(insert_scraped_data(1, 'example data'))
    conn.commit()
