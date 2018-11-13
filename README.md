# Genetic-Algorithm-Using-Python

# Introduction
  * A genetic algorithm is a heuristic search method used in artificial intelligence and computing. <br/>
  * Algorithm is started with a set of solutions (represented by chromosomes) called <b>population</b>. <br/>
  * Solutions from one population are taken and used to form a new population.<br/> 
  * This is motivated by a hope, that the new population will be better than the old one.<br/>
  * Solutions which are <b>selected</b> to form new solutions (offspring) are selected according to their fitness the more suitable they are the more chances they have to reproduce. 
  
  # Instructions
   * There are many steps to solve problem :- <br/>
    1. <b> [Start] </b> Generate random <b>population</b> of n chromosomes (suitable solutions for the problem) <br/>
    2. <b> [Fitness] </b> Evaluate the <b>fitness</b> f(x) of each chromosome x in the <b>population</b>.<br/>
    3. <b>[New population] </b> Create a new <b>population </b>by repeating following steps until the <b>new population</b> is complete. <br>
    4. <b>[Selection] </b> Select two parent chromosomes from a <b>population </b> according to their <b>fitness</b> (the better fitness, the bigger chance to be selected).<br/>
        [Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
        [Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).
        [Accepting] Place new offspring in a new population 
    [Replace] Use new generated population for a further run of algorithm
    [Test] If the end condition is satisfied, stop, and return the best solution in current population
    [Loop] Go to step 2 
  
  
