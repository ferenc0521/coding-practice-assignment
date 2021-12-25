#find the minimum cost you'll need to spend on each meal
#cntProducts an integer representing the total number of products you will be using in all of your meals
#quantities[i][j] = represents the product j available in shop i
#costs [i][j]     = represent cost of product j from shop i
#meals [m][j]     = represent the amount of product j required to make the mth meal
cntProducts = 2
quantities = [ [1,3],[2,1],[1,3] ]
costs =      [ [2,4],[5,2],[4,1] ]
meals =      [ [1,1],[2,2],[3,4] ]
#The output should be solution( ) = [ 3 , 8, 19 ]
def check_quantities_single(meal,store):
    enough=[]
    for p in range(cntProducts):
        e=0
        if quantities[store][p] >= meals[meal][p]:
            e=1
            enough.append(e)
        else:
            break
    if len(enough) < cntProducts :
        print 'meal',meal,'store',store,'enough',False,enough
        return False
    else:
        print 'meal',meal,'store',store,'enough',True,enough
        return True

def check_quantities_double(meal,store,storeb):
    enough=[]
    for p in range(cntProducts):
        e=0
        if quantities[store][p]+ quantities[storeb][p] >= meals[meal][p]:
            e=1
            enough.append(e)
        else:
            break
    if len(enough) < cntProducts :
        print 'meal', meal, 'stores', store, storeb, 'enough',False,enough
        return False
    else:
        print 'meal',meal,'stores',store, storeb, 'enough',True,enough
        return True

def calculate_cost_single(meal,store):
    cost=0
    for p in range(cntProducts):
        print 'cost', meals[meal][p] ,'x', costs[store][p],'=', meals[meal][p] * costs[store][p]
        cost = cost + meals[meal][p] * costs[store][p]
    return cost

def calculate_cost_double(meal,store,storeb):
    cost=0
    print 'meal', meals[meal], 'store', quantities[store], costs[store], 'storeb', quantities[storeb], costs[storeb]
    for p in range(cntProducts):
        print 'needs', meals[meal][p], 'of', p, 'storea', quantities[store][p],'@', costs[store][p],'storeb', quantities[storeb][p],'@', costs[storeb][p]
        if costs[store][p] <= costs[storeb][p]:
            if  quantities[store][p] >= meals[meal][p]:
                print 'cost', meals[meal][p] ,'x', costs[store][p],'=', meals[meal][p] * costs[store][p]
                cost = cost + meals[meal][p] * costs[store][p]
            else:
                print 'cost', quantities[store][p] ,'x', costs[store][p],'=', quantities[store][p] * costs[store][p]
                print '++++', meals[meal][p]-quantities[store][p] ,'x', costs[storeb][p],'=', (meals[meal][p]-quantities[store][p]) * costs[storeb][p]
                cost = cost + quantities[store][p] * costs[store][p]
                cost = cost + (meals[meal][p]-quantities[store][p]) * costs[storeb][p]
        else:
            if  quantities[storeb][p] >= meals[meal][p]:
                print 'cost', meals[meal][p] ,'x', costs[storeb][p],'=', meals[meal][p] * costs[storeb][p]
                cost = cost + meals[meal][p] * costs[storeb][p]
            else:
                print 'cost', quantities[storeb][p] ,'x', costs[storeb][p],'=', quantities[storeb][p] * costs[storeb][p]
                print '++++', meals[meal][p]-quantities[storeb][p] ,'x', costs[store][p],'=', (meals[meal][p]-quantities[storeb][p]) * costs[store][p]
                cost = cost + quantities[storeb][p] * costs[storeb][p]
                cost = cost + (meals[meal][p]-quantities[storeb][p]) * costs[store][p]
    return cost
print "============calculating mealcosts"
mealcosts=[]    
for m in range(len(meals)):
    choices=[]
    min_of_choices=0
    print '---------meal', m, meals[m]
    for s in range(len(quantities)):
        print '---single', s
        if check_quantities_single(m,s):
            choices.append(calculate_cost_single(m,s))
            min_of_choices=min(choices)
            print m, s, 'x', choices, 'min', min_of_choices
        for ss in range(s+1, len(quantities)):
            print '---pair', s,'and', ss 
            if check_quantities_double(m,s,ss):
                choices.append(calculate_cost_double(m,s,ss))
                min_of_choices=min(choices)
                print m, s, ss, choices, 'min', min_of_choices
    print "meal",meals[m],'min_cost',min_of_choices
    mealcosts.append(min(choices))
print '============mealcosts',mealcosts