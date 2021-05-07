import random,copy,difflib
perfect_character={
    12: [['down',100]],
    13: [['right',100]],
    14: [['down',100],['right',0]],

    21: [['down',100]],
    23: [['down',100],['left',0]],
    24: [['left',100]],

    31: [['right',0],['down',100]],
    32: [['up',0],['right',0],['down',100]],
    34: [['up',0],['down',100]],

    41: [['up',0],['left',0],['down',100]],
    42: [['left',0],['down',100]],
    43: [['up',0],['down',100]],

}
basic_character={
    12: [['down',100]],
    13: [['right',100]],
    14: [['down',50],['right',50]],

    21: [['down',100]],
    23: [['down',50],['left',50]],
    24: [['left',100]],

    31: [['right',50],['down',50]],
    32: [['up',50],['right',50],['down',0]],
    34: [['up',50],['down',50]],

    41: [['up',50],['left',50],['down',0]],
    42: [['left',50],['down',50]],
    43: [['up',50],['down',50]],


}
def random_choice_by_percentage(array):
    probability_list=[0 for i in range(len(array))]
    sum=0
    for i in range(len(array)):
        sum+=array[i][1]
        probability_list[i]=sum
    choice=random.randint(0,99)
    for i in range(len(probability_list)):
        if choice<probability_list[i]:
            final_choice=array[i][0]
            return final_choice
class animal():
    def __init__(self,characterDictionary,id,father):
        #self.status='alive'
        self.character=characterDictionary
        self.position_id=''
        self.Id=id
        self.father=father
def howToMove(sheep,wolf):
    environment=int(str(sheep.position_id)+str(wolf.position_id))
    move_direction=random_choice_by_percentage(sheep.character[environment])
    if move_direction=='up':
        sheep.position_id-=2
    elif move_direction=='down':
        sheep.position_id+=2
    elif move_direction =='right':
        sheep.position_id +=1
    elif move_direction =='left':
        sheep.position_id -=1
    return sheep.position_id
def compete(sheep,wolf):
    global total_dead_number
    #sheep.status='dead'
    #wolf.status='dead'
    random_position_id=random.randint(0,1)
    if random_position_id ==0:
        sheep.position_id = 1
        wolf.position_id = 2
    else:
        sheep.position_id=2
        wolf.position_id=1
    step=0

    whoFirstMove = random.randint(0, 1)
    if whoFirstMove==0:
        while True:
            step+=1
            sheep.position_id = howToMove(sheep, wolf)
            if sheep.position_id==5 or sheep.position_id==6:
                return sheep.Id
            wolf.position_id =howToMove(wolf,sheep)
            if wolf.position_id==5 or wolf.position_id==6:
                return wolf.Id
            if step>100:
                print('>>>>>>>>>>>>100')
                return random.choice([wolf.Id,sheep.Id])
    else:
        while True:
            step+=1
            wolf.position_id = howToMove(wolf, sheep)
            if wolf.position_id == 5 or wolf.position_id==6:
                return wolf.Id
            sheep.position_id = howToMove(sheep, wolf)
            if sheep.position_id==5 or sheep.position_id==6:
                return sheep.Id
            if step>100:
                print('>>>>>>>>>>>>100')
                return random.choice([wolf.Id,sheep.Id])

def reproduction_model_fast():
    global a,total_alive_number,total_dead_number,total_number,biggest_id,all_winner_list,previous_generation,id_and_a_interval
    winer_list=match_competitors(total_alive_number,total_dead_number)
    all_winner_list +=winer_list
    total_dead_number=total_alive_number +total_dead_number
    total_alive_number *=2
    total_number=total_alive_number+total_dead_number
    b=0
    umbilical_cord=0
    for j in range(total_alive_number):
        if b==4:
            umbilical_cord+=1
            b=0
        biggest_id+=1
        a[j]=animal(copy.deepcopy(previous_generation[winer_list[umbilical_cord]-id_and_a_interval].character),biggest_id,str(winer_list[umbilical_cord])+'   ')
        if b==0:
            a[j].character = gene_mutation(a[j].character)
            a[j].father=str(int(a[j].father))+'XXX'
        b += 1
    previous_generation=a.copy()
    id_and_a_interval=total_dead_number
        #return previous_generation


def reproduction_model_stable():
    global a, total_alive_number, total_dead_number, total_number, biggest_id, all_winner_list, previous_generation,id_and_a_interval
    winer_list = match_competitors(total_alive_number, total_dead_number)
    total_dead_number = total_alive_number + total_dead_number
    total_alive_number *= 1
    total_number=total_alive_number +total_dead_number
    umbilical_cord =0
    umbilical_cord_rule_number=0
    for i in range(total_alive_number):
        if umbilical_cord_rule_number ==2:
            umbilical_cord_rule_number =0
            umbilical_cord +=1
        biggest_id += 1
        a[i] = animal(copy.deepcopy(previous_generation[winer_list[umbilical_cord]-id_and_a_interval].character), biggest_id,str(winer_list[umbilical_cord])+'   ')
        if umbilical_cord_rule_number ==0:
            if_gene_mutation=random.randint(0,3)
            if if_gene_mutation ==1:
                a[i].father=str(int(a[i].father))+'XXX'
                a[i].character=gene_mutation(a[i].character)
        umbilical_cord_rule_number += 1
    all_winner_list += winer_list
    id_and_a_interval =total_dead_number
    previous_generation =a.copy()

def match_competitors(total_alive_number,total_dead_number):
    winer_list=[]
    random_match=random.sample(range(total_alive_number),total_alive_number)
    for k in range(int((total_alive_number) / 2)):
        winer_list.append(compete(previous_generation[random_match[k*2]], previous_generation[random_match[k*2+1]]))

    return winer_list
