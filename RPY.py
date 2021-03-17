import requests,xmltodict,json

def GetPosts(limit,tags,pagenumber):
    Limit = int(limit)
    GET = requests.get(f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit={Limit}&tags={tags}&pid={pagenumber}")
    print(GET.status_code)
    JSON = json.dumps(xmltodict.parse(GET.content),sort_keys=True)
    LinkList = []
    if Limit == 1:
        LinkList.append(json.loads(JSON)["posts"]["post"]["@file_url"])
    else:
        for i in range(0,Limit):
            LinkList.append(json.loads(JSON)["posts"]["post"][i]["@file_url"])
    
    return LinkList