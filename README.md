#HPCTwitterGeoProcessing

This project is solving the problem of searching into a large dataset of twitter file geocode
using high performance (HPC) facility named Spartan, this geocode is from one of any 16
possible geographic areas or from somewhere outside. We must write a program for searching
for a number of tweets made in each box, each row, and each column. This is a very
computationally intensive task as we have around 10 GB tweet file, and for solving this we are
using HPC.

I have used python as a programming language because python provides very powerful
programming experience, also python programs are comparatively compact and easy to
understand. I have used mpi4py external package for implementing Message Passing Interface
(MPI). MPI is very powerful and widely used system for the parallel software application. In a
way, it is the de facto industry standard and it is widely available as open source
implementation.

<img src="https://github.com/jigar007/HPCTwitterGeoProcessing/blob/master/map.png">
<img src="https://github.com/jigar007/HPCTwitterGeoProcessing/blob/master/graph.png">
