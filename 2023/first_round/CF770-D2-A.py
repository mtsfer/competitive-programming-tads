password_length, number_of_distinct_letters = map(int, input().split())
password_distinct_letters = [chr(97 + i) for i in range(number_of_distinct_letters)]
password_repeated_letters = [password_distinct_letters[i % number_of_distinct_letters]
                             for i in range(password_length - number_of_distinct_letters)]
formatted_password = ''
for letter in password_distinct_letters + password_repeated_letters:
    formatted_password += letter
print(formatted_password)
