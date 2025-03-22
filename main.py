from model.restaurant import Restaurant
from controller.restaurant import get_all_restaurants
for restaurant in get_all_restaurants():
    print(restaurant.__str__())
