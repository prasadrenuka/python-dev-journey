try:
    a= input('Enter an number')
    b = int(a)
    # a= 10/0
    if(b<0):
     raise ValueError ("Age can't be negative")
except ZeroDivisionError:
    print('can\'t be divided by zero')
except ValueError:
    print('Pleas Enter the valid input')

# multiple errors handled in single except
# except (ZeroDivisionError, ValueError) as e:
#     print('caught an error:', e)
except Exception as e:
    print('Error:', e)
else:
    print('there was no error')
finally:
    print('code ran with or without an error')
