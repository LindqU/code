def country_code(output,file_name):
    '''
    ***help***
    output : 現状csvのみ
    file_name : 任意のファイルネームを取得
    今回使用しているpandas.read_htmlは、lxml、html5lib、
    beautifulsoup4が必要なので、pipでインストールしておく
    '''
    import pandas as pd
    url = "https://www-yousei.jsps.go.jp/yousei1/kuniList.do"
    dfs = pd.read_html(url,header = 0)
    if output == "csv":
        dfs[0].to_csv(file_name + ".csv")
    return dfs[0]
