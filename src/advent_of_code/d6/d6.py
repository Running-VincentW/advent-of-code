#!/usr/bin/env python
# coding: utf-8

# Let's define the distance traveled as a function to the variable $j$. The race is raced for a fixed time $T$.
# $$f(j) = j×(T−j)$$
#
# which equates to a downwards parabola
# $$f(j) = -j^2 + Tj$$
#
# To find the highest distance travelled, we find the max value of this parabola.
# The vertex of equation of form $f(x) = ax^2 + bx + c$ is found at $x = \frac{-b}{2a}$.
# So in this case, the vertex is at $x = \frac{-T}{2(-1)}$, thus $x = \frac{T}{2}$.
#
# As we are more concerened about beating the race record $r$, we need to find $f(j) > r$. We need to solve this equation.
# $$ j x (T - j) > r$$
# Let's solve this quadratic equation.
# $$ j x (T - j) - r> 0$$
# $$ j^2 - Tj + r < 0$$
#
# The roots of the equation are.
# $$ j = \frac{-(-T) \pm \sqrt{T^2 - 4(1)(r)}}{2(1)}$$
# $$ j = \frac{T \pm \sqrt{T^2 - 4r}}{2}$$
#
# If $T^2 - 4r <0$, There are no solutions.
# If $T^2 - 4r = 0$ There's exactly one solution.
# If $T^2 - 4r > 0$, There's two solutions
#
# Assume there are two solutions, since we are solving for $f(j)$ above $r$. We consider the range within the two solutions as valid solution.
#
# We also need to take integer values as solutions only for $j$, as we are holding the button for $j$ complete seconds.

# In[4]:

import timeit
import math

input = """Time:        34     90     89     86
Distance:   204   1713   1210   1780"""
# In[5]:
part_2 = True
if part_2:
    new_input = "\n".join(x.replace(" ", "") for x in input.splitlines())
    input = new_input

# In[6]:


def calculate_j(T, r):
    """Solving for soltuions for j such that
    j x (T - j) > r
    """
    discriminant = T**2 - 4 * r

    if discriminant < 0:
        return []  # No real roots within the range
    elif discriminant == 0:
        j = (T + math.sqrt(discriminant)) / 2
        return [j]  # Exactly one solution
    else:
        j1 = (T + math.sqrt(discriminant)) / 2
        j2 = (T - math.sqrt(discriminant)) / 2
        return [j1, j2]  # Two solutions


# In[7]:


race_time, record = input.splitlines()
ts = list(map(int, race_time.split(":")[1].split()))
rs = list(map(int, record.split(":")[1].split()))


def get_range(n: float, lower=True) -> int:
    if lower:
        nr = math.ceil(n)
        if nr == n:
            return nr + 1
    else:
        nr = math.floor(n)
        if nr == n:
            return nr - 1
    return nr


def solution():
    for t, r in zip(ts, rs):
        js = sorted(calculate_j(t, r))
        solution = get_range(js[1], lower=False) - get_range(js[0]) + 1
        print(f"{solution}")


runtime = timeit.timeit(solution, number=10000) / 10000
print(f"{runtime=}")


# In[8]:


def solution_2():
    for t, r in zip(ts, rs):
        solution = 0
        for j in range(1, t):
            if j * (t - j) > r:
                solution += 1
        print(f"{solution}")


runtime = timeit.timeit(solution_2, number=10) / 10
print(f"{runtime=}")

# %%
