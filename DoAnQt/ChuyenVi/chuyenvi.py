#========================================
def MaHoa(plaintext):
    ciphertext=plaintext[0]
    for i in range(1, len(plaintext), 2) :
        ciphertext=ciphertext+plaintext[i]
    for i in range(2, len(plaintext), 2) :
        ciphertext=ciphertext+plaintext[i]
    return ciphertext
#========================================
def GiaiMa(ciphertext):
    plaintext=list(ciphertext)
    k=1
    for i in range(1, len(plaintext), 2) :
        plaintext[i] = ciphertext[k]
        k=k+1
    for i in range(2, len(plaintext), 2) :
        plaintext[i] = ciphertext[k]
        k=k+1
    return ''.join(x for x in plaintext)
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    p=p.upper()
    c = MaHoa(p)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main()


    
