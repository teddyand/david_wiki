def  loan(p):
	payment=0
	intrest_m=0.005
	month=360-1

	while(month!=0):
		payment=payment / (1+intrest_m) +p
		month-=1

	return payment

