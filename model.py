import pulp

# weights of the boats

def schedule_optimize(weights):

    num_boats = len(weights)
    window_size = 6

    prob = pulp.LpProblem("Boat scheduling", pulp.LpMinimize)

    x = {i: {j: pulp.LpVariable('x:{}:{}'.format(i, j), cat=pulp.LpBinary, lowBound=0, upBound=1) for j in range(num_boats)} for i in range(num_boats)}

    objective = pulp.LpVariable('objective_var')

    # set objective function for model
    prob += objective

    # make constriant that each boat must be in exactly one slot


    # objective function

    for start in range(num_boats - (window_size-1)):
        window_expression = sum(weights[boat] * sum(x[boat][start + i] for i in range(window_size)) for boat in range(num_boats))
        prob += objective >= window_expression

    for i in range(num_boats):
        prob+= sum(x[i][j] for j in range(num_boats)) ==1

    for j in range(num_boats):
        prob+= sum(x[i][j] for i in range(num_boats))==1


    prob.solve(pulp.COIN_CMD(maxSeconds=3))
    outputdic=[i for i in range(num_boats)]
    output_order=[i for i in range(num_boats)]
    for v in prob.variables():
        if v.name.startswith("x"):
            if v.varValue==1:
                parts= v.name.split(":")
                outputdic[int(parts[2])]=weights[int(parts[1])]
                output_order[int(parts[2])]=int(parts[1])
        if v.name.startswith("objective"):
            objective=v.varValue
            print(objective)

    print(outputdic)
    print(output_order)

    running_avg=[i for i in range(num_boats)]
    for i in range(window_size-1):
        running_avg[i]="-"
    for start in range(num_boats-(window_size-1)):
        window_amount=sum(outputdic[start+i] for i in range(window_size))
        running_avg[(window_size-1)+start]=window_amount
    print(running_avg)
    return outputdic, output_order, running_avg
