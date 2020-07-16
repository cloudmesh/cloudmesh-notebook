import os
import sys

! pip
install
cloudmesh.notebook

import cloudmesh.notebook

....


def notebook(
    processors="2",
    path='..',
    directory="/content/....",
):
    _COLAB = 'google.colab' in sys.modules

    os.environ["CUDA_VISIBLE_DEVICES"] = processors
    sys.path.insert(0, os.path.abspath(path))


def filename(name):
    if _COLAB:
        return f"/content/{name}"
    else:
        return name


def gitclone(name, path, pull=False):
    "
    name - repo
    https or ssh
    link
    path - path
    where
    things
    to
    unpack
    to
    update - if true
    do
    a
    pull
    even if repo is alredy
    cloned, default
    False
    "
    pass
    # if git repo already there pass
    # else:
    #    do git clone


notebook(
    git="gitrepo"
processor = "2",
            path = '..',
                   collab = not romeo,
                            directory = "/content/...."
)



filename("../data")
gitclone("https:// ....)
gitclone("ssh:// ....)

sc_df = utils.read_sc_catalog(filename('../data/USGS_SC_1990-2019.catalog'))
