from django.db import models
from datetime import datetime

class tblAdvtBsc(models.Model):
    AdvtNo      = models.IntegerField(default=0, primary_key=True)            # 광고번호
    AdvtTpCd    = models.CharField(max_length=30)                             # 광고종류코드
    AdvtTitl    = models.CharField(max_length=200)                            # 광고제목
    AdvtStaDate = models.CharField(max_length=8)                              # 광고시작일자
    AdvtEndDate = models.CharField(max_length=8)                              # 광고종료일자
    AdvtDesc    = models.CharField(max_length=3000)                           # 광고내용
    AdvtGrdCd   = models.CharField(max_length=30)                             # 광고등급코드
    DelYN       = models.CharField(max_length=1)                              # 삭제여부
    FstAddTmst  = models.DateTimeField(default=datetime.now(), blank=True)    # 최초등록일시
    FstAddID    = models.CharField(max_length=30)                             # 최초등록ID
    LastUptTmst = models.DateTimeField(default=datetime.now(), blank=True)    # 최종변경일시
    LastUptID   = models.CharField(max_length=30)   


 #   def __str__(self):
 #       """A string representation of the model."""
 #       return self.AdvtNo