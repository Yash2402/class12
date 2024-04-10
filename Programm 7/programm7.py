ch = " "
vcount = 0
uppercount = 0
lowercount = 0
ccount = 0

with open("abc.txt", "r") as file:
    while ch:
        # print(file.tell())
        ch = file.read(1)
        if ch.lower() in ["a","e","i","o","u"]:
            vcount += 1
            if ch.islower():
                lowercount += 1
            else:
                uppercount += 1
        elif ch.isnumeric():
            pass
        else:
            if ch not in "-_+.{|}[?]\}\"\'/,><!@#$%^&*();: \n":
                ccount += 1
                if ch.islower():
                    lowercount += 1
                else:
                    uppercount += 1
        # print("  c     v     u    l")
print(f"{ccount-1, vcount, uppercount-1, lowercount}")