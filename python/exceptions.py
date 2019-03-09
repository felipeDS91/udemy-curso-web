# Python 2.7
'''
try:
	1/0
except Exception, e:
	raise
else: # Else means no exception
	pass
finally: # It will always execute
	pass
'''

# Python 3
try:
	1/0
# Here we can specify one or more types of exceptions or just use the first parameter "Exception"
except(Exception, ZeroDivisionError) as e:
	print(e)
else:
	print('No exception')
finally:
	print('Finally')