FILE="contact.txt"
def load_contact():
    contact_dict={}
    try:
        with open(FILE,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                name,phone=line.split("|")
                contact_dict[name]=phone
    except FileNotFoundError:
        pass
    return contact_dict

def save_contact(data):
    with open(FILE,"w",encoding="utf-8") as f:
        for name,phone in data.items():
            f.write(f"{name}|{phone}\n")

def main():
    contact=load_contact()
    while True:
        print("\n=====简易通讯录=====")
        print("1.添加联系人")
        print("2.查看所有联系人")
        print("3.搜索联系人")
        print("4.修改联系人")
        print("5.删除联系人")
        print("0.退出程序")
        try:
            choice=int(input("请输入功能序号："))
            if choice==1:
                name=input("输入联系人姓名：")
                if name=="":
                    print("姓名不能为空")
                    continue
                if name in contact:
                    print("该联系人已存在!")
                phone=input("输入手机号码：").strip()
                if len(phone)!=11 or not phone.isdigit():
                    print("手机号必须是11位数字!")
                    continue
                contact[name]=phone
                save_contact(contact)
                print("联系人添加成功")

            elif choice==2:
                if not contact:
                    print("通讯录暂无该联系人")
                    continue
                print(f"\n{'姓名':<6}{'手机号码'}")
                print("-"*16)
                for n,p in contact.items():
                    print(f"{n:<6}{p}")

            elif choice==3:
                key=input("输入要查找的联系人姓名关键词：").strip()
                find_list=[]
                for n,p in contact.items():
                    if key in n:
                        find_list.append((n,p))
                if not find_list:
                    print("未找到匹配联系人")
                else:
                    print(f"\n{'姓名':<6}{'手机号码'}")
                    print("-"*16)
                    for n,p in find_list:
                        print(f"{n:<6}{p}")

            elif choice==4:
                edit_name=input("输入要修改的联系人姓名：").strip()
                if edit_name not in contact:
                    print("不存在该联系人！")
                    continue
                new_phone=input("输入新手机号：").strip()
                if len(new_phone)!=11 or not new_phone.isdigit():
                    print("手机号格式错误！")
                    continue
                contact[edit_name]=new_phone
                save_contact(contact)
                print("联系人已删除！")

            elif choice==5:
                del_name=input("请输入要删除联系人的姓名").strip()
                if del_name not in contact:
                    print("该联系人不存在")
                    continue
                del contact[del_name]
                save_contact(contact)
                print("联系人已删除！")

            elif choice==0:
                print("通讯录已保存，程序结束")
                break
            else:
                print("请输入0-5的数字！")

        except ValueError:
            print("输入错误，请填写数字序号")
if __name__=="__main__":
    main()
