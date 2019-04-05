from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from . import templates
from .blindSignature import blindAttack
from .chosenCipherText import cctAttack
def cyclicAttack(n,e,c):
	c0 = c

	c1 = None
	li = [] 
	#file = open("output.txt","a")
	while ( c1 != c):
		c1 = pow(c0,e,n)
		print(c1,end=" ")
		li.append(c1)
		#file.write(str(c1) + "\n")
		prev = c0
		c0 = c1
		#c1 = None
	li.append(prev)
	return li
# Create your views here.
def index(request):
	return render(request,"home/templates/home.html")

def cct(request):
	return render(request,'home/templates/cct.html')
def cctSubmit(request):
	cipher = request.POST.get('cipher')
	p = request.POST.get('p')
	q = request.POST.get('q')
	r = request.POST.get('r')
	e = request.POST.get('e')
	output = cctAttack(cipher,int(p),int(q),int(r),int(e))
	print(output)
	return render(request,'home/templates/cct.html',{'output':output['li'],'rInv':output['rInv'],'d':output['d'],'flag':0})
def cyclic(request):
	#output = cyclicAttack(323,5,2)
	return render(request,'home/templates/cyclic.html')
	#return HttpResponse(str(output))
def cyclicSubmit(request):
	n = request.POST.get('n')
	e = request.POST.get('e')
	c = request.POST.get('c')
	output = cyclicAttack(int(n),int(e),int(c))
	print(output)
	if output == 1:
		return render(request,'home/templates/cyclic.html',{'output':"R value wrong",'flag':1})
	if output == 2:
		return render(request,'home/templates/cyclic.html',{'output':"E value wrong",'flag':1})
	return render(request,'home/templates/cyclic.html',{'output':output})

def blind(request):
	return render(request,'home/templates/blind.html')
def blindSubmit(request):

	plain = request.POST.get('cipher')
	p = request.POST.get('p')
	q = request.POST.get('q')
	r = request.POST.get('r')
	e = request.POST.get('e')
	output = blindAttack(plain,int(p),int(q),int(r),int(e))
	print(output)
	if output == 1:
		return render(request,'home/templates/blind.html',{'output':"R value wrong",'flag':1})
	if output == 2:
		return render(request,'home/templates/blind.html',{'output':"E value wrong",'flag':1})
	return render(request,'home/templates/blind.html',{'output':output['li'],'rInv':output['rInv'],'d':output['d'],'flag':0})
