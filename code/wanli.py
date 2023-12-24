def  repay(gain):
	pool=200000
	surplus=pool - gain
	n=1
	a=[] #每月结余钱数
	a.append(200000)
	while(surplus >=0 and surplus<6000000):
		a.append(surplus)
		surplus=surplus*1.005-gain
		n+=1

	return n,a

n,a=repay(5000)

m,b=repay(800)


import matplotlib.pyplot as plt

print(a)
print(n)
month = [i for i in range(0,n)]
month2 = [i for i in range(0,m)]
fig, axs = plt.subplots(1,2)
axs[0].plot(month,a,linestyle='None',marker='o')
#axs[0].vlines(month,0,a)
axs[0].set_xlabel('month')
axs[0].set_ylabel('surplus')
axs[0].set_title("c=5000")

axs[1].plot(month2,b,linestyle='None',marker='o')
axs[1].set_xlabel('month')
axs[1].set_ylabel('surplus')
axs[1].set_title("c=800")
plt.show()

