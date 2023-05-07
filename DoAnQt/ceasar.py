
def MaHoa(plaintext, key):
    ciphertext=""
    for c in plaintext:
        if c!=' ':
            so = ord(c) - 33
            so = (so+key) % 65500
            ciphertext = ciphertext+ chr(so+ 33)
        else:
            ciphertext=ciphertext+c
    return ciphertext
#========================================
def GiaiMa(ciphertext,key):
    plaintext = ""
    for c in ciphertext:
        if c != ' ':
            so = ord(c)- 33
            so = (so - key + 65500) % 65500
            plaintext = plaintext+ chr(so+33)
        else:
            plaintext = plaintext+c
    return plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    key=3
    c = MaHoa(p, key)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c,key)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 