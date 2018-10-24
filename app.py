from flask import Flask, render_template, url_for, redirect, jsonify
import json
from src import Div
from src import make_static_chart, make_interactive_chart

# ----- Generate Altair Charts -----
chart_1 = make_static_chart()
chart_2 = make_interactive_chart()

# ----- Charts Payload -----
charts_ = [{'id': 'scatter_1',
            'chart_as_json': json.loads(chart_1.to_json())
            },
           {'id': 'interactive_1',
            'chart_as_json': json.loads(chart_2.to_json())
            }
    ]

# ----- Build Payload -----

page_title = Div(id='page_title',
                 class_='tc f2 code pa4 bg-washed-green',
                 children='Flask + Altair')

row_1 = Div(class_='pa4 w-60 center bb helvetica fw2',
            children='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas recusandae doloremque itaque fugit cupiditate asperiores, atque, voluptates eum enim culpa eos! Repellat, ab, ipsam molestiae ut molestias unde sunt deserunt distinctio non modi et nisi quas in rem, minus odio possimus expedita quam officia dolores. Nam sint enim neque modi et a nisi eligendi recusandae dolorem. Neque cum numquam, expedita nostrum officiis, dicta quo quidem rerum molestias voluptates aspernatur ut quos amet modi praesentium. Tempora illo, nihil mollitia expedita fugit quos ut incidunt placeat dolores perferendis ullam, labore aspernatur dicta sunt a minima adipisci fuga, quaerat quasi delectus harum facere.')

row_2 = Div(class_='w-60 center bb helvetica fw2',
            children=[
                Div(class_='fl w-50 pa4',
                    id='scatter_1',
                    children=None),
                Div(class_='fl w-50 pa4 tl',
                    children='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Praesentium eveniet iusto, delectus qui veniam assumenda provident, repellendus consectetur enim quia explicabo quam, maiores, id doloribus reiciendis. Suscipit nobis obcaecati aliquam dolores similique eligendi earum totam exercitationem odit accusamus, nihil blanditiis vel deleniti facilis eos, optio repellendus quod provident ipsum libero sapiente explicabo consectetur iusto sunt. Dolorem veniam mollitia amet, aliquid libero vero. Ad doloribus quae tempore quis nulla eius, ea eum sunt provident aspernatur dignissimos esse, reprehenderit, tenetur laudantium placeat.')
                ])

row_3 = Div(class_='w-60 center bb helvetica fw2',
            children=[
                Div(class_='tc w-100 pa4',
                    children='Click on a bar on the histogram to interact with the visualization.'),
                Div(id='interactive_1',
                    class_='w-100',
                    children=None)])

payloads_ = [page_title, row_1, row_2, row_3]

# ------ Build Flask App ------
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', payloads=payloads_, charts=charts_)

if __name__ == '__main__':
    app.run(debug=True)
