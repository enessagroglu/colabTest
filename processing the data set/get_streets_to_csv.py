from get_streets_with_selenium import get_streets
import pandas as pd

def get_streets_to_csv():
    url_list = [
                "https://www.posta-kodu.org/istanbul/cekmekoy/omerli/resadiye/caddeler-sokaklar",
                "https://www.posta-kodu.org/istanbul/umraniye/ihlamurkuyu/tepeustu/caddeler-sokaklar",
                "https://www.posta-kodu.org/istanbul/maltepe/aydinevler/basibuyuk/caddeler-sokaklar"
                ]
    
    cadde_tag = "/html/body/main/section[2]/div/div[1]/div[1]/table[1]/tbody"
    sokak_tag = "/html/body/main/section[2]/div/div[1]/div[1]/table[2]"
    
    caddeler, sokaklar = get_streets(url_list[0], cadde_tag, sokak_tag)
    df = pd.DataFrame(caddeler + sokaklar, columns=["street"])
    df.to_csv("./data/resadiye.csv", index=False)
    
    caddeler, sokaklar = get_streets(url_list[1], cadde_tag, sokak_tag)
    df = pd.DataFrame(caddeler + sokaklar, columns=["street"])
    df.to_csv("./data/tepeustu.csv", index=False)
    
    caddeler, sokaklar = get_streets(url_list[2], cadde_tag, sokak_tag)
    df = pd.DataFrame(caddeler + sokaklar, columns=["street"])
    df.to_csv("./data/basibuyuk.csv", index=False)
