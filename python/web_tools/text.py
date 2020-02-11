shared_doc_kwargs = dict(
    axes="index, columns",
    klass="DataFrame",
    axes_single_arg="{0 or 'index', 1 or 'columns'}",
    axis="""axis : {0 or 'index', 1 or 'columns'}, default 0
        If 0 or 'index': apply function to each column.
        If 1 or 'columns': apply function to each row.""",
    optional_by="""
        by : str or list of str
            Name or list of names to sort by.

            - if `axis` is 0 or `'index'` then `by` may contain index
              levels and/or column labels
            - if `axis` is 1 or `'columns'` then `by` may contain column
              levels and/or index labels

            .. versionchanged:: 0.23.0
               Allow specifying index or column level names.""",
    versionadded_to_excel="",
    optional_labels="""labels : array-like, optional
            New labels / index to conform the axis specified by 'axis' to.""",
    optional_axis="""axis : int or str, optional
            Axis to target. Can be either the axis name ('index', 'columns')
            or number (0, 1).""",
)



shared_doc_kwargs.update


for item,value  in shared_doc_kwargs.items():
    print (value)

print(value.__sizeof__.__name__)