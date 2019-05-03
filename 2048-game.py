import random


def rasgele_olustur(matris):
    while True:
        rasx=random.randint(0,3)
        rasy=random.randint(0,3)
        if(matris[rasx][rasy]==0):
            matris[rasx][rasy]=2
            break
        elif (matris[rasx][rasy]==2):
            matris[rasx][rasy]=4
    return matris

def yukariasagi(matris,yon):
    
    for k in range(4):
        cikis=0
        for i in range(4):
            for j in range(4):
                if(i!=j and (abs(i-j)<2) and matris[j][k]!=0):
                    if matris[i][k]==matris[j][k]:
                        matris[i][k]=matris[i][k]*2
                        matris[j][k]=0
                        cikis=1
                    matris=hareket_ettir(matris,yon)
                    break
            if cikis==1:
                break
        
    return matris

def sagasola(matris,yon):
    
    for k in range(4):
        cikis=0
        for i in range(4):
            for j in range(4):
                if(i!=j and (abs(i-j)<2) and matris[k][j]!=0):
                    if matris[k][i]==matris[k][j]:
                        matris[k][j]=matris[k][j]*2
                        matris[k][i]=0
                        cikis=1
                    matris=hareket_ettir(matris,yon)
                    break
            if cikis==1:
                break
        
    return matris

def hareket_ettir(matris,yon):
    for k in range(4):
        for i in range(3):
            for j in range(3):
                if(yon==1):
                    if(matris[-j-2][k]==0):
                        matris[-j-2][k]=matris[-j-1][k]
                        matris[-j-1][k]=0
                elif(yon==2):
                    if(matris[j+1][k]==0):
                        matris[j+1][k]=matris[j][k]
                        matris[j][k]=0
                elif(yon==3):
                    if(matris[k][j+1]==0):
                        matris[k][j+1]=matris[k][j]
                        matris[k][j]=0
                elif(yon==4):
                    if(matris[k][-j-2]==0):
                        matris[k][-j-2]=matris[k][-j-1]
                        matris[k][-j-1]=0               
    return matris

def duzelt_ve_goster(matris):
    print "\n" * 25
    puan=0
    print "\n"+25*" "+"|"+24*"-"+"|"
    for i in range(4):
        sepet=25*" "+"|"
        for j in range(4):
            puan+=matris[i][j]
            if(len(str(matris[i][j]))<=6):
                if(matris[i][j]==0):
                    sepet+=6*" "
                else:
                    sepet+=str(matris[i][j])+((6-len(str(matris[i][j])))*" ")
        if(i==3):
            print sepet+"|\n"+25*" "+"|"+24*"-"+"|"
        else:
            print sepet+"|\n"+25*" "+"|"+24*" "+"|"
    print
    print "puaniniz: ",puan,"\n"
    
def calistir():
    matris=[[0 for i in range(4)]for j in range(4)]
    matris=rasgele_olustur(matris)
    matris=rasgele_olustur(matris)
    while True:
        duzelt_ve_goster(matris)
        yonlendir=raw_input("w a s d giriniz: ")
        if(yonlendir=='w'):
            (matris)=yukariasagi(matris,1)
        elif(yonlendir=='s'):
            (matris)=yukariasagi(matris,2)
        elif(yonlendir=='d'):
            (matris)=sagasola(matris,3)
        elif(yonlendir=='a'):
            (matris)=sagasola(matris,4)
        matris=rasgele_olustur(matris)
        
calistir()
