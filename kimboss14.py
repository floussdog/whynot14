import http.client

conn = http.client.HTTPSConnection("sms-international.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

conn.request("GET", "/WebTool/SMStoCountry/sms1?phonenum=14168052749,14507002889&msg=Hello%2C%20welcome%20to%20use%20sms%20service", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
