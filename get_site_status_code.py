import requests


def get_site_status_code_by_excel(file_name=None):

    if file_name is not None:
        import pandas
        df = pandas.read_excel(file_name)
        df["status_code"] = df.apply(lambda x: get_site_status_code(x["url"]), axis=1)
        df.to_excel(file_name, index=False)


def get_site_status_code_by_csv(file_name=None):
    if file_name is not None:
        import pandas
        df = pandas.read_csv(file_name)
        df["status_code"] = df.apply(lambda x: get_site_status_code(x["url"]), axis=1)
        df.to_csv(file_name, index=False)


def get_site_status_code(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code
    except requests.exceptions.ConnectTimeout as e:
        return "Timeout"
    except Exception as e:
        print(e)
        return None


