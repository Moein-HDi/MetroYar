from django.shortcuts import render
from django.http import HttpResponse
from pathfinder.backend import *
from pathfinder.subway import *


def homePageView(request):

    # Find shortest path and its cost between stations
    path, cost = subway.shortest_path(station_a, station_e)
    print('Shortest path:', path)
    print('Cost:', cost)

    current_line = ''
    linechange_penalty = 8
    stops = []
    lines = []

    #checking line change method
    def lineChange(a, b):
        a_set = set(a)
        b_set = set(b)
        if (a_set & b_set):
            return False
        else:
            return True

    for index, station in enumerate(path):
        #checking if we are entering a station
        if index == 0:
            current_line = list(set(path[index].lines).intersection(path[index+1].lines))[0]
            stops.append(Stop(station.name, current_line))
            lines.append(current_line)
        #checking if we are changing lines
        elif index != len(path)-1 and lineChange(path[index-1].lines, path[index+1].lines):
            cost += linechange_penalty
            stops.append(Stop(station.name, current_line))
            current_line = list(set(path[index].lines).intersection(path[index+1].lines))[0]
            lines.append(current_line)
            stops.append(Stop(station.name, current_line))
        #then we are just on our way
        else:
            stops.append(Stop(station.name, current_line))
    
    
    
    context = {
        'cost': cost,
        'stops': stops,
        'lines': lines,
    }
    return render(request, 'home.html', context)
