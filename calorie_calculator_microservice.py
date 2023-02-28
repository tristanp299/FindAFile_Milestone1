# Name: Maggie Wu
# Github UN: wumag
# Date: 02/14/2023
# Description: Calorie calculator program that writes data to a file

import datetime


def main():
    # Create file name using current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f"calorie-calculator-{current_date}.txt"

    with open(file_name, 'w') as f:
        while True:
            welcome()
            info()
            gender = get_sex(f)
            weight = get_weight(f)
            height = get_height(f)
            age = get_age(f)
            rest_bmr = calculate_bmr(gender, weight, height, age)
            total_calculation(rest_bmr, f)
            play = input("\nPress enter to recalculate or type 'exit' to stop the program: ")
            play = play.lower()
            if play == "exit":
                print("\nProgram terminating...")
                break


def welcome():
    print("\nWelcome to your Calorie Calculator!\nFind out how many calories should you eat daily to maintain your current weight.")


def info():
    learn_more = str(
        input("\nDo you wish to learn more about BMR and calories before calculating? "))
    learn_more = learn_more.lower()
    if learn_more == "yes" or learn_more == "y":
        print("\nUnderstanding your BMR, your typical activity level, and the amount of calories you need daily to maintain your weight are important ways for you to actively participate in your physical health.\n\nBasal metabolic rate is the number of calories your body needs to accomplish its most basic (basal) life-sustaining functions.\n\nOne popular way to estimate BMR is through the Mifflin-St Jeor formula, which takes into account weight, height, age, and gender, which is the equation we will be using today.")
    else:
        return learn_more


def get_sex(f):
    user_sex = str(input("\nDo you identify as male or female? "))
    user_sex = user_sex.lower()
    if user_sex not in ("male", "female", "m", "f"):
        user_sex = str(
            input("Invalid input. Please enter either 'male' or 'female' "))
    f.write(f"User gender: {user_sex}")
    return user_sex


def get_weight(f):
    kgs_or_lbs = get_weight_unit_input()

    if kgs_or_lbs == "lbs":
        weight_lbs = get_weight_input(kgs_or_lbs)
        weight_kgs = convert_lbs_to_kgs(weight_lbs)
        f.write(f"\nUser weight(lbs): {weight_lbs}")
        return weight_kgs
    else:
        weight_kgs = get_weight_input(kgs_or_lbs)
        f.write(f"\nUser weight(kgs): {weight_kgs}")
        return weight_kgs


def get_weight_unit_input():
    kgs_or_lbs = str(
        input("Would you like to calculate your weight in kgs or lbs?: ")).lower()
    while kgs_or_lbs not in ("lbs", "kgs"):
        kgs_or_lbs = str(input(
            "Invalid input. Would you like to calculate your weight in kgs or lbs?: ")).lower()
    return kgs_or_lbs


def get_weight_input(kgs_or_lbs):
    weight = float(input(f"Enter your weight in {kgs_or_lbs}: "))
    while weight <= 0:
        weight = float(
            input(f"Invalid input. Please enter your weight in {kgs_or_lbs}: "))
    return weight


def convert_lbs_to_kgs(weight_lbs):
    return weight_lbs * 0.453592


def get_height(f):
    cm_or_ft = get_height_unit_input()

    if cm_or_ft == "ft":
        height_ft_in = get_height_ft_in_input()
        height_cm = convert_ft_to_cm(height_ft_in)
        f.write(f"\nUser height(ft/in): {height_ft_in}")
        return height_cm

    else:
        height_cm = get_height_cm_input()
        f.write(f"\nUser height(cm): {height_cm}")
        return height_cm


def get_height_unit_input():
    cm_or_ft = str(
        input("Would you like to calculate your height in cm or ft?: ")).lower()
    while cm_or_ft not in ("cm", "ft"):
        cm_or_ft = str(
            input("Invalid input. Would you like to calculate your height in cm or ft?: "))
    return cm_or_ft


def get_height_ft_in_input():
    height_ft = float(input("Enter your height, feet first: "))

    while height_ft <= 0:
        height_ft = float(
            input("Invalid input. Please enter your height in feet: "))
    height_in = float(input("Enter your height, inches second: "))

    while height_in <= 0:
        height_in = float(
            input("Invalid input. Please enter your height in inches: "))
    return height_ft, height_in


def get_height_cm_input():
    height_cm = float(input("Enter your height in cm: "))

    while height_cm <= 0:
        height_cm = float(
            input("Invalid input. Please enter your height in cm: "))
    return height_cm


def convert_ft_to_cm(height_ft_in):
    height_ft, height_in = height_ft_in
    height_in += height_ft * 12
    height_cm = height_in * 2.54
    return height_cm


def get_age(f):
    age_yrs = int(input("Enter your age in years: "))
    while age_yrs <= 0:
        age_yrs = int(input("Invalid Input. Please enter your age in years: "))
    else:
        f.write(f"\nUser age: {age_yrs}")
        return age_yrs


def get_user_activity(f):
    activity_lvl = ["sedentary", "light", "moderate", "active"]
    while True:
        user_lvl = str(input("\nWhat is your activity level?\n\nSedentary is little to no exercise.\nLightly active is light exercise/sports 1 - 3 days/week.\nModerately active is moderate exercise/sports 3 - 5 days/week.\nVery active is intense exercise 6 - 7 days/week.\n\nPlease enter 'sedentary', 'light', 'moderate',  or 'active': ")).lower()

        while user_lvl not in activity_lvl:
            user_lvl = str(input("Invalid input. Please enter 'sedentary', 'light', 'moderate',  or 'active': "))
        else:
            f.write(f"\nUser activity level: {user_lvl}")
            return user_lvl


def total_calculation(rest_bmr, f):
    user_activity_lvl = get_user_activity(f)

    maintain = {
        "sedentary": get_sedentary(rest_bmr),
        "light": get_light_activity(rest_bmr),
        "moderate": get_moderate_activity(rest_bmr),
        "active": get_very_active(rest_bmr)
    }

    calories_needed = maintain.get(user_activity_lvl)
    if calories_needed:
        f.write("\nCalories: " + str(calories_needed))
        print("\nYou need to eat " + str(calories_needed) + " calories a day to maintain your current weight.")


def calculate_bmr(gender, weight, height, age):
    female = ["female", "f"]
    if gender == female:
        women = (weight * 10) + (height * 6.25) - (age * 5) - 161
        return int(women)
    else:
        men = (weight * 10) + (height * 6.25) - (age * 5) + 5
        return int(men)


def get_sedentary(rest_bmr):
    sedentary = rest_bmr * 1.25
    return sedentary


def get_light_activity(rest_bmr):
    light = rest_bmr * 1.375
    return light


def get_moderate_activity(rest_bmr):
    moderate = rest_bmr * 1.550
    return moderate


def get_very_active(rest_bmr):
    active = rest_bmr * 1.725
    return active


if __name__ == '__main__':
    main()