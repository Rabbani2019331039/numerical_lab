import LU_decomp
from LU_decomp import matInv
from gaussElimin import gaussElimin
import take_input
import gaussElimin
import gaussianEliminPivoting
from print_solution import print_sol_le
from print_solution import print_invMat



op,a,b = take_input.take_input()

if op==1:
    res = gaussElimin.gaussElimin(a,b)
    print_sol_le(res)
elif op==2:
    res = gaussianEliminPivoting.gaussPivot(a,b)
    print_sol_le(res)
elif op==3:
    res = matInv(a)
    print_invMat(res)
else:
    print("bye bye")