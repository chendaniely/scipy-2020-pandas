try:
    import pandas as pd
    import seaborn as sns
    import sklearn as sk
except ImportError:
    print("""Missing packages.
    Please make sure pandas, seaborn, and scikit-learn are installed.
    You can do this with conda or pip:

    conda: conda install pandas seaborn scikit-learn

    pip: pip install pandas seaborn scikit-learn
    """
    )

try:
    from pyprojroot import here
except ImportError:
    print("""Take a look at the pyprojroot library,
    it may make your data analysis projects easier:
    https://github.com/chendaniely/pyprojroot
    """)


try:
    pd.read_csv(here("./data/gapminder.tsv"), sep='\t')
except NameError:
    print("Unable to load dataset using pd. Do you have pandas installed?")
except FileNotFoundError:
    print("""Libraries are all installed, but I could not find the './data/gapminder.tsv' file.
    Make sure you have the datasets in the 'data' folder, it should match the website on GitHub.

    If you have the datasets on your computer, this may be a working directory issue.
    Make sure you are running `python test_installation.py` from the correct location.

    The more import thing is that you have the datasets on your computer with the necessary libraries installed.
    """)

