"""

! pip install cloudmesh.notebooks

from cloudmesh.notebooks import Notebook

Notebook.config(
    git="gitrepo",
    processor = "2",
    path = '..',
    collab = not romeo,
    directory = "/content/...."
)

Notebook.filename("../data")
Notebook.gitclone("https:// ....)
Notebook.gitclone("ssh:// ....)

sc_df = utils.read_sc_catalog(Notebook.filename('../data/USGS_SC_1990-2019.catalog'))
"""

import os
import sys


class Notebook:

    def config(
        processors="2",
        path='..',
        directory="/content/....",
    ):
        _COLAB = 'google.colab' in sys.modules

        os.environ["CUDA_VISIBLE_DEVICES"] = processors
        sys.path.insert(0, os.path.abspath(path))


    def filename(name, prefix="/content"):
        if _COLAB:
            return f"/{prefix}/{name}"
        else:
            return name


    def gitclone(name, path, pull=False):
        """

        :param path:
        :param pull:
        :return:
        """

        """
        name - repo https or ssh link
        path - path where things to unpack to
        update - if true do a pull even if repo is alredy cloned, default False
        
        I think we already have git cone command in cloudmesh.common
        """
        pass
        # if git repo already there pass
        # else:
        #    do git clone

