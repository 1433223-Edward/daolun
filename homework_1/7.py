def has_repeated_substring(s):
    length = len(s)
    i = 0

    while i < length - 1:
        if s[i] == s[i + 1]: 
            count = 2  
            while i + count < length and s[i] == s[i + count]:
                count += 1
            if count >= 2:
                return True
            else:
                i += 1
        else:
            i += 1

    return False

input_string = input("Enter a string: ")

if has_repeated_substring(input_string):
    print("Yes")
else:
    print("No")
