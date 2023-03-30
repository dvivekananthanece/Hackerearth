received_text = input()
palindrome_text = received_text[::-1]
if received_text == palindrome_text:
    print("YES")
else:
    print("NO")
