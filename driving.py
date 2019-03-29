country = input('请问是哪国人: ')
age = input('请输入年龄: ')
if country == '中国':
    if int(age) >= 18:
        print('你可以考驾照')
    else:
        print('你还不能考驾照')
elif country == '美国':
    if int(age) >= 16:
        print('你可以考驾照')
    else:
        print('还不可以考哟~')
else:
    print('你只能输入台湾/美国')