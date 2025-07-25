api = {
  "query": "24.48.0.1",
  "status": "success",
  "country": "Canada",
  "countryCode": "CA",
  "region": "QC",
  "regionName": "Quebec",
  "city": "Montreal",
  "zip": "H1K",
  "lat": 45.6085,
  "lon": -73.5493,
  "timezone": "America/Toronto",
  "isp": "Le Groupe Videotron Ltee",
  "org": "Videotron Ltee",
  "as": "AS5769 Videotron Ltee"
}

# 24.48.0.1 Ip Address located in Canada. Its longitude and latitude are respectively.

ip_address = api.get("query") # ip_address = api["query"]
country = api.get("country")
latitude = api.get("lon")
longitude = api.get("lat")
# print(ip_address,country,latitude,longitude)

sentence = f"{ip_address} Ip Address located in {country}.{longitude} and {latitude} are respectively its longitutude and latitude."

print(sentence)