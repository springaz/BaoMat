import numpy as np
import math
#========================================
def TimViTriX(key, x):
    for i in range(len(key)):
        if key[i]==x:
            return i
    return -1;
#========================================
def MaHoa(plaintext,key):
    soCot = len(key)
    soDong = math.ceil(len(plaintext)/soCot)
    tam = []
    k=0
    for i in range(soDong):
        row = []
        for j in range(soCot):
            if k>=len(plaintext): row+=['*']; continue
            row+=[plaintext[k]]; k+=1
        tam+=[row]
    ciphertext = ""
    for i in range(1,len(key)+1,1):
        viTriCot = TimViTriX(key,i)
        for r in tam:
            ciphertext += r[viTriCot]
    return ciphertext
#========================================
def GiaiMa(ciphertext,key):
    soCot = len(key)
    soDong = math.ceil(len(ciphertext)/soCot)
    tam = np.zeros((soDong, soCot))
    i=0
    for k in range(1,len(key)+1,1):
        viTriCot = TimViTriX(key,k)
        for r in range(soDong):
            tam[r][viTriCot]=ord(ciphertext[i]); i+=1
    plaintext=""
    for r in tam:
        for c in r:
            plaintext+=chr(int(c))
    return plaintext.rstrip('*')
#========================================
def main():
    p =  input("Moi nhap chuoi can ma hoa: ")
    k=[3,5,6,7,2,1,4]
    c = MaHoa(p,k)
    print("Sau khi ma hoa= ", c)
    s= GiaiMa(c,k)
    print("Sau khi giai ma= ",s)
#========================================
if __name__=="__main__": #entry point
    main() 