import scipy as sp
import matplotlib.pyplot as plt

def error(f,x,y):
	return sp.sum((f(x)-y)**2)

data = sp.genfromtxt("web_traffic2.tsv",delimiter="\t")
#Splitting the 2D datapoints files in two vectors
x=data[:,0] #Hours
y=data[:,1] #hits per hours
#Remove from the datapoints invalid values
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]

print x
print y
plt.scatter(x,y)
plt.title("Web Traffic Per hour")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks(
[w*7*24 for w in range(10)],
['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

#ScyPy polifit find the best polinomial or straight line(order =1 straight ) which
#minimiezes the error
fp1,residual,rank,sv,rcond =sp.polyfit(x,y,1,full=True)

print("Model parameter:%s" % fp1)

#best straight line 
f1 = sp.poly1d(fp1)

print(error(f1,x,y))

#generate X-values(24) for plotting of our best line
fx = sp.linspace(0,x[-1],24)
print fx
plt.plot(fx,f1(fx),linewidth=4)

f2p = sp.polyfit(x,y,2)
print (f2p)
f2 = sp.poly1d(f2p)
print (error(f2,x,y))
plt.plot(fx,f2(fx),linewidth=4)
plt.show()




