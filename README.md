# extract

##### extract.py
```python
>> get_key() -> str
# os환경에 저장된 api key 가져오기

>> gen_url(dt="20180101", req_val={}) -> str
# request url을 생성

>> req(dt="20180101", url_param={}) -> (int, dict)
# 생성된 url을 이용하여 실제 api 호출

>> req2list(dt="20180101", url_param) -> list
# req() 함수의 결과로 얻어진 dict에서 필요한 데이터를 추출하여 list로 반환

>> list2df(dt="20180101", url_param={}) -> pandas.DataFrame
# req2list의 결과를 pandas DataFrame으로 변환하여 반환

>> save2df(dt="20180101", url_param={}) -> pandas.DataFrame
# list2df의 결과에 load_dt와 repNationCd 컬럼을 추가하여 반환
# 실제 dags에서 호출되는 함수
```
##### ice_breaking.py
```python
>> pic() -> None
# ice_breaking용 ascii-art 출력
```

### dependency
- `requests` : url을 이용한 api 호출
- `pandas`   : DataFrame 조작
- `pyarrow`  : parquet으로 저장 및 불러오기

