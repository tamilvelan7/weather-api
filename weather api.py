import requests

api_url=" https://api.openweathermap.org/data/2.5/weather?appid=4690bedc3fb49c50ffca8ebcdf2bee15&q="
city=input("Enter the city name: ")

url=api_url+city

weather=requests.get(url).json()

if weather["cod"]!="404":
    city1=weather['name']
    print("Name of the city: ",city1)
    sampletemp=weather['main']
    temp=sampletemp["temp"]
    k = temp
    normal=(k - 273.15)  
    print("City Temperature is: ",round(normal,1))
    temp1=sampletemp["temp_min"]
    k1=temp1
    min=(k1- 273.15)
    print("City Minimum Temperature is: ",round(min,1))
    temp2=sampletemp["temp_max"]
    k2=temp2
    max=(k2- 273.15)
    print("City Maximum Temperature is: ",round(max,1))
    humidity=sampletemp["humidity"]
    print("City humidity is: ",humidity)
else:
    print("City is not found")

