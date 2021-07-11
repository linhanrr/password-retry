password = 'a123456'
n = 3 #剩餘機會
while n > 0:
    n = n - 1 #放在這裡，相當於只要問一次密碼，就用掉一次機會
    attempt = input('請輸入密碼: ')
    if attempt == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤!')
        if n > 0:
            print('你還有', n, '次機會') #這樣在最後一次的時候，就不會印出還剩幾次
        else:
            print('沒機會嘗試了! 要鎖帳號ㄌ!')
            

