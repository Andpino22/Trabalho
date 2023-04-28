numero1=int(input('Digite o numero:'))
operacao=input('digite a operação:')
numero2=int(input('Digite o numero:'))

rs=('resultado')
if operacao == '+':
    resultado = numero1+numero2
if operacao == '-':
    resultado = numero1-numero2
if operacao == '/':
    resultado = numero1/numero2
if operacao == '*':
    resultado = numero1*numero2
    

print('__________________________________________________________________')
print('.')
print('Este e o resultado:',resultado)    
print('.')
print('__________________________________________________________________')



