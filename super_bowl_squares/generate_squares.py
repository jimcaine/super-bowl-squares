import random
import pandas as pd

def generate_squares(players, blank_squares='Unbought', export_path=None):
    """
    Generates Super Bowl squares given either a list of players to evenly
    distribute the squares or a dictionary where the keys represent the player
    name and the values represent the number of squares to allocate.  If the
    number of players or number of squares do not evenly allocate across 100
    squares, these squares will be filled in with the value of the
    blank_squares parameter.  The output of the squares will be returned as a
    Pandas DataFrame, but can also be exported to CSV if the export_path is
    provided.

    Parameters
    ----------
    players : list[str] | dict[str:int]
        If a list is provided, the squares will be allocated evenly across
        all values in the list.  If a dictionary is provided representing the
        players as keys and number of squares purchased as the values, the
        squares will be allocated accordingly.

    blank_squares : str
        Value to fill in non-allocated (extra) squares.  This is a great way
        to make your dog feel included.

    export_path : str
        Local file system path to save exported squares as a CSV file.

    export_type : enum ['csv']
        The file type to save the results.  Currently, only CSV is supported.
    """

    def chunk_list(l, n):
        """
        Generator function to transform a list into a list of list with chunks
        of size n.

        Parameters
        ----------
        l : list
            The list to transform.

        n : int
            The number of items in each "chunk"
        """
        for i in range(0, len(l), n):
            yield l[i:i + n]

    # declare function to flatten list
    flatten = lambda t: [item for sublist in t for item in sublist]

    # create a flat list of 100 values that will be used to fill in the squares
    if isinstance(players, dict):
        l = flatten([[k]*v for k,v in players.items()])

    elif isinstance(players, list):
        l = players*int(100/len(players))

    # fill in blank squares
    l = l + [blank_squares]*(100-len(l))

    # shuffle list to ensure that square are picked randomly
    random.shuffle(l)

    # create pandas DataFrame and fill in values with the names
    df = pd.DataFrame(
        data=list(chunk_list(l, 10)),
        index=range(10),
        columns=range(10))

    # add home / away multiindex
    df.columns = pd.MultiIndex(
        levels=[range(10)],
        codes=[range(10)],
        names=['Home'])

    df.index = pd.MultiIndex(
        levels=[range(10)],
        codes=[range(10)],
        names=['Away'])

    # save to csv
    if export_path:
        print('Saving to CSV.')
        df.to_csv(export_path)

    return df
