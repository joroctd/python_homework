import traceback

END_LINE = 'done for now'

try:
    with open('diary.txt', 'w') as diary:
        line = input('What happened today?\n')
        while not line == END_LINE:
            diary.write(line + '\n')
            line = input('What else?\n')
        diary.write(END_LINE + '\n\n')

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")