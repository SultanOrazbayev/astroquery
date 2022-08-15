import os


def get_package_data():
    paths_test = [os.path.join('data', '*.json'),
                  os.path.join('data', '*.fits')]

    return {'astroquery.cds.tests': paths_test}
