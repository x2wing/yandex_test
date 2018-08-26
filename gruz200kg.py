items = """0;9;35,12,3;26
1;8;7,29,3;1
2;96;22,36,32;39
3;88;10,9,31;76
4;51;14,33,17;66
5;77;4,18,34;30
6;68;16,34,26;10
7;3;23,27,32;96
8;32;1,33,9;60
9;26;39,15,20;18
10;98;33,36,29;51
11;52;14,21,22;8
12;77;3,31,13;85
13;30;4,9,34;35
14;88;22,6,40;97
15;34;12,10,21;65
16;67;24,33,8;58
17;6;6,1,24;55
18;53;7,38,6;91
19;37;38,26,11;69
20;68;14,5,6;94
21;24;12,13,30;19
22;97;36,8,9;35
23;2;3,8,36;8
24;9;16,38,4;89
25;91;1,14,24;40
26;86;31,19,3;55
27;55;9,7,29;47
28;79;37,33,34;53
29;23;6,7,21;54
30;45;11,32,10;2
31;23;26,37,12;24
32;42;16,37,14;94
33;56;19,13,39;23
34;70;31,11,7;33
35;54;23,10,2;34
36;76;37,12,6;60
37;67;16,25,11;57
38;3;14,27,32;72
39;33;37,4,13;90"""

# items = input()


lst = map(lambda x: x.split(';'), items.split())
storage1 = {'ids': set(), 'weight': 0}
storage2 = {'ids': set(), 'weight': 0}
for i in sorted(lst, reverse=True, key=lambda x: int(x[3])):
    incompatibles = set(i[2].split(','))
    if   not incompatibles.intersection(storage1['ids']) and storage1['weight'] + int(i[1]) < 200:
        storage1['ids'].add(i[0])
        storage1['weight'] += int(i[1])
    elif not incompatibles.intersection(storage2['ids']) and storage2['weight'] + int(i[1]) < 200:
        storage2['ids'].add(i[0])
        storage2['weight'] += int(i[1])
print(';'.join(storage1['ids']))
print(';'.join(storage2['ids']))

