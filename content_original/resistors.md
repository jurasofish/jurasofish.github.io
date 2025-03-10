Title: Picking Resistors for Parallel and Series Equivalence
Date: 2021-02-07 12:17

I came across an [interesting question](https://stackoverflow.com/questions/65912561/python-algorithm-to-approximate-closest-parallel-equivalence-of-resistors-from-a) on stack overflow that I couldn't help [answering](https://stackoverflow.com/a/65915378/8899565). 
The question asks how to determine which resistors from a given pool have an equivalent parallel resistance as close as possible to some target.
This jumped out at me as a fun little combinatorial problem to tackle with integer programming.

A few google searches didn't turn up any existing work, but it's a tricky one to google because the wording is so similar to asking which (single) resistor value to pick for some task. 

I chose to use the [python-mip](https://github.com/coin-or/python-mip) library
as it's quite clean to use and easy to install.

All this code is available [on github](https://github.com/jurasofish/resistors).


### In series

To start with, I implemented a program to pick the resistors in series.

The resistors are picked by setting a binary variable on or off for each resistor in the $\text{r_in_use}$ list. 
For example, if $\text{resistors} = [R_1, R_2, R_3, R_4, ...]$ and the solution finds that $ \text{r_in_use} = [0, 1, 1, 0, ...]$
then the solution for the final resistance is $R_2 + R_3$.

For the objective function, I want to minimise the difference between the
solution resistance and the target resistance - that is, I want to minimise the
absolute value of the error. To do this a minimax method is used: a value 
greater than the absolute error is created, and then that value is
minimised in the objective function - thus minimising the absolute error.
The absolute error could be calculated exactly by using some more integer
constraints, but minimax is sufficient in this case.


    :::python
    import mip
    from typing import List
    
    
    def equivalent_series(resistors: List[float], target: float) -> List[float]:
        """Return list of resistors which in series are closest to target resistance.
    
        Args:
            resistors: float values of the resistors to choose from. A resistor
                value can be used as many times as it occurs in this list.
            target: The target resistance.
    
        Returns:
            Optimal resistor values.
        """
        m = mip.Model()  # Create new mixed integer/linear model.
    
        # Will take value of 1 when corresponding resistor is in use, otherwise 0.
        r_in_use = [m.add_var(var_type=mip.BINARY) for _ in resistors]
        opt_r = sum([b * r for b, r in zip(r_in_use, resistors)])  # Optimal resistance
        error = opt_r - target  # Want to minimise the absolute value of this error.
    
        # create a variable which is greater than than the absolute value of the error.
        # Because we will be minimizing, this will be forced down to equal the
        # absolute value. Common trick, google "linear programming absolute value".
        abs_error = m.add_var(lb=0)
        m += abs_error >= error
        m += abs_error >= -1 * error
    
        # Objective of the optimisation is to minimise the absolute error.
        m.objective = mip.minimize(abs_error)
        m.verbose = False  # Turn off verbose logging output.
        sol_status = m.optimize()
        assert sol_status == mip.OptimizationStatus.OPTIMAL
    
        # Get the solution values telling us which resistors are in use.
        r_in_use_sol = [float(v) for v in r_in_use]
    
        # Pick out the values of the resistors corresponding to the resistors
        # that the optimiser decided to use.
        r_to_use = [r for r, i in zip(resistors, r_in_use_sol) if i > 0]
    
        solved_resistance = sum(x for x in r_to_use)
        solved_error = 100 * (solved_resistance - target) / target
        print(f'Resistors {r_to_use} in series '
              f'will produce R={solved_resistance:.3f}. Aiming for R={target:.3f}, '
              f'error of {solved_error:.2f}%')
        return r_to_use
    
    
    sol = equivalent_series([1, 2, 3, 4, 5, 6, 7], 11)
    sol = equivalent_series([1, 2, 3, 4, 5, 6, 7], 15.6)
    sol = equivalent_series(list(range(1, 100)), 1056)


```text
Resistors [1, 2, 3, 5] in series will produce R=11.000. Aiming for R=11.000, error of 0.00%
Resistors [1, 2, 3, 4, 6] in series will produce R=16.000. Aiming for R=15.600, error of 2.56%
Resistors [1, 7, 8, 13, 16, 19, 21, 23, 24, 25, 26, 28, 30, 31, 32, 34, 35, 43, 44, 45, 55, 60, 62, 66, 73, 74, 76, 85] in series will produce R=1056.000. Aiming for R=1056.000, error of 0.00%
```


### Extending to work with in parallel

To make this work with parallel resistors requires only a small change.
I simply change the target and the individual resistor values to be
their reciprocals.


    :::python hl_lines="17 18 47 48"
    import mip
    from typing import List
    
    
    def equivalent(resistors: List[float], target: float, series: bool) -> List[float]:
        """Return list of resistors which in series/parallel are closest to target resistance.
    
        Args:
            resistors: float values of the resistors to choose from. A resistor
                value can be used as many times as it occurs in this list.
            target: The target resistance.
            series: True for series, false for parallel.
    
        Returns:
            Optimal resistor values.
        """
        _target = target if series else 1/target
        _resistors = resistors if series else [1/x for x in resistors]
    
        m = mip.Model()  # Create new mixed integer/linear model.
    
        # Will take value of 1 when corresponding resistor is in use, otherwise 0.
        r_in_use = [m.add_var(var_type=mip.BINARY) for _ in _resistors]
        opt_r = sum([b * r for b, r in zip(r_in_use, _resistors)])  # Optimal resistance
        error = opt_r - _target  # Want to minimise the absolute value of this error.
    
        # create a variable which is greater than than the absolute value of the error.
        # Because we will be minimizing, this will be forced down to equal the
        # absolute value. Common trick, google "linear programming absolute value".
        abs_error = m.add_var(lb=0)
        m += abs_error >= error
        m += abs_error >= -1 * error
    
        # Objective of the optimisation is to minimise the absolute error.
        m.objective = mip.minimize(abs_error)
        m.verbose = False  # Turn off verbose logging output.
        sol_status = m.optimize()
        assert sol_status == mip.OptimizationStatus.OPTIMAL
    
        # Get the solution values telling us which resistors are in use.
        r_in_use_sol = [float(v) for v in r_in_use]
    
        # Pick out the values of the resistors corresponding to the resistors
        # that the optimiser decided to use.
        r_to_use = [r for r, i in zip(resistors, r_in_use_sol) if i > 0]
    
        solved_resistance = sum(x for x in r_to_use) if series \
            else 1/sum(1/x for x in r_to_use)
        solved_error = 100 * (solved_resistance - target) / target
        print(f'Resistors {r_to_use} in {"series" if series else "parallel"} '
              f'will produce R={solved_resistance:.3f}. Aiming for R={target:.3f}, '
              f'error of {solved_error:.2f}%')
        return r_to_use
    
    
    sol = equivalent([1, 2, 3, 4, 5, 6, 7], 11, True)
    sol = equivalent([1, 2, 3, 4, 5, 6, 7], 15.6, True)
    sol = equivalent(list(range(1, 100)), 1056, True)
    
    sol = equivalent([1, 2, 3, 4, 5, 6, 7], 1.5555, False)
    sol = equivalent([1, 2, 3, 4, 5, 6, 7], 1.9, False)
    sol = equivalent(list(range(1, 100)), 123, False)


```text
Resistors [1, 2, 3, 5] in series will produce R=11.000. Aiming for R=11.000, error of 0.00%
Resistors [1, 2, 3, 4, 6] in series will produce R=16.000. Aiming for R=15.600, error of 2.56%
Resistors [1, 7, 8, 13, 16, 19, 21, 23, 24, 25, 26, 28, 30, 31, 32, 34, 35, 43, 44, 45, 55, 60, 62, 66, 73, 74, 76, 85] in series will produce R=1056.000. Aiming for R=1056.000, error of 0.00%
Resistors [2, 7] in parallel will produce R=1.556. Aiming for R=1.556, error of 0.00%
Resistors [3, 5] in parallel will produce R=1.875. Aiming for R=1.900, error of -1.32%
Resistors [99] in parallel will produce R=99.000. Aiming for R=123.000, error of -19.51%
```

### Picking the least number of resistors to satisfy a tolerance

Minimising the error is all well and good, but in reality you probably
want to pick the least number of resistors to satisfy some tolerance.
(It also turns out this is the question that the person on stack overflow meant
to ask).

To do this I simply constrain the error to be within some lower and upper
bound, and then minimise the sum of $ \text{r_in_use}$ (each in-use resistor
is indicated by a value of 1, so this minimises number of resistors).

Currently, if there are multiple solutions which are both within the tolerance
and have the same number of resistors then it will arbitrarily pick one as the
solution with no regard for which is better. You could add a small term (<1.0)
to the objective to incorporate the error.


    :::python hl_lines="31 32 35"
    import mip
    from typing import List
    
    
    def equivalent_tol(
            resistors: List[float], target: float, series: bool, tol: float
    ) -> List[float]:
        """Return list of resistors which in series/parallel are within tolerance
         of the target resistance, minimising the number of resistors in use.
    
        Args:
            resistors: float values of the resistors to choose from. A resistor
                value can be used as many times as it occurs in this list.
            target: The target resistance.
            series: True for series, false for parallel.
            tol: Solved resistance will be in range [(1-tol)*target, (1+tol)*target]
    
        Returns:
            Optimal resistor values, or empty list if no solution.
        """
        _target = target if series else 1/target
        _resistors = resistors if series else [1/x for x in resistors]
        lower = (1-tol) * target if series else 1/((1+tol) * target)
        upper = (1+tol) * target if series else 1/((1-tol) * target)
    
        m = mip.Model()  # Create new mixed integer/linear model.
    
        # Will take value of 1 when corresponding resistor is in use, otherwise 0.
        r_in_use = [m.add_var(var_type=mip.BINARY) for _ in _resistors]
        opt_r = sum([b * r for b, r in zip(r_in_use, _resistors)])  # Optimal resistance
        m += opt_r >= lower
        m += opt_r <= upper
    
        # Objective of the optimisation is to minimise the number of resistors.
        m.objective = mip.minimize(mip.xsum(r_in_use))
        m.verbose = False  # Turn off verbose logging output.
        sol_status = m.optimize()
        if sol_status != mip.OptimizationStatus.OPTIMAL:
            print(f'No solution found')
            return []
    
        # Get the solution values telling us which resistors are in use.
        r_in_use_sol = [float(v) for v in r_in_use]
    
        # Pick out the values of the resistors corresponding to the resistors
        # that the optimiser decided to use.
        r_to_use = [r for r, i in zip(resistors, r_in_use_sol) if i > 0]
    
        solved_resistance = sum(x for x in r_to_use) if series \
            else 1/sum(1/x for x in r_to_use)
        solved_error = 100 * (solved_resistance - target) / target
        print(f'Resistors {r_to_use} in {"series" if series else "parallel"} '
              f'will produce R={solved_resistance:.3f}. Aiming for R={target:.3f}, '
              f'error of {solved_error:.2f}%')
        return r_to_use
    
    
    sol = equivalent_tol([1, 2, 3, 4, 5, 6, 7], 11, True, 0.1)
    sol = equivalent_tol([1, 2, 3, 4, 5, 6, 7], 15.6, True, 0.1)
    sol = equivalent_tol(list(range(1, 100)), 1056, True, 0.1)
    
    sol = equivalent_tol([1, 2, 3, 4, 5, 6, 7], 1.5555, False, 0.1)
    sol = equivalent_tol([1, 2, 3, 4, 5, 6, 7], 1.9, False, 0.1)
    sol = equivalent_tol(list(range(1, 100)), 123, False, 0.1)


```text
Resistors [5, 6] in series will produce R=11.000. Aiming for R=11.000, error of 0.00%
Resistors [4, 5, 6] in series will produce R=15.000. Aiming for R=15.600, error of -3.85%
Resistors [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] in series will produce R=1034.000. Aiming for R=1056.000, error of -2.08%
Resistors [2, 5] in parallel will produce R=1.429. Aiming for R=1.556, error of -8.16%
Resistors [2] in parallel will produce R=2.000. Aiming for R=1.900, error of 5.26%
No solution found
```


### Stress Testing

How many possible resistor values can I feed it, and how long will it take to solve?
The following, with ten thousand resistors, runs in about one second on my computer.

    :::python
    sol = equivalent([x/100 for x in range(1, 10_000)], 5.26591, False)

```text
Resistors [28.59, 61.6, 88.54, 89.88, 92.31, 92.75, 93.11, 93.12, 93.6, 94.08, 94.25, 94.45, 95.69, 98.61, 98.74] in parallel will produce R=5.264. Aiming for R=5.266, error of -0.03%
```

