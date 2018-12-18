# onad/onad_web

구동파일
- wsgi.py

하위 디렉토리
service/model : DB 커넥션 및 DB 설정 관련
> __init__.py : sqlalchemy 설정

service/controller : 데이터를 처리하거나, 디비와 접촉하는 등의 대부분의 일들이 존재
> asdf.py : 어떠한 일

service/templates : view폴더로, html파일들

service/static : js, css, 설정파일, 업로드파일, 감성분석모델(?)-들어가게 된다면
> /js - js파일
> /css - css파일
> /storage - 업로드파일
> /ml_model

