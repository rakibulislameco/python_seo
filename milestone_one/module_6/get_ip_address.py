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

# 24.48.0.1 Ip Address located in Canada. It's longitude and latitude is respectively

ip_address = api.get("query")
country = api.get("country")
lat = api.get("lat")
lon = api.get("lon")

sentence = f'{ip_address} Ip Address located in {country}. Its longitude and latitude are {lon} and {lat} respectively'
print(sentence)