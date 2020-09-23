#! /usr/bin/python
import pandas as pd
import numpy as np
#from .microbiota import *

import matplotlib.pylab as plt

from matplotlib import gridspec


def count_sample_for_legend(variable, Grouping_Variable, order):
    '''
    generate legend such as ['E.coli\nn=7', 'Other\nn=7', 'negative\nn=15', 'rotaEAEC\nn=16', 'rotavirus\nn=26']
    '''
    variable_ =pd.Series(variable)
    count_samples= variable_.groupby(Grouping_Variable).count().loc[order]
    return ['{}\nn={}'.format(*label) for label in count_samples.iteritems()]


def Bubbleplot(data,indexes='show',headers='show',aspect_size=200., value_max=100,marker='s',
               ax=None,legend='normal',legend_title=None, color='blue'):

    """sample ids X feature ids"""
    data=data.T

    try:
        sns.set_style("whitegrid")
    except:
        pass

    #NORMALIZE
    size=data.values.ravel()/float(value_max)

    y,x=np.arange(data.shape[0]-1,-1,-1), np.arange(data.shape[1])
    X,Y=plt.meshgrid(x,y)
    X,Y=X.ravel(), Y.ravel()


    if ax is None:
        ax = plt.subplot(111)

    ax.yaxis.tick_right()
    ax.scatter(X,Y,s=size*float(aspect_size),marker=marker, color= color)

    #AXES
    if headers is None:
        ax.set_xticklabels(ax.get_xticklabels(), visible=False)


    elif headers=='show':
        ax.set_xticks(x+0.5)
        ax.set_xticklabels(data.columns.values, ha='right',rotation=90)
        ax.set_xlim([-.5,max(x)+.5])

    elif headers=='hide':
        ax.set_xticks(x+0.5)
        ax.set_xlim([-.5,max(x)+.5])
        ax.set_xticklabels(data.columns.values,rotation=90, visible=False)



    if indexes=='show':
        ax.set_yticks(y-0.5)
        ax.set_yticklabels(data.index.values,va='bottom')
    else:
        ax.yaxis.set_visible(False)
    ax.set_ylim([-.5,max(y)+.5])

    #LEGEND
    if legend!='hide':
        sizes = np.array([0.1,0.5,1.])
        labels=(sizes*value_max).astype(type(value_max))


        lines=[plt.scatter([],[], s=s*aspect_size, edgecolors='none',marker=marker, color= color) for s in sizes]
        legend_prop=dict(ncol=len(labels), frameon=False,loc = 2,scatterpoints = 1,
            bbox_to_anchor=(1, 0), borderaxespad=0.25,title=legend_title)
        if legend=='normal':

            leg = ax.legend(lines, labels, fontsize=12, handlelength=2, borderpad = 1.8, handletextpad=1 ,**legend_prop)
        elif legend=='slim':
            leg = ax.legend(lines, labels, fontsize='x-small', borderpad = 0.7,**legend_prop)
    return ax



def Grouped_Bubble_Plot(data,grouping_variables,headers='hide',
                        figsize=(15,10),order=None,value_max=1.,sp_keywords={},Grid=None):
    """sample ids X feature ids"""
    data=data.T

    if order is None:
        order=np.unique(grouping_variables)


    Grouped_data= data.groupby(grouping_variables,axis=1)




    ngroups =len(order)
    index_of_subplot=dict(zip(order,range(ngroups)))

