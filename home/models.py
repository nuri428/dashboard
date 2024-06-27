from django.db import models

# Create your models here.
from django.db.models import (
    BooleanField, 
    CharField, 
    DateTimeField,
    ForeignKey,    
    TextField
)

class NewsIncome(models.Model):
    """_summary_
    """
    hash_key =  CharField(unique=True, max_length=32, blank=False, null=False, help_text='뉴스 유일값')
    url = CharField(max_length=255, blank=False, null=False, help_text='기사 url')
    is_scrap = BooleanField(blank=False, null=False, default=False, help_text='수집여부')
    list_date = DateTimeField(auto_now=True,help_text='목록 추가날짜')
    scrap_date = DateTimeField(blank=True, null=True, help_text='수집 시각')
    portal = CharField(max_length=255, blank=True, null=False, help_text='1차 기사출처[다음,네이버]')
    
    class Meta:
        managed = False
        db_table = "news_income"
        app_label = 'home'
        ordering = ["hash_key","list_date"]
        indexes = [
            models.Index(fields=["hash_key"]),
            models.Index(fields=["url"]),
            models.Index(fields=["is_scrap"]),
            models.Index(fields=["list_date"]),
            models.Index(fields=["scrap_date"]),
            models.Index(fields=["portal"]),
        ]


class NewsArticle(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    hash_key = ForeignKey(NewsIncome, default=None, to_field='hash_key',db_column='hash_key', on_delete=models.CASCADE, help_text='뉴스 유일값')    
    title  =  CharField(max_length=255, blank=True, null=False, help_text='뉴스 제목')
    content = TextField(blank=True, null=False, help_text='뉴스 본문')
    created_date = DateTimeField(blank=True, null=True, help_text='뉴스 생성시각')
    portal = CharField(max_length=255, blank=True, null=False, help_text='1차 기사출처[다음,네이버]')
    media = CharField(max_length=255, blank=True, null=False, help_text='2차 기사출처[조선, 이데일리...]')
    url = CharField(max_length=255, blank=False, null=False, help_text='기사 url')
    image_url = CharField(max_length=300, blank=False, null=False, help_text='기사 이미지 url')    
    created = DateTimeField(auto_now=True,help_text='데이터 입력시각')
    updated = DateTimeField(auto_now_add=True,help_text='데이터 갱신시각')
    class Meta:
        managed = False
        db_table = "news_article"        
        app_label = 'home'
        ordering = ["hash_key","created"]
        indexes = [
            models.Index(fields=["hash_key"]),
            models.Index(fields=["url"]),
            models.Index(fields=["portal"]),
            models.Index(fields=["media"]),            
            models.Index(fields=["created_date"]),
            models.Index(fields=["created"]),
            models.Index(fields=["updated"]),
        ]