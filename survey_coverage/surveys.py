import numpy as np
import pandas as pd
from mocpy import MOC
import matplotlib.pyplot as plt
from survey_coverage.utils import get_wcs
from glob import glob
from pathlib import Path


class BaseSurvey:

    @property
    def coverage_type(self):
        raise NotImplementedError

    def __init__(self,
                 survey_name,
                 coverage_file):
        self.survey_name = survey_name
        self.coverage_file = coverage_file

    def plot_coverage(self):
        raise NotImplementedError


class MOCSurvey(BaseSurvey):
    """
    Class where the survey coverage is given in the healpix multi-order-coverage (MOC)
    format
    See : https://www.ivoa.net/documents/MOC/20190215/WD-MOC-1.1-20190215.pdf
    """

    coverage_type = "moc"

    def __init__(self,
                 *args,
                 **kwargs):
        super(MOCSurvey, self).__init__(*args, **kwargs)
        self.moc = MOC.from_fits(self.coverage_file)

    def plot_coverage(self,
                      band=None,
                      ax=None,
                      wcs=None,
                      border=True,
                      **kw_mpl):
        if wcs is None:
            wcs = get_wcs()

        if ax is None:
            fig = plt.figure(figsize=(15, 7))
            ax = plt.subplot(projection=wcs)

        self.moc.fill(ax=ax,
                      wcs=wcs,
                      **kw_mpl)

        if border:
            self.moc.border(ax=ax, wcs=wcs, alpha=0.7, color="black")
        return ax


known_surveys = {}
datadir = Path(__file__).parent.joinpath("data")
maplist = np.sort(glob(f'{datadir.as_posix()}/*-DR*.fits'))
survey_instrument_mapping = {'UKIRT': ['dxs', 'gcs', 'gps', 'las', 'uds', 'uhs'],
                             'VISTA': ['vhs', 'video', 'viking', 'vmc', 'vvv']}
for mapname in maplist:
    survey_name = mapname.split('/')[-1].split('-')[0]
    band_name = mapname.split('/')[-1].split('-')[1]
    survey_instrument = ''
    for instrument in survey_instrument_mapping:
        if survey_name in survey_instrument_mapping[instrument]:
            survey_instrument = instrument

    survey_string = f"{survey_instrument}-{survey_name}-{band_name}"
    known_surveys[survey_string] = MOCSurvey(survey_name='ukirt-uhs',
                                             coverage_file=mapname
                                             )