## make grid
    if Grid is None:

        fig = plt.figure(figsize=figsize)
        Grid=gridspec.GridSpec(1,1)[0]

    gs =gridspec.GridSpecFromSubplotSpec(1,ngroups,subplot_spec=Grid ,
                                         width_ratios= Grouped_data.size().loc[order].values,
                                        wspace=0.05)
    axes=[plt.subplot(gs[0])]

    for i in range(1,ngroups):
        axes.append(plt.subplot(gs[i],sharey=axes[0]))

    #gridspec_kw=dict(width_ratios= Grouped_data.size().loc[order].values ) # adapt widths

    #fig, axes = plt.subplots(1,ngroups, sharex=False, sharey=True, figsize=figsize,gridspec_kw=gridspec_kw)




    for group_name in order[:-1]:

        data_group = Grouped_data.get_group(group_name)
        ax=axes[index_of_subplot[group_name]]

        Bubbleplot(data_group,value_max=value_max,indexes='show',headers=headers,ax=ax,**sp_keywords)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.setp(ax.get_legend(),visible=False)
        ax.set_title(group_name)



    #plt.tight_layout(pad=0.0)
    group_name=order[-1]
    ax=axes[-1]
    data_group = Grouped_data.get_group(group_name)
    Bubbleplot(data_group,value_max=value_max,headers=headers,indexes='show',ax=ax,**sp_keywords)
    ax.set_title(group_name)



    return axes




def BarPlot(data,colormap='Paired',ax=None,headers='show',value_max=None,x_ticklabels_rotation=90,**kws):
    """sample ids X feature ids"""
    if ax is None:
        ax=plt.subplot(111)

    if value_max is None:
        value_max=data.sum(1).max()

    data.plot(kind='bar', stacked=True,colormap=colormap, ax=ax,**kws)
    ax.set_ylim((0,value_max))


    #reverse legend order
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(reversed(handles),reversed(data.columns),bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    #AXES
    if (headers is None or headers=='hide'):
        ax.get_xaxis().set_visible(False)
        ax.get_xaxis().set_ticks([])
    elif headers=='show':
        plt.setp(ax.get_xticklabels(),rotation=x_ticklabels_rotation)
        ax.set_xlabel(None,visible=False)


    #plt.tight_layout()


    return ax


def Grouped_Bar_Plot(data,grouping_variable,headers='hide',
                        figsize=(15,10),order=None,value_max=100.,sp_keywords={},
                    Grid=None):

    """sample ids X feature ids"""

    grouping_variables=grouping_variable
    data=data.T

    if order is None:
        order=np.unique(grouping_variables)


    Grouped_data= data.groupby(grouping_variables,axis=1)




    ngroups =len(order)
    index_of_subplot=dict(zip(order,range(ngroups)))


## make grid
    if Grid is None:

        fig = plt.figure(figsize=figsize)
        Grid=gridspec.GridSpec(1,1)[0]

    gs =gridspec.GridSpecFromSubplotSpec(1,ngroups,subplot_spec=Grid ,
                                         width_ratios= Grouped_data.size().loc[order].values)
    axes=[plt.subplot(gs[0])]

    for i in range(1,ngroups):
        axes.append(plt.subplot(gs[i],sharey=axes[0]))


    #gridspec_kw=dict(width_ratios= Grouped_data.size().loc[order].values ) # adapt widths

    #fig, axes = plt.subplots(1,ngroups, sharex=False, sharey=True, figsize=figsize,gridspec_kw=gridspec_kw)


    for group_name in order:

        data_group = Grouped_data.get_group(group_name)
        ax=axes[index_of_subplot[group_name]]

        BarPlot(data_group.T,value_max=value_max,headers=headers,ax=ax,**sp_keywords)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.setp(ax.get_legend(),visible=False)
        ax.set_title(group_name)



    plt.setp(axes[-1].get_legend(),visible=True)
    plt.setp(axes[0].get_yticklabels(), visible=True)
    plt.tight_layout(pad=0.8)
    return axes



def MeanGroup_Barplot(data,grouping_variable,filtervalue=20,mode='fixed',order=None,figsize=(8,8),sp_keywords={},x_ticklabels_rotation=0):
    """ samples x features"""
    if order is None:
        order=np.unique(grouping_variable)

    Grouped=data.groupby(grouping_variable)
    refined=minfilter(Grouped.mean(),value=filtervalue, mode=mode)
    refined=refined.loc[order]

    plt.figure(figsize=figsize)
    ax=plt.subplot(111)
    ax=BarPlot(refined,headers='show',**sp_keywords)
    ax.set_xticklabels(count_sample_for_legend(pd.Series(1,index=data.index),grouping_variable,order=order),rotation=x_ticklabels_rotation)
    return ax
