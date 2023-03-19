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
            # Find shortest path and its cost between stations
            stops, lines, cost = calculate(str(origin), str(destination))

            s1, l1 ,cost1 = calculate('تجریش', 'کهریزک')
            s1w, l1w, cost2 = calculate('شاهد', 'فرودگاه امام خمینی')
            s2, l2, cost3 = calculate('فرهنگسرا', 'تهران (صادقیه)')
            s3, l3, cost4 = calculate('قائم', 'آزادگان')
            s4, l4, cost5 = calculate('شهید کلاهدوز', 'ارم سبز')
            s4s, l4s, cost6 = calculate('بیمه', 'پایانه 4و6 فرودگاه مهرآباد')
            s5, l5, cost7 = calculate('تهران (صادقیه)', 'گلشهر')
            s5w, l5w, cost8 = calculate('گلشهر', 'شهید سپهبد سلیمانی')
            s6e, l6e, cost9 = calculate('دولت آباد', 'امام حسین')
            s6w, l6w, cost10 = calculate('دانشگاه تربیت مدرس', 'شهید ستاری')
            s7, l7, cost11 = calculate('بسیج', 'میدان صنعت')
            
            lines2 = []
            for line in lines:
                if line == 'l1':
                    lines2.append(Line(line,'خط 1 - (تجریش - کهریزک)'))
                elif line == 'l1w':
                    lines2.append(Line(line,'توسعه غربی خط 1'))
                elif line == 'l2':
                    lines2.append(Line(line,'خط 2 - (فرهنگسرا - صادقیه)'))
                elif line == 'l3':
                    lines2.append(Line(line,'خط 3 - (قائم - آزادگان)'))
                elif line == 'l4':
                    lines2.append(Line(line,'خط 4 - (شهید کلاهدوز - ارم سبز)'))
                elif line == 'l4s':
                    lines2.append(Line(line,'توسعه جنوبی خط 4'))
                elif line == 'l5':
                    lines2.append(Line(line,'خط 5 - (ارم سبز - گلشهر)'))
                elif line == 'l5w':
                    lines2.append(Line(line,'توسعه غربی خط 5'))
                elif line == 'l6e':
                    lines2.append(Line(line,'خط 6 - (امام حسین - دولت آباد)'))
                elif line == 'l6w':
                    lines2.append(Line(line,'خط 6 - (تربیت مدرس - شهید ستاری)'))
                elif line == 'l7':
                    lines2.append(Line(line,'خط 7 - (بسیج - میدان صنعت)'))
            error = 'hidden=True'

            if cost > 60:
                costdesc = str('{h} ساعت و {m} دقیقه'.format(h=int(cost/60), m=cost%60))
                cost = str('{h}:{m:02d}'.format(h=int(cost/60), m=cost%60))
            else:
                costdesc = str('{m} دقیقه'.format(m=int(cost)))
                cost = str('00:{m:02d}'.format(m=int(cost)))
            context = {
                'stops': stops,
                'cost': cost,
                'lines': lines2,
                'error': error,
                'costdesc': costdesc,
                
            }
            return render(request, 'result.html', context)

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
        
        

    options = subway.stations

    error = 'hidden=True'

    context = {
        'options': options,
        'error': error,

    }
    return render(request, 'home.html', context)




