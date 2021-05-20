from covid_india import states

from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = states.getdata('Total')
    data = list(data.values())
    confirmed_case = str(data[1] + data[2] + data[3])
    active_case = str(data[1])
    recovered_case = str(data[2])
    deaths = str(data[3])
    icfc = "Confirmed case: " + confirmed_case
    iatc = "Active case: " + active_case
    irvc = "Recovered: " + recovered_case
    idth = "Deaths: " + deaths
    return render_template('index.html', icfc=icfc, iatc=iatc, irvc=irvc, idth=idth)


@app.route('/search', methods=['GET', 'POST'])
def search():
    data = states.getdata('Total')
    data = list(data.values())
    confirmed_case = str(data[1] + data[2] + data[3])
    active_case = str(data[1])
    recovered_case = str(data[2])
    deaths = str(data[3])
    icfc = "Confirmed case: " + confirmed_case
    iatc = "Active case: " + active_case
    irvc = "Recovered: " + recovered_case
    idth = "Deaths: " + deaths
    data = ''
    state = request.form.getlist('state')

    if len(state) == 0:
        abort(500)

    if state[0] != 'Select location':
        data = states.getdata(state[0])
    else:
        return redirect('/')
    data = list(data.values())
    confirmed_case = str(data[1] + data[2] + data[3])
    active_case = str(data[1])
    recovered_case = str(data[2])
    deaths = str(data[3])
    cfc = "Confirmed case: " + confirmed_case
    atc = "Active case: " + active_case
    rvc = "Recovered: " + recovered_case
    dth = "Deaths: " + deaths
    return render_template('index.html', stat=state[0], cfc=cfc, atc=atc, rvc=rvc, dth=dth, icfc=icfc, iatc=iatc, irvc=irvc, idth=idth)


if __name__ == '__main__':
    app.run(debug=True)
