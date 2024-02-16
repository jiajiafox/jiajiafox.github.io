old_name=input('要備份的文件名稱:')
index=old_name.rfind('.')
new_name=old_name[:index]+'[複製]'+old_name[index:]
old_f=open(old_name,'rb')   #讀二進制
new_f=open(new_name,'wb')   #寫二進制

while True:
    con=old_f.read(1024)
    if len(con)==0:
        break