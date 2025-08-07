def palindrome(str):
    if str == str[::-1]: 
        return 'yes' 
    else: 
        return 'no'

while True:
    str = input()
    if str == '0':
        break
    print(palindrome(str))

