# flasked-altair

- Tools to build simple dashboard/webapp with Flask and Altair! 
- Inspired by Plotly's Dash
- Build the environment with `conda`, and activate it

```
conda env create -f environment.yml
```

- Start the Flask app 

```
python app.py
```

## Known Issues

- Tooltips don't work yet. If your Altair chart has tooltips, it will raise an error when trying to export as JSON configuration for vega-lite.
