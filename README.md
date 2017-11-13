
# HPCTwitterGeoProcessing

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

We have a huge dataset to process which can't be processed by our personal laptop's CPU (it'll
take days to process). So that's why we are using spartan for that. Spartan is hybrid computing
facilities with various cores at physical partition and over 400 virtual machines with over
3,000 cores at cloud partition. (See below Picture)

<img src="https://github.com/jigar007/HPCTwitterGeoProcessing/blob/master/spartan.jpg">

the result is shown on the map. Analysis shown that near you go to CBD you more number of
tweets are from there. (See below Picture)

<img src="https://github.com/jigar007/HPCTwitterGeoProcessing/blob/master/map.png">

Most of the time taken by the total process is for pre-processing data this includes reading
from a file and catching location from each tweet and making a list of locations.Average
actual processing time is around 8 seconds. In 8 seconds program finds from geo-location list
that from which one of 16 box that location is from. (See below Picture)

<img src="https://github.com/jigar007/HPCTwitterGeoProcessing/blob/master/graph.png">
