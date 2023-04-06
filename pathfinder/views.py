from django.shortcuts import render
from django.http import HttpResponse
from pathfinder.backend import *
from pathfinder.subway import *
from pathfinder.subway2 import *
from pathfinder.subway3 import *

# def PageNotFoundView(request):
#     return render(request, '404.html')

# def ServerErrorView(request):
#     return render(request, '500.html')

def StationsView(request):
    return render(request, 'stations.html')

def MapView(request):
    return render(request, 'map.html')

def ReportView(request):
    return render(request, 'report.html')

def HomePageView(request):
    if request.method == 'POST':
        
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        pathtype = request.POST.get('path')
        #input validation
        stlist = []
        for obj in subway.stations:
            stlist.append(str(obj))
        ortest = origin in stlist
        destest = destination in stlist
        if origin == destination or destest == False or ortest == False:
            error = ''
            options = subway.stations

            context = {
                'error': error,
                'options': options
            }
            return render(request, 'home.html', context)
        else:
            # Find path and its cost between stations
            # stops, lines, cost = calculate(str(origin), str(destination))
            if pathtype == 'on':
                stops, lines, cost = calculate_leastchange(str(origin), str(destination))
            else:
                stops, lines, cost = calculate(str(origin), str(destination))


            s1, l1 ,cost1 = calculate('تجریش', 'کهریزک')
            s1w, l1w, cost2 = calculate('شاهد', 'فرودگاه امام خمینی')
            s2, l2, cost3 = calculate('فرهنگسرا', 'تهران (صادقیه)')
            s3, l3, cost4 = calculate('قائم', 'آزادگان')
            s4, l4, cost5 = calculate('شهید کلاهدوز', 'ارم سبز')
            s4s, l4s, cost6 = calculate('بیمه', 'پایانه 4و6 فرودگاه مهرآباد')
            s5, l5, cost7 = calculate('تهران (صادقیه)', 'گلشهر')
            s5w, l5w, cost8 = calculate('گلشهر', 'شهید سپهبد سلیمانی')
            s6, l6, cost9 = calculate('دولت آباد', 'شهید ستاری')
            
            s7, l7, cost11 = calculate('بسیج', 'شهید دادمان')
            
            lines2 = []
            
            for line in lines:
                if line == 'l1':
                    i = stops.index(next(station for station in stops if station.line == 'l1'))
                    j = s1.index(next(station for station in s1 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s1[j+1].name:
                            lines2.append(Line('l1','خط 1 - به سمت کهریزک'))
                        else:
                            lines2.append(Line('l1','خط 1 - به سمت تجریش'))
                    except:
                        lines2.append(Line('l1','خط 1 - به سمت تجریش'))


                elif line == 'l1w':
                    i = stops.index(next(station for station in stops if station.line == 'l1w'))
                    j = s1w.index(next(station for station in s1w if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s1w[j+1].name:
                            lines2.append(Line('l1w','خط 1 - به سمت فرودگاه امام خمینی'))
                        else:
                            lines2.append(Line('l1w','خط 1 - به سمت شاهد'))
                    except:
                        lines2.append(Line('l1w','خط 1 - به سمت شاهد'))

                elif line == 'l2':
                    i = stops.index(next(station for station in stops if station.line == 'l2'))
                    j = s2.index(next(station for station in s2 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s2[j+1].name:
                            lines2.append(Line('l2','خط 2 - به سمت صادقیه'))
                        else:
                            lines2.append(Line('l2','خط 2 - به سمت فرهنگسرا'))
                    except:
                        lines2.append(Line('l2','خط 2 - به سمت فرهنگسرا'))

                elif line == 'l3':
                    i = stops.index(next(station for station in stops if station.line == 'l3'))
                    j = s3.index(next(station for station in s3 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s3[j+1].name:
                            lines2.append(Line('l3','خط 3 - به سمت آزادگان'))
                        else:
                            lines2.append(Line('l3','خط 3 - به سمت قائم'))
                    except:
                        lines2.append(Line('l3','خط 3 - به سمت قائم'))

                elif line == 'l4':
                    i = stops.index(next(station for station in stops if station.line == 'l4'))
                    j = s4.index(next(station for station in s4 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s4[j+1].name:
                            lines2.append(Line('l4','خط 4 - به سمت ارم سبز'))
                        else:
                            lines2.append(Line('l4','خط 4 - به سمت شهید کلاهدوز'))
                    except:
                        lines2.append(Line('l4','خط 4 - به سمت شهید کلاهدوز'))

                elif line == 'l4s':
                    i = stops.index(next(station for station in stops if station.line == 'l4s'))
                    j = s4s.index(next(station for station in s4s if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s4s[j+1].name:
                            lines2.append(Line('l4s','خط 4 - به سمت فرودگاه مهر آباد'))
                        else:
                            lines2.append(Line('l4s','خط 4 - به سمت بیمه'))
                    except:
                        lines2.append(Line('l4s','خط 4 - به سمت بیمه'))

                elif line == 'l5':
                    i = stops.index(next(station for station in stops if station.line == 'l5'))
                    j = s5.index(next(station for station in s5 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s5[j+1].name:
                            lines2.append(Line('l5','خط 5 - به سمت گلشهر'))
                        else:
                            lines2.append(Line('l5','خط 5 - به سمت صادقیه'))
                    except:
                        lines2.append(Line('l5','خط 5 - به سمت صادقیه'))

                elif line == 'l5w':
                    i = stops.index(next(station for station in stops if station.line == 'l5w'))
                    j = s5w.index(next(station for station in s5w if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s5w[j+1].name:
                            lines2.append(Line('l5w','خط 5 - به سمت شهید سپهبد سلیمانی'))
                        else:
                            lines2.append(Line('l5w','خط 5 - به سمت گلشهر'))
                    except:
                            lines2.append(Line('l5w','خط 5 - به سمت گلشهر'))

                elif line == 'l6':
                    i = stops.index(next(station for station in stops if station.line == 'l6'))
                    j = s6.index(next(station for station in s6 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s6[j+1].name:
                            lines2.append(Line('l6','خط 6 - به سمت شهید ستاری'))
                        else:
                            lines2.append(Line('l6','خط 6 - به سمت دولت آباد'))
                    except:
                        lines2.append(Line('l6','خط 6 - به سمت دولت آباد'))

                elif line == 'l7':
                    i = stops.index(next(station for station in stops if station.line == 'l7'))
                    j = s7.index(next(station for station in s7 if station.name == stops[i].name))
                    try:
                        if stops[i+1].name == s7[j+1].name:
                            lines2.append(Line('l7','خط 7 - به سمت شهید دادمان'))
                        else:
                            lines2.append(Line('l7','خط 7 - به سمت بسیج'))
                    except:
                        lines2.append(Line('l7','خط 7 - به سمت بسیج'))

            error = 'hidden=True'

            if cost > 60:
                costdesc = str('{h} ساعت و {m} دقیقه'.format(h=int(cost/60), m=cost%60))
                cost = str('{h}:{m:02d}'.format(h=int(cost/60), m=cost%60))
            else:
                costdesc = str('{m} دقیقه'.format(m=int(cost)))
                cost = str('00:{m:02d}'.format(m=int(cost)))
            context = {
                'origin': stops[0].name,
                'destination': stops[-1].name,
                'stops': stops,
                'cost': cost,
                'lines': lines2,
                'error': error,
                'costdesc': costdesc,
                
            }
            return render(request, 'result.html', context)


    options = subway.stations

    error = 'hidden=True'

    context = {
        'options': options,
        'error': error,

    }
    return render(request, 'home.html', context)




