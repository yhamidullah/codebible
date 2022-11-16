import glob
import os


def remove_files_by_time(path, n=1, last=False, ext=""):
    """
    :param path:
    :param n: number of files
    :param last: True means -> newest files (last created)
                 False means -> oldest files (first created)
    :param ext: extension example: ".jpeg", ".py"..
    :return: None
    """

    paths = glob.glob("{}/*{}".format(path, ext))
    paths.sort(key=lambda s: os.path.getmtime(s), reverse=last)
    tmp = paths[:n]
    for file in tmp:
        os.remove(file)



