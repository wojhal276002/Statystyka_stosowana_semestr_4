dyrektor = [4,10,7.5,9,11,2,5,1,3,7.5,6]
wizytator = [5,11,6,8.5,10,2,3,1,4,7,8.5]
suma = [(dyrektor[i]-wizytator[i])**2 for i in range(len(dyrektor))]
suma_6 = 6*sum(suma)
r_s = 1-(suma_6/(11*120))
print(r_s)