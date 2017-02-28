import random

def load_from_txt():
    with open('pass.txt',"rb") as f:
        lines = f.read().split('\n')
    passes = lines[:len(lines)-1]
    ids = list(range(len(passes)))
    pass_list = dict(zip(ids,passes))
    return pass_list

def random_gen(org_pass_list):
    new_list = []
    for i in range(0, random.randint(0, len(org_pass_list)-1)):
        index = random.randint(0 , len(org_pass_list)-1)
        new_list.append(index)
    return new_list

def make_file_gen(passes):
    with open ('makefile_tmp.txt', 'rb') as f:
        tmp = f.read()
    with open ('makefile_tmp_two.txt', 'rb') as f:
        tmp_two = f.read()
    opt = 'opt:\n$(opt) $(irfile) -debug-pass=Structure -o $(irfile)'
    for item in passes:
        opt = opt + ' '+item
    with open('Makefile', 'wb') as f:
        f.write(tmp+opt+'\n\n'+tmp_two)

def main():
    pass_list = load_from_txt()
    random_list_index = random_gen(pass_list)
    random_list = [pass_list[k] for k in random_list_index]
    print(random_list)
    make_file_gen(random_list)


if __name__=="__main__":
    main()
