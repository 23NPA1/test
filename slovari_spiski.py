sex = {
    'аня': 10,
    'вика': 15,
    'жак': 4,
    'витька': 12,
    'генка': 1 
}
print(sex)
sex.pop('аня')
print(sex)
x = sex['вика']
y = sex['жак']
a = sex['вика']
print(x, y, a)
sex['генка'] = 15
sex['аня'] = 25
sex['жак'] = 10000000000
print(sex)

jopa = ['пися', 52, 3.13, 'оливье', 'маракасы']
print(jopa)
jopa.remove(52)
print(jopa)
print(jopa[0], jopa[3], jopa[2])
print(jopa.index('пися'))
