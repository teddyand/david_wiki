def   dec2bin_ex(target):
	#将target分离成整数和小数部分
	i= int(target) #整数部分
	f = target - i #小数部分

	#将整数部分转换位二进制数
	a = [] #剩余部分列表

	#直到商为0
	while i !=0:
		a.append(i%2) #余数
		i = i//2 #商

    #把元素按相反的顺序排列
	a.reverse()

	#将小数部分转换为二进制数
	b =[] #带有整数部分列表
	n =0 # 重复次数

	#乘以2直到小数部分为0
	while (f !=0):
		temp =f*2 #小数部分*2
		b.append(int(temp)) #整数部分
		f = temp -int(temp) #小数部分
		n+=1
		if(n>=10):
			break

	#值转换为二进制
	return a,b
