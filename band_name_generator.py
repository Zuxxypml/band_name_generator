print("Welcome to band name generator.")
print("Generate awesome band names for your band ")
user_city = input("Which city did you grow up ?")
user_pet_name = input("What's the name of your pet ?")
first_brand_name = user_city +" "+ user_pet_name
second_brand_name = user_pet_name +" "+user_city
generated_brand_names = first_brand_name +", "+ second_brand_name
print("Generated brand names: "+ generated_brand_names)