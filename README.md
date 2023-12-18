# Visualizing car sharing trips in Turin
The data used in this project comes from
[Mendeley Data](https://data.mendeley.com/datasets/drtn5499j2/1)
(Vassio, Giordano, Mellia, Cocca,
"Free Floating Electric Car Sharing Design: Data Driven Optimisation" (2019),
[link](https://doi.org/10.1016/j.pmcj.2019.02.007)).

It contains information about 2 months worth of electric car
sharing trips in the city of Turin.
For each trip, the start and end coordinates and timestamps are known.

The coordinates were projected to the
[UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)
system to calculate an estimate of the distance covered by each ride
(see the [script](https://github.com/francescolafratta/powerbi-car-sharing/blob/main/src/cleaning.py)).

## Dashboard
The following picture illustrates a dashboard that allows to learn more
about the size of this phenomenon, and when or how is it most used.

![Dashboard](https://github.com/francescolafratta/powerbi-car-sharing/blob/main/resources/dashboard.png)

### Key findings
- More than 120 thousand rides have occurred.
- The service is mostly used during workdays and less often on the weekends, especially on Sundays.
- Most rides are pretty short as they last about 20 minutes on average.
- Around 70% of rides are taken in the morning or afternoon.
## Timeline map
The following map allows to visualize the starting locations of the car rides
during the timeline of analysis. It also gives insights as to which zones of the
city tend to use the service the most.

![Timeline](https://github.com/francescolafratta/powerbi-car-sharing/blob/main/resources/timeline.gif)

Check out the [.pbix](https://github.com/francescolafratta/powerbi-car-sharing/blob/main/carsharing.pbix)
file to visualize the data yourself!