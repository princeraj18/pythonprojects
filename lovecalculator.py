Your_name=input("Enter your name \n").lower()
partner_name=input("Enter your patner name:\n").lower()
comb_name=Your_name+partner_name
t=comb_name.count("t")
r=comb_name.count("r")
u=comb_name.count("u")
e=comb_name.count("e")
true=t+r+u+e
l=comb_name.count("l")
o=comb_name.count("o")
v=comb_name.count("v")
e=comb_name.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f"your love score is {love_score} and you go together like Coke and Mentos.")
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score} you both are alright together.")
else:
    print(f"your love score is {love_score}.")
