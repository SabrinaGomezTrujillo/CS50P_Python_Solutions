def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not s[0].isalpha() and not s[1].isalpha():
        return False
    exclusiones = ".,;:!?\"'()-[]{}¡¿ "
    if s in exclusiones:
        return False
    for i in range(len(s)):
        if s[i].isdigit():
        if s[i]=="0" and s[i-1].isalpha:
            return False
    else:
         return True
main()
