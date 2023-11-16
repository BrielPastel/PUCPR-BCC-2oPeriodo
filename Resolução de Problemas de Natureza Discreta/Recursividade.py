#Questão 1

def A(n):
  if n == 1: return 10
  if n >= 2: return A(n - 1) + 10

print(f"Questão 1) a) A(5) = {A(5)}")

def B(n):
  if n == 1: return 2
  if n >= 2: return 1/B(n - 1)
    
print(f"Questão 1) b) B(5) = {B(5)}")

def C(n):
  if n == 1: return 1
  if n >= 2: return C(n - 1) + n**2

print(f"Questão 1) c) C(5) = {C(5)}")

def D(n):
  if n == 1: return 1
  if n >= 2: return n**2 * D(n - 1) + n - 1

print(f"Questão 1) d) D(5) = {D(5)}")

def E(n):
  if n == 1: return 3
  if n == 2: return 5
  if n > 2: return (n - 1) * E(n - 1) + (n - 2) * E(n - 2)

print(f"Questão 1) e) E(5) = {E(5)}")

def F(n):
  if n == 1: return 2
  if n == 2: return 5
  if n > 2: return F(n - 1) * F(n - 2)

print(f"Questão 1) f) F(5) = {F(5)}")

def G(n):
  if n == 1: return 1
  if n == 2: return 2
  if n == 3: return 3
  if n > 3: return G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3)

print(f"Questão 1) g) G(5) = {G(5)}")

# Questão 2

def progressao_geometrica(a, r, n):
  if n == 1:
      return a
  else:
      return progressao_geometrica(a, r, n - 1) * r

print(f"Questão 2) progressao_geometrica(2, 3, 5) = {progressao_geometrica(2, 3, 5)}")

# Questão 3

def T(n):
    if n == 2: return True
    elif n < 2: return False
    else: return T(n - 3) or T(n / 2)

numeros_T = [6, 7, 19, 12]
for i in numeros_T:
    if T(i):
        print(f'Questão 3) {i} pertence a T')
    else:
        print(f'Questão 3) {i} não pertence a T')

# Questão 4
def M(n):
  if n == 2 or n == 3: return True
  elif n < 2: return False
  else: 
     return M(n / 2) or M(n / 3)

numeros_M = [6, 9, 16, 21, 26, 54, 72, 218]
for i in numeros_M:
    if M(i):
        print(f'Questão 4) {i} pertence a M')
    else:
        print(f'Questão 4) {i} não pertence a M')

#Questão 5

def S(n):
    if n == "a" or n == "b":return True
    elif n[0] == "a":return S(n[1:])
    elif n[0] == "b":return S(n[1:])
    else:return False

sequenciaS = ["a", "ab", "aba", "aaab", "bbbbb"]

for string in sequenciaS:
    if S(string):
        print(f'Questao 5) "{string}" pertence a S')
    else:
        print(f'Questao 5) "{string}" não pertence a S')



#Questão 6
def W(n):
    if n == "a" or n == "b" or n == "c":return True
    elif n[0] == "a" and n[-1] == "c":return W(n[1:-1])
    else:return False

array = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]

for string in array:
    if W(string):
        print(f'Questão 6) "{string}" pertence a W')
    else:
        print(f'Questão 6) "{string}" não pertence a W')

#Questão 7
def binario_gerar(n, antes=""):
    if n == 0:
        if antes.count("0") % 2 != 0:
            print(f"Questão 7) {antes}")
    else:
        binario_gerar(n-1, antes + "0")
        binario_gerar(n-1, antes + "1")

binario_gerar(4)

#Questão 8
def A8(n):
    if n == 1:
        return 1
    else:
        return 3 * A8(n - 1)

print(f"Questão 8) a) A8(5) = {A8(5)}")

def B8(n):
  if n == 1: 
    return 2
  else:
    return .5 * B8(n - 1)

print(f"Questão 8) b) B8(5) = {B8(5)}")

def C8(n):
    if n == 1:
        return 'a'
    elif n == 2:
        return 'b'
    else:
        return C8(n-2) + C8(n-1)

print(f"Questão 8) c) C8(5) = {C8(5)}")

def D8(n, p, q):
    if n == 1:
        return 'p'
    elif n == 2:
        return 'p - q'
    elif n % 2 == 0:
        return D8(n-1, p, q) + ' + {}q'.format((n-1) // 2)
    else:
        return D8(n-1, p, q) + ' - {}q'.format(n // 2)

print(f"Questão 8) d) D8(5) = {D8(5, 5, 5)}")


#Questão 9
def pitagoras(n):
    if n == 1:
        return 1
    else:
        return n + pitagoras(n - 1)

print(f"Questão 9) pitagoras(5) = {pitagoras(5)}")

# Questão 10
def bacterias(n, populacao_inicial):
    if populacao_inicial >= 200000:
        return n
    else:
        return bacterias(n+1, 3 * populacao_inicial)

leituras = bacterias(0, 50000)

print(f'Questão 10) Execuções para ter mais de 200,000 bactérias: {leituras}')


#Questão 11
def Rotina(L, j):
    if j == 1:
        return L

    i = L.index(max(L[:j]))
    L[i], L[j-1] = L[j-1], L[i] 
    return Rotina(L, j-1)

L = [3, 7, 4, 2, 6]
lista = Rotina(L, len(L))

print(f"Questão 11) Lista:{lista}")


print("\nTrabalho feito por: Gabriel Berto Beckauser e Henrique De Conti")
