# I want to provide change of 34$, How can we provide it with maximum number of notes possible?
# --> We have a note of 20$, 10$, 5$ and 2$ in our wallet.
# --> Choosing the 20$ note first was the best solution at that point, as it was the closest one to 34$.
# --> Choosing the 10$ note next was the best solution at that point, as it was the closest one to remaining 14$.
# --> Choosing 2 notes of 2$ next was the best solution at that point, as it was the closest one to remaining 4$.
# --> The technique we have just used in the change making game is known as the Greedy approach.

# Let's see one more example of Greedy Aproach.
'''
--> I have to visit 25 places today and get back to the starting place. 
--> How do I find the shortest possible route?

--> 25 places will have 24 factorial ( 24! = 620448401733239439360000) routes.
--> Why? Because permutations of n distinct objects is n factorial.

--> How big is 24! ?
--> If 24! (= 6.204484017332394 x 1023 ) grains of sand are put into a ball, it would have a radius of 2.6459548720674647 x 10+1 Kilometers !

--> Instead of picking the best route from 24! routes, we can travel by choosing the next closest city from the current city.  
--> We can keep doing this until all the cities have been visited.
--> This is the "Greedy approach" for solving a problem.


--> One of the world’s largest package delivery company found out that their drivers were waiting idle at intersections to make left turns.
--> They decided to re-route all their vehicles by minimizing left turns.
--> This re-routing helped them eliminate 464,000 miles (747,000 km) from its travel and save 51,000 US gallons (190,000 l) of fuel!!!
--> UPS became more efficient by using a variation of Traveling Salesman algorithm.
'''