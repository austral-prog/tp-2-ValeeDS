def earth():
    x = "Bangladesh"
    y = "Barbados"

    chequeo = x < y

    print(f"The result of {x} comes first in the dictionary than {y} is {chequeo}.")
    print(f"The result of {y} comes first in the dictionary than {x} is {not(chequeo)}.")

earth()