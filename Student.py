import os
import tarfile
 
filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统么?y/n\n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            else:
                show()
 
def menu():
    print('****学生信息管理系统****')
    print('     1.录入学生信息    ')
    print('     2.查找学生信息    ')
    print('     3.删除学生信息    ')
    print('     4.修改学生信息    ')
    print('     5.排序           ')
    print('     6.统计学生总人数   ')
    print('     7.显示所有学生信息 ')
    print('     0.退出系统        ')
 
def insert():
    student_list=[]
    while True:
        id=int(input('请录入学生id：'))
        if not id:
            break
        name=input('请输入学生姓名：')
        if not name:
            break
 
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            java=int(input('请输入软件需求分析成绩：'))
 
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #将录入的学生信息保存到字典当中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        #将学生信息添加到列表当中
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #调用save（）函数
    save(student_list)
    print('学生信息录入完成！！！！！！！！1')
 
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
 
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按id查找请输入1,按姓名查找请输入2\n')
            if mode=='1':
                id=input('请输入要查找的id：')
            elif mode=='2':
                name=input('请输入要查找的姓名：')
            else:
                print('您的输入有误,请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否要继续查询？y/n\n')
            if answer=='y'  or answer=='Y':
                continue
            else:
                break
        else:
            print('暂未保存该学生信息')
            return
 
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息,无数据显示！！！')
        return
    #定义标题显示格式
    format_title='{:^8}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(format_title.format('id','姓名','英语成绩','python成绩','java成绩','总成绩'))
    #定义内容显示格式
    format_date='{:^8}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_date.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                ))
 
def delete():
    while True:
        student_id=int(input('请输入要删除的学生id：'))
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False         #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))        #将字符串转换成字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}')
            else:
                print('无学生信息')
                break
            show()          # 删除之后显示所有学生信息
            answer=input('是否继续删除？y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
    print('删除学生信息完毕！！！')
 
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            stuedent_old=rfile.readlines()
    else:
        return
    student_id=input('请输入修改学生的id：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in stuedent_old:
            d=dict(eval(item))
            if str(d['id'])==student_id:
                print('恭喜找到这名学生的信息，可以修改他的相关信息了！！！')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['english']=input('请输入英语成绩：')
                        d['python']=input('请输入python成绩：')
                        d['java']=input('请输入Java成绩')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他学生的信息？y/n\n')
        if answer=='y' or answer=='Y':
            modify()
        else:
            print('修改完毕')
 
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
        student_new=[]
        for item in students:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择排序方式（0,升序  1,降序）\n')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式（1，按英语成绩排序   2，按python成绩排序     3，按Java成绩排序    0，按总成绩排序）\n')
    if mode=='1':
        student_new.sort(key=lambda student_new:int(student_new['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda student_new: int(student_new['python']), reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda student_new: int(student_new['java']), reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda student_new: int(student_new['english'])+int(student_new['python']+int(student_new['java'])), reverse=asc_or_desc_bool)
    else:
        print('您输入的信息有误，请重新输入')
        sort()
    show_student(student_new)
 
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                if students:
                    print('一共有{}个学生'.format(len(students)))
                else:
                    print('还没有录入学生信息')
    else:
        print('暂未保存学生信息')
 
def show():
    student_information=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_information.append(eval(item))
            if student_information!=[]:
                show_student(student_information)
    else:
        print('暂未保存学生信息')
 
if __name__ == '__main__':
    main()