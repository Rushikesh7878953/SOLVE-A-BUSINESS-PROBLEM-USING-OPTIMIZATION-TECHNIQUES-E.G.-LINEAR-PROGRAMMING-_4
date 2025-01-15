# Import pulp
import pulp
# Step 1. Define The Linear Program Problem
# For Maximize The Profit,So We Use LpMaximize
prob=pulp.LpProblem("Production Optimization",pulp.LpMaximize)

# Step 2. Define Decision Variables
# x_A And x_B Represent The Number Of Units Of Product A And Product B to Produce
x_A = pulp.LpVariable("x_A",lowBound=0,cat='Continuous') # Non-negative,Continuous Variable
x_B = pulp.LpVariable("x_B",lowBound=0,cat='Continuous') # Non-negative,Continuous Variable

# Step 3. Define The Objective Function (For Maximize Profit)
prob+=40*x_A+30*x_B,"Total Profit"

# Stpe 4. Define The Constraints
# Labor Hours Constraint (5 * x_A + 3 * x_B <= 150)
prob+=5*x_A+3*x_B<=150,"Labor Hours"

# Material Constraint (2 * x_A + 3 * x_B <= 180)
prob+=2*x_A+3*x_B<=180,"Material"

# Stpe 5. Solve The Problem
prob.solve()

# Stpe 6. Output The Results
if pulp.LpStatus[prob.status] == 'Optimal':
    print(f"Optimal number of Product A to produce: {x_A.varValue} units")
    print(f"Optimal number of Product B to produce: {x_B.varValue} units")
    print(f"Total Profit: ${pulp.value(prob.objective)}")
else:
    print("No optimal solution found")