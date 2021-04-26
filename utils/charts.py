import plotly.graph_objects as go

'''
    Utilities to generate charts on the changes of the fitness through generations
'''
def create_figure():
  return go.Figure()
  
def plot_figure(fig, data, color, title):  
    
  y_axis = [float(x) for x in data]
  fig.add_scatter(
    y=y_axis,
    x=[x+1 for x in range(len(y_axis))],
    mode="lines+markers", 
    textposition="bottom center",
    name=title,
    line={"color": color, "width": 1}
  )
  fig.update_layout(
    title="Fitness chart",
    width=1024,
    height=400,
    xaxis_title="Generations",
    yaxis={"title": "Fitness value", "tickformat": ".2f"},
    font=dict(
      family="Courier New, monospace",
      size=14,
      color="#7f7f7f"
    )
  )

def plot_multiBar(fig, labels, data_x, data_y, color, titles):
    plot_data = []
    for i in range(len(data_x)):
        plot_data.append( go.Bar(name=labels[i], x=data_x[i], y=data_y[i]) )
    fig.add_traces(data=plot_data)
    fig.update_layout(
        title=titles['title'],
        x_axis_title=titles['x_title'],
        barmode='group',
        yaxis={"title": titles['y_title'], "tickformat": ".2f"},
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#7f7f7f"
        )
    )