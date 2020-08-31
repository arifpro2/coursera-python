name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()

for i in handle:
    if i.startswith('From '):
        split_i = i.split()[5].split(':')
        if split_i[0] not in d:
            d[split_i[0]] = 1
        else:
            d[split_i[0]] += 1

for k in sorted(d):
    print(k, d[k])