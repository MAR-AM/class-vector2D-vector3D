from vecteur import Vecteur2D

V1 = Vecteur2D (1,6)
V1.Tostring()
V1.norme()
V2 = Vecteur2D (2,4)
V2.Tostring()

print("\nare equal ??",V1.Equals(V2))

V3 = Vecteur2D (3,9)
V3.Tostring()
V3.norme()
V4 = Vecteur2D (6/2,3*3)
V4.Tostring()
V3.Equals(V4)
print("\nare equal ??",V3.Equals(V4))



