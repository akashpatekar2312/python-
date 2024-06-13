import math
input_height = 3 
input_width = 9 
fixed_coverage = 5
# formula = (hight*width) / 5

def paint_calc(height=input_height,width=input_width,coverage=fixed_coverage):
    cans_to_paint = ((height * width) / coverage)
    cans_float = (float(cans_to_paint))
    final_cans = (math.ceil(cans_float))
    print (f"You would require total of '{final_cans}' cans of paint to paint the specified wall")
    

paint_calc()
# print(math.ceil(4.2))
