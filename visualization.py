import plotly
import matplotlib
import plotly.graph_objs as go
import math

#------ Visualization - Scatter Plots ---------------------
# Scatter plotting failed due to data being too discrete


def generateScatterPlot(plot_filename, plot_table):

    # Set marker properties. Put each number in avg_pers_trait_table to the power of
    #   two to make differences between points more obvious. Muptiplied by 1.5 just
    #   because that factor made the chart look pretty.
    markersize = [math.pow(i, 2)*1.5 for i in plot_table['C']]
    markercolor = plot_table['O']

    #Make Plotly figure
    fig1 = go.Scatter3d(x=plot_table['E'],
                      y=plot_table['N'],
                      z=plot_table['A'],
                      marker=dict(size=markersize,
                                    color=markercolor,
                                    opacity=0.9,
                                    reversescale=False,
                                    colorscale='Blues'),
                        line=dict (width=0.02),
                        mode='markers')

    #Make Plot.ly Layout
    mylayout = go.Layout(scene=dict(xaxis=dict(title="Extraversion"),
                         yaxis=dict(title="Neuroticism"),
                         zaxis=dict(title="Agreeableness")))

    #Plot and save html
    plotly.offline.plot({"data": [fig1],
                         "layout": mylayout},
                         auto_open=True,
                         filename=(plot_filename))

# ------------ Visualization - Histograms -----------------

# Import the libraries
# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# num_hist_categories = 10
# # matplotlib histogram
# plt.hist(plot_table['E'], color = 'blue', edgecolor = 'black',
#          bins = (1))
#
# # seaborn histogram
# sns.distplot(avg_pers_trait_table['E'], hist=True, kde=False,
#              bins=(1), color = 'blue',
#              hist_kws={'edgecolor':'black'})
# # Add labels
# plt.title('Histogram of Traits')
# plt.xlabel('E')
# plt.ylabel('E Commonality')
#
# plt.tight_layout()
# plt.show()
