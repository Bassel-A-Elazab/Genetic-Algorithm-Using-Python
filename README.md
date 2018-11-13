# Genetic-Algorithm-Using-Python

# Introduction
  * A genetic algorithm is a heuristic search method used in artificial intelligence and computing. <br/>
  * Algorithm is started with a set of solutions (represented by chromosomes) called <b>population</b>. <br/>
  * Solutions from one population are taken and used to form a new population.<br/> 
  * This is motivated by a hope, that the new population will be better than the old one.<br/>
  * Solutions which are <b>selected</b> to form new solutions (offspring) are selected according to their fitness the more suitable they are the more chances they have to reproduce. 
  
  # Instructions
   * There are many steps to solve problem i explain it in details but there are 3 main steps such that :- <br/>
     * Selection Operator. <br/>
     * Crossover Operator. <br/>
     * Mutation Operator. <br/>
   * and steps in details :- <br/>
    1.<b> [Start] </b> Generate random <b>population</b> of n chromosomes (suitable solutions for the problem) <br/>
    2.<b> [Fitness] </b> Evaluate the <b>fitness</b> f(x) of each chromosome x in the <b>population</b>.<br/>
    3.<b> [New population] </b> Create a new <b>population </b>by repeating following steps until the <b>new population</b> is complete. <br>
    4.<b> [Selection] </b> Select two parent chromosomes from a <b>population </b> according to their <b>fitness</b> (the better fitness, the bigger chance to be selected).<br/>
    5.<b> [Crossover] </b> With a <b>crossover</b> probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents. </br>
    6.<b> [Mutation] </b> With a <b>mutation </b>probability mutate new offspring at each locus (position in chromosome).<br/>
    7.<b> [Accepting] </b> Place new offspring in a new <b>population.</br> 
    8.<b> [Replace] </b> Use new generated <b>population</b> for a further run of algorithm.<br/>
    9.<b> [Test] </b> If the end condition is satisfied, stop, and return the best solution in current <b>population.</b><br/>
    10.<b> [Loop] </b> Go to <b>["step 2"]</b><br/> 
    
 # Requirements 
 Install Python 2.7 <br/>
 Install Numpy <br/>
 
  
  