def gene_mutation(father_character):
    new_character =father_character
    random_gene_mutation_position=random.choice([14,23,31,32,34,41,42,43])
    random_gene_mutation_position_deep=random.sample(range(0,len(father_character[random_gene_mutation_position])),2)
    change1=new_character[random_gene_mutation_position][random_gene_mutation_position_deep[0]][1]
    change2=new_character[random_gene_mutation_position][random_gene_mutation_position_deep[1]][1]
    change_number=random.randint(1,20)
    if change1+change_number<=100 and change2-change_number >=0:
        new_character[random_gene_mutation_position][random_gene_mutation_position_deep[0]][1]+=change_number
        new_character[random_gene_mutation_position][random_gene_mutation_position_deep[1]][1] -= change_number
    return new_character
def import_log_alive():
    for i in range(total_alive_number):
        file = open('log.txt', 'a')
        file.write(str(previous_generation[i].Id) + '     father: ' + previous_generation[i].father +'   '+str(previous_generation [i].character) +'\n')
        file.close()
    file=open('log.txt', 'a')
    file.write('\n')
    file.close()
def import_log_all_stable():
    enter=0
    for i in range(biggest_id+1):
        file = open('log.txt', 'a')
        if i in all_winner_list:
            file.write('V    ')
        else:
            file.write('     ')

        file.write(str(i) + '     father: ' + a[i].father +'   '+str(a[i].character) +'\n')
        enter += 1
        if enter==total_alive_number:
            enter=0
            file.write('\n')
        file.close()

def import_log_all_fast():
    file=open('log.txt','w')
    file.write('')
    file.close()
    dead_number = 0
    alive_number = 2
    u = [2]
    for i in range(10000):
        dead_number = alive_number + dead_number
        alive_number *= 2
        t = dead_number + alive_number
        u.append(t)
    for i in range(biggest_id+1):
        file = open('log.txt', 'a')
        if i in u:
            file.write('\n')
        if i in all_winner_list:
            file.write('V    ')
        else:
            file.write('     ')
        file.write(str(i) + '     father: ' + a[i].father +'   '+str(a[i].character) +'\n')
        file.close()
    file=open('log.txt','a')
    file.write('\n')
    file.close()
def import_log_last():
    file=open('log.txt','a')
    file.write(str(biggest_id-1) + '     father: ' + a[biggest_id-1].father +'   '+str(a[biggest_id -1].character) +'\n')
    file.write(str(biggest_id) + '     father: ' + a[biggest_id].father + '   ' + str(a[biggest_id ].character) + '\n')
    file.write('\n')
    file.close()

def data_analyse():
    import difflib
    basic_character = str(
        ['{12:', "[['down',", '100]],', '13:', "[['right',", '100]],', '14:', "[['down',", '50],', "['right',", '50]],',
         '21:', "[['down',", '100]],', '23:', "[['down',", '50],', "['left',", '50]],', '24:', "[['left',", '100]],',
         '31:', "[['right',", '50],', "['down',", '50]],', '32:', "[['up',", '50],', "['right',", '50],', "['down',",
         '0]],', '34:', "[['up',", '50],', "['down',", '50]],', '41:', "[['up',", '50],', "['left',", '50],',
         "['down',", '0]],', '42:', "[['left',", '50],', "['down',", '50]],', '43:', "[['up',", '50],', "['down',",
         '50]]}'])

    #basic_character={12: [['down', 100]], 13: [['right', 100]], 14: [['down', 0], ['right', 100]], 21: [['down', 100]], 23: [['down', 0], ['left', 100]], 24: [['left', 100]], 31: [['right', 100], ['down', 0]], 32: [['up', 100], ['right', 0], ['down', 0]], 34: [['up', 100], ['down', 0]], 41: [['up', 0], ['left', 100], ['down', 0]], 42: [['left', 100], ['down', 0]], 43: [['up', 100], ['down', 0]]}
    a = 0
    i = 0
    b = []
    character_list = []
    ch_number = []
    file = open('log.txt', 'r')
    for line in file:
        i = i + 1
        b.append(line.split())
        if line.split() == []:
            a = i
    file.close()
    for j in range(a, i):
        del (b[j][0], b[j][0], b[j][0])

        if b[j] not in character_list:
            character_list.append(b[j])
    for k in range(len(character_list)):
        n = 0
        for j in range(0, i):
            if b[j] == character_list[k]:
                n += 1
        ch_number.append(n)
    print(ch_number)
    print("max value", max(ch_number))
    print("max value index", ch_number.index(max(ch_number)))
    p = ch_number.index(max(ch_number))
    p = p
    print(str(character_list[p]))
    o = str(character_list[p])
    d = difflib.Differ()
    diff = d.compare(o.splitlines(), basic_character.splitlines())
    print('\n\n')
    print ('\n'.join(list(diff)))


a= [0 for i in range(3**10)]
a[0] = animal(copy.deepcopy(basic_character),0,'none')
a[1] = animal(copy.deepcopy(basic_character),1,'none')
#print(a)
previous_generation=a.copy()
#print(previous_generation)
total_number=2
total_alive_number=2
total_dead_number=0
biggest_id=1
all_winner_list=[]
id_and_a_interval=0

file=open('log.txt','w')
file.close()
for i in range(10):
    reproduction_model_fast()
    #import_log_alive()
for i in range(10000):
    reproduction_model_stable()
    #if i==0:
        #previous_generation[0].character=perfect_character
    if i%10==0:
        print(i)
import_log_alive()
print(all_winner_list)
    #print(i)
#import_log_all_fast()
'''for i in range(0):
    print(have_del_number)
    if i%100==0:
        print(i)
    reproduction_model_stable()
import_log_alive()
print(all_winner_list )
data_analyse()'''







