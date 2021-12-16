My iterated version of the popular "Prisoner's Dilemma" is a project that, via game theory, demonstrates why “rational” individuals are unlikely to cooperate, even when it could be in both of their best interests to do so, a win-win scenario. It provides simple tools to test out the many possibilities when it comes to simulating the outcome of multiple "classes", or decision algorhythms. In this particular version the "objective" for any given class is to achieve the highest amount of collective points, which in turn convert into instances of that class. The most populated class at the end of the simulation is shown to be the most fit for such a dillema. 

The setup is fairly easy, allowing the selection of up to two different behavioral algorhythms from the pool below:
1.) "Saint" - An algorhythm that always decides to cooperate.
2.) "Traitor" - The opposite of the Saint, an algorhythm that always betrays.
3.) "Good" - A weaker-willed version of the Saint, cooperating 3/4 of the time.
4.) "Bad" - A weaker-willed version of the Traitor, betraying 3/4 of the time.
5.) "TFT" - An algorhythm based of the "Tit-For-Tat" strategy, betraying once betrayed, with the chance of redemption if cooperated with.
6.) "TF2T" - A slowpoke version of the TFT, doing the same, but needing 2 consecutive betrayals in order to start betraying the traitors.
7.) "Amnesiac" - An algorhythm deciding completely randomly.
8.) "Big-Dog" - A complex algorhythm when it comes to deciding. If betrayed whilst cooperating, betrays the traitor next round. If betrayed whilst betraying, offers a peaceful resolution via cooperation. If betraying a cooperating unit, it will continue to betray. Will always start off by cooperating.
9.) "Small-Dog" - Identical in every way to Big-Dog except for starting off with betraying.

The simulation also offers a chance of a "Mishap" happening. This chance will directly impact the chance of any given decision to be inverted (i.e. "cooperation" turns to "betrayal".). If the "Mishap" window is left blank, the feature will simply not affect anything at all.
