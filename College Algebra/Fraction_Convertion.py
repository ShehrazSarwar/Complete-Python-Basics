import random

# converts string input (even fractions) to float, that means 4/5 etc
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n / d
        return ans
    else:
        ans = float(in_string)
        return ans

# One-step multiply
def one_step_mult():
    # Uses string_frac(<input string>)
    a = random.randint(1, 11)
    b = random.randint(2, 24)
    print(a, "x = ", b)
    print("Round your answer to two decimal places.")
    ans_in = (input("x = "))
    answer = round(b / a, 2)
    # test
    if string_frac(ans_in) == answer:
        print("Correct!")
    else:
        print("Try again")
        print("The correct answer is ", answer)

one_step_mult()

