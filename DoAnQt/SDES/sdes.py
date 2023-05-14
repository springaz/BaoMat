import math
class BitSet():
    value = 0
    length = 0
    @classmethod
    def from_sequence(cls, seq):
        n = 0
        for index, value in enumerate(reversed(seq)):
            n += 2**index * bool(int(value))
        return BitSet(n)
    @classmethod
    def from_list(cls, lst): 
        n = 0
        for index, value in enumerate(reversed(lst)):
            n+= 2**index * bool(int(value))
        return BitSet(n, len(lst))
    def __init__(self, value=0, length=0):
        self.value = value
        try: self.length = length or math.floor(math.log(value, 2)) + 1
        except Exception: self.length = 0
    def __and__(self, other):
        b = BitSet(self.value & int(other))
        b.length = max(self.length, b.length)
        return b
    def __or__(self, other):
        b = BitSet(self.value | int(other))
        b.length = max(self.length, b.length)
        return b
    def __invert__(self):
        b = BitSet(~self.value)
        b.length = max(self.length, b.length)
        return b
    def __xor__(self, other):
        b = BitSet(self.value ^ int(other))
        b.length = max(self.length, b.length)
        return b
    def __lshift__(self, value):
        b = BitSet(self.value << int(value))
        b.length = max(self.length, b.length)
        return b
    def __rshift__(self, value):
        b = BitSet(self.value >> int(value))
        b.length = max(self.length, b.length)
        return b
    def __eq__(self, other):
        try: return self.value == other.value
        except Exception: return self.value == other
    def __int__(self):
        return self.value
    def __str__(self):
        s=''
        for i in self[:]:
            s += '1' if i else '0'
        return s
    def __repr__(self):
        return 'BitSet(%s)'%str(self)
    def __getitem__(self, s):
        try:
            start, stop, step = s.indices(len(self))
            results = []
            for position in range(start, stop, step):
                pos = len(self) - position - 1
            results.append(bool(self.value & (1<<pos)))
            return results
        except:
            pos = len(self) - s -1
        return bool(self.value & (1 <<pos))
    def __setitem__(self, s, value):
        try:
            start, stop, step = s.indices(len(self))
            for position in range(start, stop, step):
                pos = len(self) - position - 1
            if value: self.value |= (1 << pos)
            else: self.value &= ~(1<<pos)
            maximun_position = max(start + 1, stop, len(self))
            self.length = maximun_position
        except:
            pos = len(self) - s - 1
            if value: self.value |= (1 << pos)
            else: self.value &= ~(1<<pos)
            if len(self) < pos: self.length = pos
        return self
    def __iter__(self):
        for i in self[:]:
            yield i
    def __len__(self):
        return self.length
#=================================================
def Permutation(b, p):
    results = BitSet(0, len(p))
    vt = 0
    for item in p:
        results[vt] = b[item-1]
    vt+=1
    return results
#=================================================
def ShiftLeftCircle(b):
    t = b[0]
    b = b << 1
    if t:
        b[5] = t
        return BitSet.from_list(b[1:])
    return b
#=================================================
def Ghep(b1, b2):
 results = BitSet(int(b1), len(b1)+len(b2))
 results <<= len(b2)
 results |= b2
 return results
#=================================================
a10 = [3,5,2,7,4,10,1,9,8,6]
a8 = [6,3,7,4,8,5,10,9]
aIP = [2,6,3,1,4,8,5,7]
aEP = [4,1,2,3,2,3,4,1]
aS0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
aS1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
a4 = [2,4,3,1]
aIP_1 = [4,1,3,5,7,2,8,6]
#=================================================
def TaoKhoa(Key):
 #--- slide 17 ---
 p10 = Permutation(Key, a10)
 print("P10 = %12s"%p10)
 print("Left: ",end='\t')
 p10_L = BitSet.from_list(p10[:5]) 
 print(p10_L, end='\t')
 p10_L= ShiftLeftCircle(p10_L)
 print(p10_L)
 print("Right: ", end='\t')
 p10_R = BitSet.from_list(p10[5:])
 print(p10_R,end='\t')
 p10_R= ShiftLeftCircle(p10_R)
 print(p10_R)
 LS1= Ghep(p10_L,p10_R)
 print('LS1= %s'%LS1)
 #-----slide 18------
 K1 = Permutation(LS1, a8 ) #P8 chính là K1
 print("K1= %s"%K1)
 p10_L= ShiftLeftCircle(p10_L)
 p10_R= ShiftLeftCircle(p10_R)
 LS2= Ghep(p10_L,p10_R)
 print('LS2= %s'%LS2)
 #------slide 19-----------
 K2 = Permutation(LS2, a8) #P8 lần 2 => K2
 print("K2= %s"%K2)
 #-----------------
 return K1,K2
