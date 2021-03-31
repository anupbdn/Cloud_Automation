x = input('shortname: ')

y= "\033[1m" + x.upper() + "\033[0m"
print(y)

print('\nNLB\n')

nlb_prd = x + '-ppgwa-nlb'

print(nlb_prd)
nlb_nprd = x + '-dpgwa-nlb'
print(nlb_nprd)

print('\nTG\n')

tg_nprd = x + '-dpgwa-nlb-tg'
print(tg_nprd)
tg_nprd1 = x + '-dpgwa-nlb-7299'
print(tg_nprd1)

tg_prd = x + '-ppgwa-nlb-tg'
print(tg_prd)
tg_prd1 = x + '-ppgwa-nlb-7299'
print(tg_prd1)

print('\nInstance\n')

print('EIP')