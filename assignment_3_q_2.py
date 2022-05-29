# Write a Python program to reverse a string.
def reverse():
    sample_string="1234abcd"
    reversed =" "
    for i in sample_string:
        reversed=i+reversed
    print("sample string is  :", sample_string)
    print("Reversed string is  :", reversed)

  
reverse()