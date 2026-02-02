temperature = float(input("Enter the current temperature in Celsius: "))

if temperature >= 25:
    print("It's warm you can wear light soft short sleeve tops")
elif 20 <= temperature < 25:
    print("A single long-sleeve shirt is recommended.")
elif 15 <= temperature < 20:
    print("You can wear light clothes but bring a light outer layer just in case.")
elif 10 <= temperature < 15:
    print("A light training jacket is still recommended.")
else:
    print("Warning: too cold for light clothes, stick to your jacket to stay safe.")
