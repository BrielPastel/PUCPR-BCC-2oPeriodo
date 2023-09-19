#Definição de função f para cálculo

def f(x):
    return x**2
  
#Definição de função g para cálculo
def g(x):
    return x/3
  
#Cálculo para g de f de x
def g_f(x):
    return g(f(x))

#Cálculo para g de g de x
def g_g(x):
    return g(g(x))

#Cálculo para f de f de x
def f_f(x):
    return f(f(x))

#Cálculo para f de f de x
def f_g(x):
    return f(g(x))

# Teste com alguns valores
x = int(input("Valor de x: "))

# Resultados
print("(g°f) = ({})".format(g_f(x)))
print("(g°g) = ({})".format(g_g(x)))
print("(f°f) = ({})".format(f_f(x)))
print("(f°g) = ({})".format(f_g(x)))
