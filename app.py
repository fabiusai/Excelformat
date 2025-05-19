from flask import Flask, render_template, request, send_file, flash
from formatta import formatta_excel

app = Flask(__name__)
app.secret_key = 'sostituisci_con_una_chiave_random'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f or not f.filename.endswith('.csv'):
            flash('Seleziona un file .csv valido', 'danger')
            return render_template('index.html')

        excel_io = formatta_excel(f.read())
        return send_file(
            excel_io,
            as_attachment=True,
            download_name='report_editoriale_formattato.xlsx',
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
