import altair as alt
from vega_datasets import data

def make_static_chart():
    '''
    '''
    return alt.Chart(data=data.cars.url).mark_circle(size=60).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    ).interactive()

def make_interactive_chart():
    '''
    '''
    pts = alt.selection(type="single", encodings=['x'])

    rect = alt.Chart(data.movies.url).mark_rect().encode(
        alt.X('IMDB_Rating:Q', bin=True),
        alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
        alt.Color('count()',
            scale=alt.Scale(scheme='greenblue'),
            legend=alt.Legend(title='Total Records')
        )
    )

    circ = rect.mark_point().encode(
        alt.ColorValue('grey'),
        alt.Size('count()',
            legend=alt.Legend(title='Records in Selection')
        )
    ).transform_filter(
        pts
    )

    bar = alt.Chart(data.movies.url).mark_bar().encode(
        x='Major_Genre:N',
        y='count()',
        color=alt.condition(pts, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
    ).properties(
        selection=pts,
        width=550,
        height=200
    )

    return alt.vconcat(
        rect + circ,
        bar
    ).resolve_legend(
        color="independent",
        size="independent"
    )
