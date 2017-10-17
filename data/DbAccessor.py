# coding: utf-8
"""
gmot schema model
"""
import configparser
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, DATETIME, create_engine
from sqlalchemy.orm import session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# config read
config = configparser.ConfigParser()
config.read('config.ini')
user = config.get('dbsettings', 'user')
passwd = config.get('dbsettings', 'passwd')
host = config.get('dbsettings', 'host')
dbname = config.get('dbsettings', 'dbname')
echo = config.getboolean('dbsettings', 'echo')

# Base init
Base = declarative_base()


class GBPost(Base):
    __tablename__ = 'gb_posts'

    created_at          = Column('created_at', DATETIME, nullable=False, default=datetime.now())
    updated_at          = Column('updated_at', DATETIME, nullable=False, onupdate=datetime.now())
    id                  = Column('id', String(100), primary_key=True)
    post_date           = Column('post_date', String(10))
    meta_ids_name       = Column('meta_ids_name', String(10))
    author              = Column('author', String(20))
    lobi_name           = Column('lobi_name', String(20))
    user_id             = Column('user_id', String(100))
    final_score         = Column('final_score', Integer)
    end_score           = Column('end_score', Integer)
    end_score_raw       = Column('end_score_raw', String(20))
    total_score         = Column('total_score', Integer)
    total_score_raw     = Column('total_score_raw', String(300))
    stage_mode          = Column('stage_mode', String(1))
    post_datetime       = Column('post_datetime', String(30))
    duration            = Column('duration', String(10))
    ring                = Column('ring', String(1))
    media               = Column('media', String(1))
    is_score_editted    = Column('is_score_editted', String(1))
    is_valid_data       = Column('is_valid_data', String(1))
    stage_mode_re       = Column('stage_mode_re', String(1))

    def __init__(self,
                 created_at, updated_at, id, post_date, meta_ids_name, author, lobi_name, user_id,
                 final_score, end_score, end_score_raw, end_score_knn, end_score_knn_raw,
                 total_score, total_score_raw, stage_mode,
                 post_datetime, duration, ring, media, is_score_editted, is_valid_data, stage_mode_re):
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = id
        self.post_date = post_date
        self.meta_ids_name = meta_ids_name
        self.author = author
        self.lobi_name = lobi_name
        self.user_id = user_id
        self.final_score = final_score
        self.end_score = end_score
        self.end_score_raw = end_score_raw
        self.total_score = total_score
        self.total_score_raw = total_score_raw
        self.stage_mode = stage_mode
        self.post_datetime = post_datetime
        self.duration = duration
        self.ring = ring
        self.media = media
        self.is_score_editted = is_score_editted
        self.is_valid_data = is_valid_data
        self.stage_mode_re = stage_mode_re


# create_engine("mysql://[user]:[passwd]@[host]/[dbname]", encoding="utf-8", echo=[True/False])
engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=%s' % (user, passwd, host, dbname, 'utf8'),
                       encoding="utf-8", echo=echo)
# Base.metadata.create_all(engine)
