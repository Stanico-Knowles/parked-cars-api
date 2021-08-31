# parked-cars-api

# I am developing an API for a biased parking garage owner.
# If he likes a car, they get free parking. He likes all red, green, and black cars but hates everything else.
# However, he may like the car but if it's dirty, then it's half off not free.
# If he hates the car, it's full price.
# If he hates the car and it's dirty, double price.
# Base parking charge is $7.

# The API will:
#   Accept the license plate number, which will serve as primary key, car color, hours parked, and whether or not it is dirty.
#   Return the same info that's accepted plus the price.
#   Delete by PK
#   Update the accpeted info

# db will include:
#   licensePlateNumber str
#   carColor str
#   isDirty bool
#   hoursParked int
#   price float
