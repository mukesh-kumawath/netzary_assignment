from calendar import month
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from dateutil import relativedelta
def index(request):
    return render(request, 'index.html')

def display_intrest(request):
    loan_date= request.POST["Loan_date"]
    pledge_date=request.POST["pledge_date"]
    amount= int(request.POST["amount"])
    intrest=request.POST["intrest"]
    period=date_diff( loan_date,pledge_date)
    if intrest=="":
        if amount <= 5000 :
                total_intrest=calculate_intrest(period.years,period.months,period.days,amount,3)
        else:
            total_intrest=calculate_intrest(period.years,period.months,period.days,amount,2)
    else:
        total_intrest=calculate_intrest(period.years,period.months,period.days,amount,intrest)
    return render(request,'display_intrest.html',{"years":period.years,"months":period.months,"days":period.days,"final_amount":total_intrest})

def date_diff(d1,d2):
    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.strptime(d2, "%Y-%m-%d")
    diff = relativedelta.relativedelta(date2, date1)
    years = diff.years
    months = diff.months
    days = diff.days
    print('{} years {} months {} days'.format(years, months, days))
    return (diff)

def calculate_intrest(years,months,days,amount,intrest):
    monthly_intrest=0
    days_intrest=0
    if years > 0:
        for i in range(0,years):
            cpAmount=(amount*years*12*intrest)/100
            amount=cpAmount+amount
            print("year",i+1, " compound intrest=",cpAmount,"principle amount ",amount)
    if months > 0:
        monthly_intrest=(amount*months*intrest)/100
        print("monthly compound intrest=",monthly_intrest)
    if days > 0:
        per_day=((amount*intrest)/100)/30
        days_intrest=per_day*days
        print("days_intrest compound intrest=",days_intrest)
    total_intrest=monthly_intrest+days_intrest
    print("final intrest=",total_intrest)
    return (amount+total_intrest)
