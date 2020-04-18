need_to_add_data = input('need_to_add_data or print_data (Y/N) ?')
if need_to_add_data == 'y' or need_to_add_data == 'Y':
    users = open('user.txt', 'a')
    user = input('input user: ')
    if user == '':
        print('input Erorr')
    else:
        print('user ADD')
        users.write(user + '\n')
        users.close()

    users_pass = open('pass.txt', 'a')
    u_pass = input('input pass: ')
    if u_pass == '':
        print('input Erorr')
    else:
        print('pass ADD')
        users_pass.write(u_pass + '\n')
        users_pass.close()
        print('start me agen and input n to show data')
elif need_to_add_data == 'n' or need_to_add_data =='N':
    u = open('user.txt', 'r')
    ru = u.readlines()
    list_ru = list(ru)
    z_list_ru = list_ru[0]
    u.close()


    p = open('pass.txt', 'r')
    rp = p.readlines()
    list_rp = list(rp)
    z_list_rp = list_rp[0]
    p.close()

    for z_list_ru, z_list_rp in zip(list_ru, list_rp):
        user = str(z_list_ru).replace('\n','')
        _pass = str(z_list_rp).replace('\n','')
        print(user + ':' + _pass)
else:
    print('must input y for add or n to show data')




