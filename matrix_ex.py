from flask import Flask, render_template, request, redirect
from model import schedule_optimize
from helper_functions import make_weights_from_input_dict
from helper_functions import writejson, loadjson
from forms import AddWeight
import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'
data_file_name = '.boat_data.json'

@app.route('/')
def home():
   return render_template('begin.html')

@app.route('/change_weights', methods=['POST','GET'])
def change_weights():
    form = AddWeight()
    if request.method == 'GET':
        data_boats = loadjson(data_file_name)
        trailer_list = data_boats['Boats']
        component_list = data_boats['Components']
        return render_template('change_weights.html', trailer_list=trailer_list, component_list=component_list, form=form)

    if request.method == 'POST':
        new_name=form.name.data
        new_weight=form.weight.data
        new_type=form.item_type.data
        data_boats = loadjson(data_file_name)
        if new_type == 'Trailer':
            data_boats['Boats'].update({new_name: new_weight})
        if new_type == 'Component':
            data_boats['Components'].update({new_name: new_weight})
        writejson(data_boats, data_file_name)
        return redirect('/change_weights')

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
   return render_template('matrix_form.html', trailer_list= sorted(trailer_list), component_list=sorted(component_list))

@app.route('/output',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.getlist("trailer")
      #t_weight= request.form.getlist("t_weight")
      #c_weight = request.form.getlist("c_weight")
      #t_weight=list(map(int, t_weight))
      #c_weight = list(map(int, c_weight))
      result = list(map(int, result))
      num_trailers=sum(result)

      data_boats = loadjson(data_file_name)
      boats=data_boats['Boats'].keys()
      components=data_boats['Components'].keys()

      boat_weights = data_boats['Boats']
      comp_weights = data_boats['Components']

      #boats = ['Pontoon', 'Moomba', 'Chanel', 'Allison', 'Tige', 'Master Craft', 'Nautique']
      #components = ['Pinstripes','Runway', 'Both', 'Neither']
      #boat_weights = {boats[i]: t_weight[i] for i in range(len(boats))}
      #comp_weights = {components[i]: c_weight[i] for i in range(len(components))}
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
    url = 'http://127.0.0.1:5000'
    webbrowser.open_new(url)
    app.run(debug = False)