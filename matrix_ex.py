from flask import Flask, render_template, request, redirect
from model import schedule_optimize
from helper_functions import make_weights_from_input_dict
from helper_functions import writejson, loadjson

app = Flask(__name__)

data_file_name = '.boat_data.json'

@app.route('/')
def home():
   return render_template('begin.html')

@app.route('/change_weights')
def change_weights():
   if request.method == 'GET':
       # give a blank form
       pass
   if request.method == 'POST':
       # process a form
       pass

@app.route('/delete/<string:item_type>/<string:name>')
def delete_item(item_type, name):
    boat_data = loadjson(data_file_name)
    boat_data[item_type].pop(name, None)
    writejson(boat_data, data_file_name)
    return redirect('/change_weights')


@app.route('/matrix_form', methods=['POST','GET'])
def student():
   data_boats = loadjson(data_file_name)
   trailer_list= data_boats['Boats'].keys()
   component_list=data_boats['Components'].keys()
   if request.method == 'POST':
      return render_template('matrix_form.html', trailer_list= trailer_list, component_list=component_list)

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
      components = ['Pinstripes','Runway', 'Both', 'Neither']
      boat_weights = {boats[i]: t_weight[i] for i in range(len(boats))}
      comp_weights = {components[i]: c_weight[i] for i in range(len(components))}
      input_dict = dict()

      for boat_num, boat in enumerate(boats):
         for comp_num, comp in enumerate(components):
            input_dict[(boat, comp)] = int(result[boat_num * len(components) + comp_num])

      trailer_weights, output_type = make_weights_from_input_dict(input_dict, boat_weights, comp_weights)

      final_weights, final_order, running_total = schedule_optimize(trailer_weights)
      type_final = [i for i in range(num_trailers)]
      for i in range(num_trailers):
         type_final[i] = output_type[final_order[i]]

      return render_template("output.html", comp=type_final, num_trailers=num_trailers, final_weights=final_weights, total=running_total)

if __name__ == '__main__':
   app.run(debug = True)