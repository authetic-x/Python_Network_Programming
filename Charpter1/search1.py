from pygeocoder import Geocoder



if __name__ == "__main__":

    address = '要翻墙啊！'
    print(Geocoder.geocode(address)[0].coordinates)