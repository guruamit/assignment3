# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def upper_lower_alphabet():
    sample_string = str(input("enter the string you want to count the upper and lower case alphabet :"))
    upper_case=0
    lower_case=0
    for i in sample_string:
        if i.isupper():
            upper_case=upper_case+1
        if i.islower():
            lower_case=lower_case+1
        else:
            pass
    print("Number of alphabets in upper case is  :",upper_case)
    print("Number of alphabets in lower case is  :",lower_case)

upper_lower_alphabet()