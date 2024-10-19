from sys import maxsize
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import enum
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



class StatusEnum(enum.Enum):
    online = 1
    offline = 2
    error = 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
    engine.connect()




