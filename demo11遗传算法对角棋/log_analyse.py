import difflib
basic_character=str(['{12:', "[['down',", '100]],', '13:', "[['right',", '100]],', '14:', "[['down',", '50],', "['right',", '50]],', '21:', "[['down',", '100]],', '23:', "[['down',", '50],', "['left',", '50]],', '24:', "[['left',", '100]],', '31:', "[['right',", '50],', "['down',", '50]],', '32:', "[['up',", '50],', "['right',", '50],', "['down',", '0]],', '34:', "[['up',", '50],', "['down',", '50]],', '41:', "[['up',", '50],', "['left',", '50],', "['down',", '0]],', '42:', "[['left',", '50],', "['down',", '50]],', '43:', "[['up',", '50],', "['down',", '50]]}'])
a=0
i=0
b=[]
character_list=[]
ch_number=[]
file=open('log.txt','r')
for line in file:
    i=i+1
    b.append(line.split())
    if line.split()==[]:
        a=i
file.close()
for j in range(a,i):
    del(b[j][0],b[j][0],b[j][0])

    if b[j] not in character_list:
        character_list.append(b[j])
for k in range(len(character_list)):
    n=0
    for j in range (0,i):
        if b[j]==character_list[k]:
            n+=1
    ch_number.append(n)
print(ch_number)
print("max value",max(ch_number))
print("max value index",ch_number.index(max(ch_number )))
p=ch_number.index(max(ch_number ))
p=p
print(str(character_list[p]))
o=str(character_list[p])
d=difflib.Differ()
diff=d.compare(o.splitlines(),basic_character.splitlines())
print('\n\n')
print ('\n'.join(list(diff)))


