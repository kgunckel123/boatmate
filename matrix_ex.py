from flask import Flask, render_template, request, make_response
from model import schedule_optimize, a

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

      output_type=[]
      output_component=[]
      #Output Type List
      for i in range(sum(result[0:4])):
         output_type.append('Pontoon')
      for i in range(sum(result[4:8])):
         output_type.append('Moomba')
      for i in range(sum(result[8:12])):
         output_type.append('Chanel')
      for i in range(sum(result[12:16])):
         output_type.append('Allison')
      for i in range(sum(result[16:20])):
         output_type.append('Tige')
      for i in range(sum(result[20:24])):
         output_type.append('Master Craft')
      for i in range(sum(result[24:28])):
         output_type.append('Nautique')

      if result[0]>0:
         for i in range(result[0]):
            output_component.append('Pinstripes')
      if result[1]>0:
         for i in range(result[1]):
            output_component.append('Runway')
      if result[2]>0:
         for i in range(result[2]):
            output_component.append('Both')
      if result[3]>0:
         for i in range(result[3]):
            output_component.append('Neither')
      if result[4]>0:
         for i in range(result[4]):
            output_component.append('Pinstripes')
      if result[5]>0:
         for i in range(result[5]):
            output_component.append('Runway')
      if result[6]>0:
         for i in range(result[6]):
            output_component.append('Both')
      if result[7]>0:
         for i in range(result[7]):
            output_component.append('Neither')
      if result[8]>0:
         for i in range(result[8]):
            output_component.append('Pinstripes')
      if result[9]>0:
         for i in range(result[9]):
            output_component.append('Runway')
      if result[10]>0:
         for i in range(result[10]):
            output_component.append('Both')
      if result[11]>0:
         for i in range(result[11]):
            output_component.append('Neither')
      if result[12]>0:
         for i in range(result[12]):
            output_component.append('Pinstripes')
      if result[13]>0:
         for i in range(result[13]):
            output_component.append('Runway')
      if result[14]>0:
         for i in range(result[14]):
            output_component.append('Both')
      if result[15]>0:
         for i in range(result[15]):
            output_component.append('Neither')
      if result[16]>0:
         for i in range(result[16]):
            output_component.append('Pinstripes')
      if result[17]>0:
         for i in range(result[17]):
            output_component.append('Runway')
      if result[18]>0:
         for i in range(result[18]):
            output_component.append('Both')
      if result[19]>0:
         for i in range(result[19]):
            output_component.append('Neither')
      if result[20]>0:
         for i in range(result[20]):
            output_component.append('Pinstripes')
      if result[21]>0:
         for i in range(result[21]):
            output_component.append('Runway')
      if result[22]>0:
         for i in range(result[22]):
            output_component.append('Both')
      if result[23]>0:
         for i in range(result[23]):
            output_component.append('Neither')
      if result[24]>0:
         for i in range(result[24]):
            output_component.append('Pinstripes')
      if result[25]>0:
         for i in range(result[25]):
            output_component.append('Runway')
      if result[26]>0:
         for i in range(result[26]):
            output_component.append('Both')
      if result[27]>0:
         for i in range(result[27]):
            output_component.append('Neither')

      type_weights = [i for i in range(num_trailers)]
      comp_weights = [i for i in range(num_trailers)]

      for v in range(num_trailers):
         if output_type[v] == 'Pontoon':
            type_weights[v] = t_weight[0]
         elif output_type[v] == 'Moomba':
            type_weights[v] = t_weight[1]
         elif output_type[v] == 'Chanel':
            type_weights[v] = t_weight[2]
         elif output_type[v] == 'Allison':
            type_weights[v] = t_weight[3]
         elif output_type[v] == 'Tige':
            type_weights[v] = t_weight[4]
         elif output_type[v] == 'Master Craft':
            type_weights[v] = t_weight[5]
         elif output_type[v] == 'Nautique':
            type_weights[v] = t_weight[6]
         if output_component[v] == 'Pinstripes':
            comp_weights[v] = c_weight[0]
         elif output_component[v] == 'Runway':
            comp_weights[v] = c_weight[1]
         elif output_component[v] == 'Both':
            comp_weights[v] = c_weight[2]
         elif output_component[v] == 'Neither':
            comp_weights[v] = c_weight[3]

      trailer_weights = [type_weights[i] + comp_weights[i] for i in range(num_trailers)]

      final_weights, final_order, running_total = schedule_optimize(trailer_weights)
      type_final = [i for i in range(num_trailers)]
      comp_final = [i for i in range(num_trailers)]
      for i in range(num_trailers):
         type_final[i] = output_type[final_order[i]]
         comp_final[i] = output_component[final_order[i]]

      return render_template("output.html", type=type_final, comp=comp_final, num_trailers=num_trailers, final_weights=final_weights, total=running_total)

if __name__ == '__main__':
   app.run(debug = True)