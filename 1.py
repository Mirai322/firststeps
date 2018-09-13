def dest(age_func):
    if age_func < 7:
        a = "Ты детсадовец"
    elif age_func < 18:
        a = "Ты школьник"
    elif age_func <= 25:
        a = "Ты студент"
    else:
        a = "Ты работяга"
    return(a)
age = int(input("How old are you?"))
run = dest(age)
print(run)