from django.shortcuts import render, redirect
from .models import Stock_db
from django.contrib import messages
from .forms import StockForm

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_73f9af75bb524825925d2d7f52551716")
    
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error..."
        
        return render(request, 'index.html', {'api': api})

    else:
        return render(request, 'index.html', {'ticker': "Enter a Ticker Symbol above..."})

def stock(request):
    import requests
    import json
    
    if request.method == 'POST':
        ticker = request.POST['ticker']
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock has been added!'))
            return redirect('stock')

    else:
        ticker = Stock_db.objects.all()
        output = []
        
        for ticker_item in ticker:
            api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_73f9af75bb524825925d2d7f52551716")
        
            try:
                api = json.loads(api_request.content)
                output.append(api)
            
            except Exception as e:
                api = "Error..."

        return render(request,'stockpage.html', {'ticker' : ticker , 'output': output})
    

def about(request):
    return render(request, 'about.html', {})

def delete_stock(request):
    ticker = Stock_db.objects.all()
    return render(request, 'delete_stock.html', {'ticker' : ticker})


def delete(request, stock_id):
    item = Stock_db.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock has been deleted!'))
    return redirect(delete_stock)