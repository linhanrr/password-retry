password = 'a123456'
n = 3
while n > 0:
    attempt = input('請輸入密碼: ')
    if attempt == 'a123456':
        print('登入成功')
        break
    elif attempt != 'a123456':
            print('密碼錯誤! 你還有', n-1, '次機會')
            n = n - 1

