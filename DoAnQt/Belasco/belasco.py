#========================================
def MaHoa(plaintext,key):
    ciphertext=""
    for i in range(len(plaintext)):
        c = plaintext[i]
        if c!=' ':
            row = ord(key[i%len(key)]) - 33
            col = ord(c) - 33
            so = (row + col) % 65500
            ciphertext = ciphertext+ chr(so+ 33)
        else:
            ciphertext=ciphertext+' '
    return ciphertext
#========================================
def GiaiMa(ciphertext,key):
    plaintext = ""
    for i in range(len(ciphertext)):
        c=ciphertext[i]
        if c != ' ':
            row = ord(key[i%len(key)]) - 33
            col = ord(c) - 33
            so = (col - row + 65500) % 65500
            plaintext = plaintext+ chr(so+33)
        else:
            plaintext = plaintext+' '
    return plaintext
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    k =  input("Moi nhap chuoi key: ")
    k=k.upper()
    c = MaHoa(p,k)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c,k)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 