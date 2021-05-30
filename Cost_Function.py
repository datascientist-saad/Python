# Calculating the cost function
def cost_fun(th0, th1, m):
    x = []
    y = []
    h = []
    j = []
    total = 0
    for i in range(m):
        x.append(float(input(f"Enter x{i+1}: ")))
        y.append(float(input(f"Enter y{i+1}: ")))
        h.append(th0 + th1*x[i])
        # for_sum.append(sum(h[i] - y[i])**2)
        sq_sum = (h[i] - y[i])**2
        total += sq_sum
        j.append(int((1/2*m) * total))

    # print("list x: ", x)
    # print("list y: ", y)
    # print("list h: ", h)

    return j


m = int(input("Enter number of training examples := "))

for i in range(m):
    th0 = int(input("Enter theta 0:= "))
    th1 = float(input("Enter theta 1:= "))
    print(cost_fun(th0, th1, m))
