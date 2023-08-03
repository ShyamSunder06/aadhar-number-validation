
p=""
n=input("enter the aadhar  no:")#step 1
w=n.split()#step 2
if len(w)==3:#step 3
  for i in w:
    if len(i)==4 and i.isdigit():
      p+=i
if len(p)==12:
          print("aadhar no is valid")
else:
        print("aadhar no is not valid")
