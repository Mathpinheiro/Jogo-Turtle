from turtle import Turtle
t = Turtle()
t.speed(1)
print()
print("Siga as instrucoes a seguir:")
print()
while True:
   direcao = input("Para qual direção ir f:frente ou t:tras?: ")
   if direcao == "f":
    dist_f = int(input("Quanto devemos ir a frente?: "))
    print()
   if direcao == "t":
     dist_t = int(input("Quanto devemos ir para tras?: "))
     print()   
   rotacao = input("Rotacionar para d:direita, e:esquerda, n:não rotacionar: ")
   print()
   if rotacao == "d":
     dist_d = int(input("Quanto devemos rotacionar a direita?: "))
     t.right = (dist_d)
     t.forward = (dist_f)
   if rotacao == "e":
    dist_e = int(input("Quanto devemos rotacionar a esquerda?: "))
   t.left = (dist_e)
   t.forward = (dist_f)
   if rotacao == "n":
      t.forward(dist_f)
         
   if direcao == "t":
      dist_t = int(input("Quanto pixel devemos ir a trás?: "))
      print()
      rotacao = input("Rotacionar para d:direita, e:esquerda, n:não rotacionar: ")
      print()
      if rotacao == "d":
       dist_d = int(input("Quanto pixel devemos rotacionar a direita?: "))
       t.right = (dist_d)
       t.backward = (dist_t)
      if rotacao == "e":
       dista_e = int(input("Quanto pixel devemos rotacionar a esquerda?: "))
       t.left = (dist_e)
       t.backward = (dist_t)
       if rotacao == "n":
        t.backward = (dist_t)
         
       print()
       continuar = input("Continuar andando? s:sim n:não: ")
       if continuar == "n":
         break