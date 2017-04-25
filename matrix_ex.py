from flask import Flask, render_template, request, make_response
from model import schedule_optimize
from helper_functions import make_weights_from_input_dict

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Begin.html')

@app.route('/matrix_form', methods=['POST','GET'])
def student():
   if request.method == 'POST':
      return render_template('matrix_form.html')

@app.route('/output',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.getlist("trailer")
      t_weight= request.form.getlist("t_weight")
      c_weight = request.form.getlist("c_weight")
      t_weight=list(map(int, t_weight))
      c_weight = list(map(int, c_weight))
      result = list(map(int, result))
      num_trailers=sum(result)

      boats = ['Pontoon', 'Moomba', 'Chanel', 'Allison', 'Tige', 'Master Craft', 'Nautique']
      componets = ['Pinstripes','Runway', 'Both', 'Neither']
      input_dict = {}

      for boat_num, boat in enumerate(boats):
         for comp_num, comp in enumerate(componets):
            input_dict[(boat, comp)] = int(result[boat_num * 4 + comp_num])

      trailer_weights, output_type = make_weights_from_input_dict(input_dict, ) # todo add bases and componets

      final_weights, final_order, running_total = schedule_optimize(trailer_weights)
      type_final = [i for i in range(num_trailers)]
      for i in range(num_trailers):
         type_final[i] = output_type[final_order[i]]

      return render_template("output.html", comp=type_final, num_trailers=num_trailers, final_weights=final_weights, total=running_total)

if __name__ == '__main__':
   app.run(debug = True)