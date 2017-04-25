from flask import Flask, render_template, request, make_response
from model import schedule_optimize
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('form_ex.html')

@app.route('/make_list',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = int(request.form["trailer_num"])
      return render_template("make_list.html", result=result)

@app.route('/output',methods = ['POST', 'GET'])
def output():
    if request.method == 'POST':
      output_type= request.form.getlist("type")
      output_component=request.form.getlist("comp")

    num_trailers=len(output_type)
    type_weights=[i for i in range(num_trailers)]
    comp_weights = [i for i in range(num_trailers)]
    for v in range(num_trailers):
        if output_type[v]=='Pontoon':
            type_weights[v]= 5
        elif output_type[v]=='Moomba':
            type_weights[v]= 1
        elif output_type[v]=='Chanel':
            type_weights[v]= 6
        elif output_type[v]=='Allison':
            type_weights[v]= 4
        if output_component[v]=='Pinstripes':
            comp_weights[v]= 5
        elif output_component[v]=='Runway':
            comp_weights[v]= 4
        elif output_component[v]=='Both':
            comp_weights[v]= 9
        elif output_component[v]=='Neither':
            comp_weights[v]= 0

    final_weights= [type_weights[i] + comp_weights[i] for i in range(num_trailers) ]
    final=schedule_optimize(final_weights)
    type_final=[i for i in range(num_trailers)]
    comp_final=[i for i in range(num_trailers)]
    for i in range(num_trailers):
        type_final[i]=output_type[final[i]]
        comp_final[i]=output_component[final[i]]

    #optimized_weights=[i for i in range(len(output_type))]
    #for i in range(len(output_type)):
    #    optimized_weights[i]=final_weights[final[i]]

    return render_template("output.html", type= type_final, comp= comp_final, num_trailers=num_trailers)

if __name__ == '__main__':
   app.run(debug = True)