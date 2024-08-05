import requests as reqs
import os
import pandas as pd

def gen_url(dt="20180101", req_val={}):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key=get_key()
    url=f"{base_url}?key={key}&targetDt={dt}"

    for key, value in req_val.items():
        url += f"&{key}={value}"
    
    return url


def req(dt="20180101", url_param={}):
    url=gen_url(dt,req_val=url_param)
    resp=reqs.get(url)

    code=resp.status_code
    data=resp.json()


    return code, data


def get_key():
    key=os.getenv("MOVIE_API_KEY")
    return key


def req2list(dt="20180101", url_param={}) -> list:
    _,data=req(dt,url_param=url_param)
    _list = data["boxOfficeResult"]["dailyBoxOfficeList"]

    return _list

def list2df(dt="20180101", url_param={}):
    l=req2list(dt,url_param=url_param)
    df=pd.DataFrame(l)

    return df


def save2df(dt="20180101", url_param={}):
    df = list2df(dt,url_param=url_param)
    df['load_dt']=dt

    return df
