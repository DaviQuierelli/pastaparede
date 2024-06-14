from django.shortcuts import render
def index(request):
    aredeparede=float; aparede=''; lparede=''; atijolo=''; ltijolo=''
    if request.method == 'POST':
        aparede = request.POST['aparede']
        lparede = request.POST['lparede']
        atijolo = request.POST['atijolo']
        ltijolo = request.POST['ltijolo']
        if aparede=='' or lparede=='' or atijolo=='' or ltijolo=='':
            return render(request, 'index.html', {'error': 'Preencha todos os campos!'})
        aparede=aparede.replace(',','.')
        lparede=lparede.replace(',','.')
        atijolo=atijolo.replace(',','.')
        ltijolo=ltijolo.replace(',','.')
        areaparede=float(aparede)*float(lparede)
        areatijolo=float(atijolo)*float(ltijolo)
        qtde=round(areaparede/areatijolo)
        lista=[]
        for i in range(0,qtde):
            lista.append(i)
        return render(request,'index.html',{'qtde':qtde, 'lista':lista})
    return render(request,'index.html')

