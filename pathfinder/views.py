from django.shortcuts import render
from django.http import HttpResponse
from pathfinder.backend import *
from pathfinder.subway import *
from pathfinder.subway2 import *
from .models import path


def HomePageView(request):
    if request.method == 'POST':
        
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
            # Find shortest path and its cost between stations
        fpath, cost = subway2.shortest_path(str(origin), str(destination))

        list1 = []
        lines = []
        for station in fpath:
            if station.name[-1] == '1' or station.name[-1] == '2':
                station.name = station.name[:-1]
                list1.append(station)
            else:
                list1.append(station)
                
        for index, station in enumerate(list1):
            if index == 0 and list1[0].name != list1[1].name:
                lines.append(list1[index+1].lines[0])
            elif index < len(list1)-2 and list1[index].name == list1[index+1].name:
                lines.append(list1[index+1].lines[0])
                cost -= 1000
                cost += 8
            
        
        if list1[0].name == list1[1].name:
            list1.pop(0)
        if list1[-1-1].name == list1[-1].name:
            list1.pop(-1)
            cost -= 1000
            cost += 8
        
        stops = []

        for station in list1:
            stops.append(Stop(station.name, station.lines[0]))

        # current_line = ''
        # linechange_penalty = 8
        # stops = []
        # lines = []

        # #checking line change method
        # def lineChange(a, b):
        #     a_set = set(a)
        #     b_set = set(b)
        #     if (a_set & b_set):
        #         return False
        #     else:
        #         return True

        # for index, station in enumerate(fpath):
        #     #checking if we are entering a station
        #     if index == 0:
        #         current_line = list(set(fpath[index].lines).intersection(fpath[index+1].lines))[0]
        #         stops.append(Stop(station.name, current_line))
        #         lines.append(current_line)
        #     #checking if we are changing lines
        #     elif index != len(fpath)-1 and lineChange(fpath[index-1].lines, fpath[index+1].lines):
        #         cost += linechange_penalty
        #         stops.append(Stop(station.name, current_line))
        #         current_line = list(set(fpath[index].lines).intersection(fpath[index+1].lines))[0]
        #         lines.append(current_line)
        #         stops.append(Stop(station.name, current_line))
        #     #then we are just on our way
        #     else:
        #         stops.append(Stop(station.name, current_line))
    
    
    
        context = {
            'stops': stops,
            'cost': cost,
            'lines': lines
        }
        return render(request, 'result.html', context)
        

    return render(request, 'home.html')




