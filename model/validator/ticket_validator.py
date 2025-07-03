import re


def code_validator(ticket_code):
   return re.match(r'^[0-9]{1,2}$',str(ticket_code))

def source_validator(source):
    return re.match(r'(Qeshm|Kish|Shiraz|Esfahan|Tehran|Mashhad)',source)

def destination_validator(destination):
    return re.match(r'(Qeshm|Kish|Shiraz|Esfahan|Tehran|Mashhad)',destination)

def airline_validator(airline):
    return re.match(r'(Qeshm air|Aseman|Mahan air|Iran air|Meraj|Kish airline)',airline)


def start_date_time_validator(start_date_time):
   return re.match(r'^14[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$',start_date_time)

def end_date_time_validator(end_date_time):
    return re.match(r'^14[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$',end_date_time)

def price_validator(price):
    return re.match(r'^[0-9]{7,}$',str(price))

def seat_no_validator(seat_no):
    return re.match(r'^[0-9]{1,2}$',str(seat_no))