#=================================================
def S_Box(XOR, S0, S1): #slide 23
 #------ tạo S0 ------
 XOR_L = BitSet.from_list(XOR[:4])
 row = BitSet(0,2)
 row[0]=XOR_L[0]
 row[1]=XOR_L[3]
 col = BitSet(0,2)
 col[0] = XOR_L[1]
 col[1] = XOR_L[2]
 n = S0[int(row)][int(col)]
 print(n)
 s0 = BitSet(n,2)
 print("S0= %s"%s0)
 #------ tạo S1 ------
 XOR_R = BitSet.from_list(XOR[4:])
 row = BitSet(0,2)
 row[0]=XOR_R[0]
 row[1]=XOR_R[3]
 col = BitSet(0,2)
 col[0] = XOR_R[1]
 col[1] = XOR_R[2]
 n = S1[int(row)][int(col)]
 print(n)
 s1 = BitSet(n,2)
 print("S1= %s"%s1)
 return s0,s1
#=================================================
def MaHoa(data, K1, K2):
 IP = Permutation(data, aIP )
 print("IP= %s"%IP) #'''slide 20'''
 IP_R = BitSet.from_list(IP[4:])
 print("IP_R= %s"%IP_R)
 EP = Permutation(IP_R, aEP)
 print("EP= %s"%EP) #'''slide 21'''
 XOR = EP ^ K1
 print("XOR= %s"%XOR)
 S0, S1= S_Box(XOR, aS0,aS1)
 S0 = Ghep(S0, S1) #slide 23
 P4 = Permutation(S0, a4)
 print("P4= %s"%P4)
 IP_L = BitSet.from_list(IP[:4])
 XOR = P4 ^ IP_L
 print("XOR= %s"%XOR)
 FK1 = Ghep(XOR, IP_R)
 print('FK1= %s'%FK1) #slide 24
 SW = Ghep(IP_R, XOR)
 SW_R = XOR
 SW_L = IP_R
 print("SW= %s"% SW)
 EP = Permutation(XOR, aEP)
 print("EP= %s"%EP)
 XOR = EP ^ K2
 print("XOR= %s"%XOR)
 S0, S1= S_Box(XOR, aS0,aS1)
 S0 = Ghep(S0, S1) #slide 25
 P4 = Permutation(S0, a4)
 print("P4= %s"%P4)
 XOR = P4 ^ SW_L
 print("XOR= %s"%XOR)
 FK2 = Ghep(XOR, SW_R) 
 print("FK2= %s"%FK2) #slide 26
 IP_1 = Permutation(FK2, aIP_1)
 print("IP_1= %s"% IP_1)
 return IP_1 #slide 27
#=================================================
def GiaiMa(Ci, K1, K2):
 IP = Permutation(Ci, aIP)
 print("IP= %s"%IP) #slide 30
 IP_R = BitSet.from_list(IP[4:])
 EP = Permutation(IP_R, aEP)
 print("EP= %s"%EP)
 XOR = EP ^ K2
 print("XOR= %s"%XOR)
 S0, S1 = S_Box(XOR, aS0, aS1)
 S = Ghep(S0, S1) #slide 31
 print("S= %s"%S)
 P4 = Permutation(S, a4)
 print("P4= %s"%P4)
 IP_L = BitSet.from_list(IP[:4])
 XOR = P4 ^ IP_L
 print("XOR= %s"%XOR)
 FK2 = Ghep(XOR, IP_R)
 print("FK2= %s"%FK2) #slide 32
 SW = Ghep(IP_R, XOR)
 print("SW= %s"%SW)
 SW_L = IP_R
 SW_R = XOR
 print("SW_R= %s"%SW_R)
 EP = Permutation(SW_R, aEP)
 print("EP= %s"%EP)
 XOR = EP ^ K1
 print("XOR= %s"%XOR)
 S0, S1 = S_Box(XOR, aS0, aS1)
 S = Ghep(S0, S1) #slide 33
 print("S= %s"%S)
 P4 = Permutation(S, a4)
 print("P4= %s"%P4)
 XOR = P4 ^ SW_L
 print("XOR= %s"%XOR)
 FK2 = Ghep(XOR, SW_R)
 print("FK2= %s"%FK2) #slide 34
 IP_1 = Permutation(FK2, aIP_1)
 print("IP_1= %s"%IP_1)
 return IP_1 #slide 35
#=================================================
def Run():
 print('Demo slide 15')
 data = BitSet.from_sequence("10100011")
 print("Data= %12s"%data)
 Key = BitSet.from_sequence("1101110001")
 print("Key = %12s"%Key)
 print('============================')
 print('***** DEMO Tạo khoá *****')
 K1,K2= TaoKhoa(Key)
 print('============================')
 print('***** DEMO Mã hoá *****')
 Ci= MaHoa(data, K1, K2)
 print("Ciphertext= %s"%Ci)
 print('============================')
 print('***** DEMO giải mã *****')
 P= GiaiMa(Ci, K1, K2)
 print("Sau khi giải mã: %s"%P)
#=================================================
if __name__ == '__main__':
 Run()