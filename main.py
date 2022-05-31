import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter phone number here +__: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
geo = geocoder.description_for_number(phone, 'en')
car = carrier.name_for_number(phone, 'en')

print(phone)
print(time)
print(geo)
print(car)