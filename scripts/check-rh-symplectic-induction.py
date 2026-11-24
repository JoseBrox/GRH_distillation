"""Exact symbolic checks for the two integral flag charts."""
import sympy as S

M = S.Matrix
J2 = M([[0, 1], [-1, 0]])
J = M([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]])
a,b,g,u,w,x,x1,y,y1,p,q = S.symbols('a b g u w x x1 y y1 p q', nonzero=True)

def eq(A, B):
    assert all(S.cancel(z) == 0 for z in A-B)

P = M([[0,a,0,a], [b,0,-b,0], [0,-1,0,1], [1,0,1,0]])
eq(P.T*S.diag(J2,a*b*J2)*P, -2*a*b*J)
D = S.diag(a*a,b*b)
I = M.vstack(M.hstack(S.zeros(2),D), M.hstack(S.eye(2),S.zeros(2)))
eq(P.inv()*I*P, S.diag(b,-a,-b,a))

def mix(A,B):
    C = P.subs({a:1,b:g})
    return C.inv()*S.diag(A,B)*C

A = M([[x1+u*p,(x-x1-u*p)*u],[p,x-p*u]])
B = M([[y-q*w,q],[(y-y1-q*w)*w,y1+q*w]])
def N(p,q,r,z,t):
    return M([[1,0,0,0],[p,1,0,0],[q,z,1,0],[r,t,-p,1]])

for C,T,diag in [
    (mix(A,B),N(g*u,-1,g*u,-2*w/(1+g*u*w),-(1-g*u*w)/(1+g*u*w)),[x,y,y1,x1]),
    (mix(B,A),N(-u,1,u,-2*w/(g+u*w),(g-u*w)/(g+u*w)),[x,y,y1,x1])
]:
    eq(T.T*J*T,J)
    E = T.inv()*C*T
    assert all(S.cancel(E[i,j])==0 for i in range(4) for j in range(i))
    assert all(S.cancel(E[i,i]-diag[i])==0 for i in range(4))
print("Induction matrix, symplectic form, both integral flag charts: verified symbolically.")
