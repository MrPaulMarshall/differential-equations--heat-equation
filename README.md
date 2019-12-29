# differential-equations--heat-equation
My program solving heat equation in given area

BaseFunction is class that represents base functions (e1, e2, ..., eN) of function space V, where eI: R2 -> R.
I assume, that sought function u(x,y) is approximately linear combination of above functions.

My base functions are pyramids, which means they have 4 faces in their domain and are 0 elsewhere.
Faces are represented by Brach class.

After doing some math it turns out, that I can get vector of coefficients by solving a linear equations system, where matrix is obtained by calculating specific integrals.

At the end I draw graph of my solution, using matplotlib.