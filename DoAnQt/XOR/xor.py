def MaHoa_GiaiMa(plaintext, key):
    ci =''
    for c in plaintext:
        so = ord(c) - 65536 
        ci += (chr) ((so ^ key)+65536)
    return ci 
##===================================

def main():
    p = input('Moi nhap chuoi: ')
    k =3 
    c = MaHoa_GiaiMa(p, k) ##
    print("Sau khi ma hoa: ", c)
    s = MaHoa_GiaiMa(c, k)
    print("Sau khi giai ma: ",s)

#===================================
if __name__=="__main__": #entry point
    main()