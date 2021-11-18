#! /usr/bin/python
import pandas as pd
import numpy as np

# from .microbiota import *

import matplotlib.pylab as plt

import warnings

from matplotlib import gridspec


def filter_taxa(data, topN=15, combine_as_other=True, based_on=np.mean):
    """sample ID X bacteria_taxa"""

    if data.shape[0] > data.shape[1]:
        warnings.warn(
            "May be your data is not in the right orientation sample x feature"
        )

    if data.shape[1] <= topN:
        return data

    N = min(topN, data.shape[1]) - 1 - int(combine_as_other)
    filter_values = based_on(data)
    criteria = filter_values >= filter_values.sort_values(ascending=False).iloc[N]

    refined = data.loc[:, criteria].copy()

    if combine_as_other:
        refined["Other"] = data.loc[:, ~criteria].sum(1)
    return refined


def count_sample_for_legend(variable, Grouping_Variable, order):
    """
    generate legend such as ['E.coli\nn=7', 'Other\nn=7', 'negative\nn=15', 'rotaEAEC\nn=16', 'rotavirus\nn=26']
    """
    variable_ = pd.Series(variable)
    count_samples = variable_.groupby(Grouping_Variable).count().loc[order]
    return ["{}\nn={}".format(*label) for label in count_samples.iteritems()]


def BarPlot(
    data,
    colormap="Paired",
    ax=None,
    headers="show",
    value_max=None,
    x_ticklabels_rotation=90,
    **kws
):
    """sample ids X feature ids"""
    if ax is None:
        ax = plt.subplot(111)

    if value_max is None:
        value_max = data.sum(1).max()

    data.plot(kind="bar", stacked=True, colormap=colormap, ax=ax, **kws)
    ax.set_ylim((0, value_max))

    # reverse legend order
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        reversed(handles),
        reversed(data.columns),
        bbox_to_anchor=(1.05, 1),
        loc=2,
        borderaxespad=0.0,
    )

    # AXES
    if headers is None or headers == "hide":
        ax.get_xaxis().set_visible(False)
        ax.get_xaxis().set_ticks([])
    elif headers == "show":
        plt.setp(ax.get_xticklabels(), rotation=x_ticklabels_rotation)
        ax.set_xlabel(None, visible=False)

    # plt.tight_layout()

    return ax


def Grouped_Bar_Plot(
    data,
    grouping_variable,
    headers="hide",
    figsize=(15, 10),
    order=None,
    value_max=100.0,
    sp_keywords={},
    Grid=None,
):

    """sample ids X feature ids"""

    grouping_variables = grouping_variable
    data = data.T

    if order is None:
        order = np.unique(grouping_variables)

    Grouped_data = data.groupby(grouping_variables, axis=1)

    ngroups = len(order)
    index_of_subplot = dict(zip(order, range(ngroups)))

    ## make grid
    if Grid is None:

        fig = plt.figure(figsize=figsize)
        Grid = gridspec.GridSpec(1, 1)[0]

    gs = gridspec.GridSpecFromSubplotSpec(
        1,
        ngroups,
        subplot_spec=Grid,
        width_ratios=Grouped_data.size().loc[order].values,
    )
    axes = [plt.subplot(gs[0])]

    for i in range(1, ngroups):
        axes.append(plt.subplot(gs[i], sharey=axes[0]))

    # gridspec_kw=dict(width_ratios= Grouped_data.size().loc[order].values ) # adapt widths

    # fig, axes = plt.subplots(1,ngroups, sharex=False, sharey=True, figsize=figsize,gridspec_kw=gridspec_kw)

    for group_name in order:

        data_group = Grouped_data.get_group(group_name)
        ax = axes[index_of_subplot[group_name]]

        BarPlot(
            data_group.T, value_max=value_max, headers=headers, ax=ax, **sp_keywords
        )
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.setp(ax.get_legend(), visible=False)
        ax.set_title(group_name)

    plt.setp(axes[-1].get_legend(), visible=True)
    plt.setp(axes[0].get_yticklabels(), visible=True)
    plt.tight_layout(pad=0.8)
    return axes


def MeanGroup_Barplot(
    data,
    grouping_variable,
    filtervalue=20,
    mode="fixed",
    order=None,
    figsize=(8, 8),
    sp_keywords={},
    x_ticklabels_rotation=0,
):
    """ samples x features"""
    if order is None:
        order = np.unique(grouping_variable)

    Grouped = data.groupby(grouping_variable)
    refined = minfilter(Grouped.mean(), value=filtervalue, mode=mode)
    refined = refined.loc[order]

    plt.figure(figsize=figsize)
    ax = plt.subplot(111)
    ax = BarPlot(refined, headers="show", **sp_keywords)
    ax.set_xticklabels(
        count_sample_for_legend(
            pd.Series(1, index=data.index), grouping_variable, order=order
        ),
        rotation=x_ticklabels_rotation,
    )
    return ax
