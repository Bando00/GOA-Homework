def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


def kata_13_december(lst):
    return [x for x in lst if x % 2 != 0]



def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    return drinks.get(param.lower(), "Beer")



def square_sum(numbers):
    return sum(x**2 for x in numbers)

