###### PRANAY #######

# python script that runs trees with different commandline arguments 
# for dir 25,35,45
# for n 5000,6000,7000,8000
# for tree 0 1 (each tree runs five times for same argument)
# It will make file according to which algorithm test is ruunig 
# it will filter and write real user and sys time   
# calculate average of user+sys and real of 5 runs and also write it in same file
# for script to run properly comment code in main.cpp which prints array after generating array and after sort
# if any of the test case fails the script will end execution and print for which tree test case failed 
# else will print "Success runnig all tests" on console


import subprocess
from builtins import open

success=1
def test(tree,n,dir):
    global success
    path="../trees {n} {dir} {tree}".format(n=n,dir=dir,tree=tree)
    if(tree !=0):
        f = open("rb_tree.txt", "a")
        f.write("\nRunnig rb_tree code\n")
        f.write(path+"\n")
        f.write("real user sys\n")
        f.close()
        sumReal=0
        sumSys=0
        sumUser=0
        for x in range(10):
            output = str(subprocess.check_output(path,shell=True)).strip()
            print(output)
            if(output.find("Timer (sort):")>0):
                real=int(output[output.find("):")+2 : output.find("ms real")])
                user=int(output[output.find("real")+6 : output.find("ms user")])
                sys=int(output[output.find("user")+6 : output.find("ms sys")])
                sumReal+=real
                sumSys+=sys
                sumUser+=user
                f = open("rb_tree.txt", "a")
                f.write('{real}  {user}  {sys}\n'.format(real=str(real),user=str(user),sys=str(sys)))
                f.close()
            else:
                success="ERROR in rb_tree"
                f = open("rb_tree.txt", "a")
                f.write("ERROR")
                f.close()
                return success+"  "+path
        avgReal=sumReal/10
        avgUserSys=(sumSys+sumUser)/10
        f = open("rb_tree.txt", "a")
        f.write('Total avg: avgReal:{avgReal}\t avg(user+sys):{avgUserSys}\n'.format(avgReal=avgReal,avgUserSys=avgUserSys))
        f.close()
    else:
        f = open("bs_tree.txt", "a")
        f.write("\nRunnig bs_tree code\n")
        f.write(path+"\n")
        f.write("real user sys\n")
        f.close()
        sumReal=0
        sumSys=0
        sumUser=0
        if (n<=100000) and (dir == 1 or dir == -1):
            for x in range(1):
                output = str(subprocess.check_output(path,shell=True)).strip()
                print(output)

                if(output.find("The output is sorted!")>0):
                    real=int(output[output.find("):")+2 : output.find("ms real")])
                    user=int(output[output.find("real")+6 : output.find("ms user")])
                    sys=int(output[output.find("user")+6 : output.find("ms sys")])
                    sumReal+=real
                    sumSys+=sys
                    sumUser+=user
                    f = open("bs_tree.txt", "a")
                    f.write('{real}  {user}  {sys}\n'.format(real=str(real),user=str(user),sys=str(sys)))
                    f.close()
                else:
                    success="ERROR in bs_tree"
                    f = open("bs_tree.txt", "a")
                    f.write("ERROR")
                    f.close()
                    return success+"  "+path
                # print(output)
                # print(real,user,sys)
            avgReal=sumReal/1
            avgUserSys=(sumSys+sumUser)/1
            f = open("bs_tree.txt", "a")
            f.write('Total avg: avgReal:{avgReal}\t avg(user+sys):{avgUserSys}\n'.format(avgReal=avgReal,avgUserSys=avgUserSys))
            f.close()
        elif dir==0 :
            for x in range(10):
                output = str(subprocess.check_output(path,shell=True)).strip()
                print(output)
                if(output.find("The output is sorted!")>0):
                    real=int(output[output.find("):")+2 : output.find("ms real")])
                    user=int(output[output.find("real")+6 : output.find("ms user")])
                    sys=int(output[output.find("user")+6 : output.find("ms sys")])
                    sumReal+=real
                    sumSys+=sys
                    sumUser+=user
                    f = open("bs_tree.txt", "a")
                    f.write('{real}  {user}  {sys}\n'.format(real=str(real),user=str(user),sys=str(sys)))
                    f.close()
                else:
                    success="ERROR in bs_tree"
                    f = open("bs_tree.txt", "a")
                    f.write("ERROR")
                    f.close()
                    return success+"  "+path
                # print(output)
                # print(real,user,sys)
            avgReal=sumReal/10
            avgUserSys=(sumSys+sumUser)/10
            f = open("bs_tree.txt", "a")
            f.write('Total avg: avgReal:{avgReal}\t avg(user+sys):{avgUserSys}\n'.format(avgReal=avgReal,avgUserSys=avgUserSys))
            f.close()




def run():
    n=[50000, 100000, 250000, 500000, 1000000, 2500000, 5000000]
    dir=[-1,0,1]
    tree=[0]
    for t in tree:
        for d in dir:
            for nval in n:
                test(t,nval,d)
    global success
    if(success==1):
        print("Success runnig all tests")
    else:
        print(success)

run()