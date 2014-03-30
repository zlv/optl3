from math import *

class Func:
    def eval(self, x) :
        return x[0]**4+x[1]**4+2*x[0]**2*x[1]**2-4*x[0]+3
        return 1-2*x[0]-2*x[1]-4*x[0]*x[1]+10*x[0]**2+2*x[1]**2
        return (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2
        return 2*x[0]**2+x[0]*x[1]+x[1]**2
        return 4*(x[0]-5)**2+(x[1]-6)**2

def check_end(step,eps) :
    sum = 0
    for delta_i in step :
        sum += delta_i*delta_i
    sum = sqrt(sum)
    return sum<eps

def search1(func,x,step,eps) :
    search2(func,x,step,1)
    return not check_end(step,eps)

def search2(func,x,step,bChangeStep=0) :
    alpha = 2.
    inc = [+0.5,-0.5]
    i = 0
    y = func.eval(x)

    for c in x :
        bFoundNew = 0
        for sign in inc :
            newx = list(x)
            newx[i] += sign*step[i]
            newy = func.eval(newx)
            if (y>newy) :
                y=newy
                x[i]=newx[i]
                bFoundNew = 1
                break
        if not bFoundNew and bChangeStep :
            step[i]/=alpha
        i += 1

def copy(x1,x2) :
    i = 0
    for x2_i in x2 :
        x1[i]=x2_i
        i += 1

def compare(x1,x2) :
    i = 0
    for x2_i in x2 :
        if x1[i]!=x2_i :
            return 0
        i += 1
    return 1

def pattern_search(func,x1,x2,step) :
    while 1 :
        lmbd = 2.
        x3 = list(x1)
        i = 0
        for x2_i in x2 :
            x3[i]+=lmbd*(x2_i-x3[i])
            i += 1
        x4 = list(x3)
        search2(func,x4,step)
        copy(x1,x2)
        if compare(x3,x4) :
            copy(x2,x4)
        else :
            return

def check_end2(x1,x2,eps) :
    i = 0
    sum = 0
    for x2_i in x2 :
        dif = x2_i-x1[i]
        sum += dif*dif
        i += 1
    sum = sqrt(sum)
    return sum<eps

def Hooke_Jeeves(x0, func, eps, y) :
    x1 = list(x0)
    x2 = list(x0)
    default_step = 0.1
    step = [default_step, default_step]
    print x2
    while search1(func,x2,step,eps) :
        print x2
        if check_end2(x1,x2,eps) :
            break
        pattern_search(func,x1,x2,step)
        copy(x2,x1)
    copy(x0,x2)
    y[0] = func.eval(x0)

x0 = [0.,0.]
func = Func()
eps = 1e-5
y = [0.]
Hooke_Jeeves(x0,func,eps,y)
print(x0)
