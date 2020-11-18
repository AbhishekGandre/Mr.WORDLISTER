import time

#colors
red='\033[91m'
b='\033[21m'
green='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'

print (red+"""                                                 
              !!\  /!!            /_\      /||   !!==!!   ===\   !!   !!  ~~!!~~    
              !! \/ !!           //  \    / ||   !!   ))     ))  !!   !!    !!       
              !!    !!  !! /)   //----\     ||   !!===||    //   !!===!!    !!      
              !!    !!  !!/    //------\    ||   !!   ))   //    !!   !!    !!     
              !!    !!  !! o  //        \   ||   !!==!!   /====  !!   !!  ~~!!~~
              
              Mr .W     O      R      D      L      I      S      T      E     R    """+red)


print (red+"             *<==****************$ WELCOME TO Mr.WORDLISTER $****************==>*"+red)

print (green+"             *<====================[[ coded by A1B2HI ]]=======================>*"+green)

print (yellow+"             *<------------( search on youtube Abhishek Gandre)---------------->*"+yellow)


length=int(raw_input(cyan+b+"Enter The Number Of Characters: "+b+cyan))
print (" ")
name=raw_input(cyan+b+"Name Your Wordlist Wit (.txt) Extension: "+b+cyan)
tic = time.clock()
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
print (yellow+b+"Wordlist Generating Please Wait!"+b+yellow)
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
lista=[0 for x in xrange(length)]
x=length-1
string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*-_+=|)(/?>.<,~`"
list_of_results=[]
file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print (red+b+"<<<========================================>>>"+b+red)
print (" ")
print (green+b+"Completed in "+str(ttn)+" seconds."+b+green)
print (" ")
print (green+b+"Please check "+str(name)+" in your Mr.WORDLISTER Directoy"+b+green)
print (" ")
print (red+"THANK YOU SO MUCH FOR USING PLEASE SUBSCRIBE TO MY CHANNEL"+red)
print (red+b+"<<<========================================>>>"+b+red)
