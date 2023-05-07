
#========================================
def MaHoa(plaintext, key):
    ciphertext=""
    for i in range(len(plaintext)):
        c = plaintext[i]
        vt_key=i% len(key)
        if c!=' ':
            so = ord(c) - 33;
            so_key=ord(key[vt_key])-33+1 #Tùy cách tính
            so = (so+so_key) % 65500
            ciphertext = ciphertext+ chr(so+ 33)
        else:
            ciphertext=ciphertext+' '
    return ciphertext
#========================================
def GiaiMa(ciphertext,key):
    plaintext = ""
    for i in range(len(ciphertext)):
        c=ciphertext[i]
        vt_key=i%len(key)
        if c != ' ':
            so = ord(c)- 33
            so_key=ord(key[vt_key])-33+1 #?????
            so = (so - so_key + 65500) % 65500
            plaintext = plaintext+ chr(so+33)
        else:
            plaintext = plaintext+' '
    return plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    # p=p.upper()
    key="ABC"
    c = MaHoa(p, key)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c,key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()



    


    
