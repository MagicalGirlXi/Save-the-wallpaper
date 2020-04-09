import os
import shutil

        
def main():
    if "TEMP" in os.environ:
        temp_path = os.environ["TEMP"]
        user_name = temp_path.split("\\")[2]
        print("Detected your user_name is %s"%user_name)
    else:
        user_name = input("Can not get your user name, please enter the name of your user folde: ")
    orig_path = r"C:/Users/"+user_name+r"/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
    temp = r"C:/Users/"+user_name+"/Desktop/聚焦壁纸/temp/"
    target_path = "C:/Users/"+user_name+"/Desktop/聚焦壁纸/"
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    files = os.listdir(orig_path)     
    print ("Orig_path = \"%s\" "%orig_path)
    print ("Target_path = \"%s\" "%target_path)
    for filename in files:
        portion = os.path.splitext(filename)
        if not os.path.exists(target_path+filename+".jpg"):
            if not os.path.exists(target_path+filename):
                f = open(target_path+filename,'w')
                print ("created "+filename)
                f.close()
            shutil.copyfile(orig_path+filename, target_path+filename)
            os.rename(target_path+filename,target_path+filename+".jpg")
    print("Copy Finished")
# 增加调用main()函数
if __name__ == '__main__':
    main()
    os.system("pause")